#!/usr/bin/env python

import argparse
import importlib
import importlib.metadata
import json
import pathlib
import shutil
import sys
import yaml
import yaml.parser
from typing import Dict, List

from . import contexts_utils, utils
from .stores import StoreInterface, fill_secret, read_secret


VERSION = importlib.metadata.version("secenv")
IS_INTERACTIVE = __name__ == "__main__"


config = {}
no_config_available = True
config_location = pathlib.Path(".secenv.yaml").resolve()


def load_config():
    """
    Load the configuration file and converts it from YAML to a Python object.
    If it's in a Git repository, look up to root directory, otherwise current directory only.
    """
    global config, no_config_available, config_location
    possible_path = pathlib.Path(".").resolve()
    paths_to_scan = [possible_path]
    if utils.is_git_directory(possible_path):
        while not pathlib.Path(possible_path / ".git").is_dir():
            possible_path = (possible_path / "..").resolve()
            paths_to_scan.append(possible_path)

    for path in paths_to_scan:
        try:
            if pathlib.Path(path / ".secenv.yaml").exists():
                config = yaml.load(open(path / ".secenv.yaml", "r"), Loader=yaml.Loader)
                config_location = pathlib.Path(path / ".secenv.yaml").resolve()
                break
            elif pathlib.Path(path / ".secenv.yml").exists():
                config = yaml.load(open(path / ".secenv.yml", "r"), Loader=yaml.Loader)
                config_location = pathlib.Path(path / ".secenv.yml").resolve()
                break

        except yaml.parser.ParserError as e:
            print("Config error: config is not a valid YAML file:", e)
            return
    else:
        print("Config error: .secenv.yaml not found")

    if config:
        no_config_available = False
    else:
        print("Config error: file is empty")


def dump_config(destination: pathlib.Path = config_location):
    """
    Dump the currently loaded configuration into a YAML file.
    """
    if destination.exists():
        print(f"Copied previous config into '{destination.name+'.bak'}'")
        shutil.copy(destination, destination.name + ".bak")

    with open(destination, "w") as f:
        yaml.dump(config, f)
        print(f"Successfully dumped config into '{f.name}'")


def gen_parser(stores: Dict[str, StoreInterface]) -> argparse.ArgumentParser:
    """
    Parse the arguments provided to the program.

    Args:
        stores (Dict[str, StoreInterface]): A dictionary where the keys are the name of
            the store and the keys are the StoreInterface instantiations

    Returns:
        argparse.ArgumentParser: A parser ready to being consumed by the application
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # secenv version
    subparsers.add_parser("version", help="get secenv version")

    # secenv validate
    subparsers.add_parser("validate", help="validate secenv config")

    # secenv stores
    subparsers.add_parser("stores", help="list the available stores")

    # secenv secrets {fill, get} STORE SECRET [KEY]
    # subparsers_group.add_parser("secrets", help="fill secrets in the stores")
    secrets_parser = subparsers.add_parser("secrets", help="manage secrets in the stores")
    secrets_subparsers = secrets_parser.add_subparsers(dest="secrets_command")
    secrets_get_parser = secrets_subparsers.add_parser("get", help="get secrets in the stores")
    secrets_get_subparser = secrets_get_parser.add_subparsers(dest="secrets_get_store")

    secrets_fill_parser = secrets_subparsers.add_parser("fill", help="fill secrets in the stores")
    secrets_fill_parser.add_argument("store", help="the store to fill the secret in", nargs="?")
    secrets_fill_parser.add_argument("secret", help="the secret to fill", nargs="?")

    for store in stores:
        if "extends" in config["stores"][store]:
            extended = config["stores"][store]["extends"]
            type = config["stores"][extended]["type"]
        else:
            type = config["stores"][store]["type"]
        store_subparser = secrets_get_subparser.add_parser(
            store,
            help=f"query store '{store}' of type '{type}'",
        )
        stores[store].gen_parser(store_subparser)

    # secenv contexts list
    # secenv contexts gen CONTEXT
    contexts_parser = subparsers.add_parser("contexts", help="manage available contexts")
    contexts_subparsers = contexts_parser.add_subparsers(dest="contexts_command")
    contexts_subparsers.add_parser("list", help="list contexts")
    contexts_gen_subparsers = contexts_subparsers.add_parser("gen", help="generate an environment based on a context")
    contexts_gen_subparsers.add_argument("context")
    contexts_gen_subparsers.add_argument(
        "-o",
        "--output-format",
        choices=contexts_utils.available_formats,
        default="shell",
        dest="format",
        help="output format",
    )

    # secenv sync
    sync_parser = subparsers.add_parser("sync", help="sync the defined and existing secrets")
    sync_parser.add_argument("store", help="the store to sync the secret in", nargs="?")
    sync_parser.add_argument("secret", help="the secret to sync", nargs="?")

    return parser


def find_stores() -> Dict[str, StoreInterface]:
    """
    Find the stores defined in the configuration object.
    For each found store, instantiate it based on its type.

    Returns:
        Dict[str, StoreInterface]: A dictionary where the keys are the name of the
            stores and the keys are the StoreInterface instantiations

    Raises:
        SystemExit: If the configuration is not valid
    """
    stores = {}
    if "stores" not in config or not config["stores"]:
        return stores

    for name in config["stores"]:
        infos = config["stores"][name]

        if "extends" in infos:
            extended = infos["extends"]
            if extended not in config["stores"]:
                print("Config error: extended store does not exist:", extended)
                sys.exit(1)
            extended_infos = config["stores"][extended]
            extended_infos.update(infos)
            infos = extended_infos

        try:
            store = importlib.import_module(f".stores.{infos['type']}", package="secenv")
        except ModuleNotFoundError:
            print(f"Config error: no store defined as '{infos['type']}'")
            sys.exit(1)
        stores[name] = store.Store(name, infos)

    return stores


def sync_secrets(stores: Dict[str, StoreInterface]) -> None:
    """
    Sync the secrets defined in the configuration object and the ones already existing in the stores.

    Args:
        stores (Dict[str, StoreInterface]): A dictionary where the keys are the name of
            the stores and the keys are the StoreInterface instantiations
    """
    if "secrets" not in config:
        config["secrets"] = []

    for store_name, store_obj in stores.items():
        specified_secrets = {s["secret"]: s for s in config["secrets"] if s["store"] == store_name}
        detected_secrets = store_obj.list_secrets()

        # check for secrets' existence
        for secret_name in detected_secrets:
            if secret_name not in specified_secrets:
                # secret is not defined in the config
                print(f"Secret filled but missing from configuration: {store_name}/{secret_name}")
                config["secrets"].append({"secret": secret_name, "store": store_name})

        config_secrets_as_map = {s["secret"]: s for s in config["secrets"] if s["store"] == store_name}

        # now they are sync-ed, check for the keys
        for secret_name in config_secrets_as_map:
            try:
                secret = store_obj.read_secret(secret_name)
                if not isinstance(secret, dict):
                    secret = json.loads(secret)
            except utils.SecretNotFoundError:
                print(f"Secret specified but not filled: {store_name}/{secret_name}")
                continue
            except json.JSONDecodeError:
                continue

            if not isinstance(secret, dict):
                # JSON will load '1' but it's not a map with actual keys
                continue

            specified_keys = set(config_secrets_as_map[secret_name].get("keys", []))
            detected_keys = set(secret.keys())
            detected_but_not_specified = list(detected_keys - specified_keys)
            specified_but_not_detected = list(specified_keys - detected_keys)

            if detected_but_not_specified:
                print(f"Detected but not specified keys for {store_name}/{secret_name}:", *detected_but_not_specified)
            if specified_but_not_detected:
                print(f"Specified but not detected keys for {store_name}/{secret_name}:", *specified_but_not_detected)

            config_secrets_as_map[secret_name]["keys"] = list(specified_keys | detected_keys)

    if IS_INTERACTIVE and utils.yes_no("Write config down?"):
        dump_config()


def fill_secrets(stores: Dict[str, StoreInterface]) -> None:
    """
    Fill the secrets defined in the configuration object.

    Args:
        stores (Dict[str, StoreInterface]): A dictionary where the keys are the name of
            the stores and the keys are the StoreInterface instantiations
    """
    for secret_config in config["secrets"]:
        if "secret" not in secret_config:
            print("Config error: a secret has no name")
            continue
        secret_name = secret_config["secret"]

        if "store" not in secret_config:
            print(f"Config error: 'store' not found in secret {secret_name}")
            sys.exit(1)

        if secret_config["store"] not in stores:
            print(f"Config error: store '{secret_config['store']}' not found")
            sys.exit(1)

        store = stores[secret_config["store"]]
        secret = {k: v for k, v in secret_config.items() if k not in ["store"]}
        fill_secret(store, secret)


def gen_context(name: str, stores: Dict[str, StoreInterface]) -> Dict[str, str]:
    """
    Generate the context specified in the configuration object.

    Args:
        name (str): Name of the context to generate
        stores (Dict[str, StoreInterface]): A dictionary where the keys are the name of
            the stores and the keys are the StoreInterface instantiations

    Returns:
        Dict[str, str]: A dictionary of variables with their associated values

    Raises:
        SystemExit: If the configuration is not valid
    """
    context_config = config["contexts"][name]
    output = {}

    if context_config is None:
        print(f"Config error: context '{name}' is empty")
        sys.exit(1)

    if "extends" in context_config:
        for extended in context_config["extends"]:
            if extended not in config["contexts"]:
                print(f"Config error: try to extend an unexistent context '{extended}'")
                sys.exit(1)
            if extended == name:
                print("Config error: can't extend a context with itself")
                sys.exit(1)
            extended_context = gen_context(extended, stores)
            output.update(extended_context)

    if "vars" in context_config:
        output.update(contexts_utils.gen_vars(context_config["vars"], stores))

    if "aws_assume_role" in context_config:
        creds = {}
        creds["key_id"] = context_config["aws_assume_role"]["aws_access_key_id"]
        creds["secret_key"] = context_config["aws_assume_role"]["aws_secret_access_key"]
        creds["role"] = context_config["aws_assume_role"]["role_arn"]

        output.update(contexts_utils.gen_aws_assume_role(creds, stores))

    return output


def list_stores() -> str:
    """
    List the stores specified in the configuration object.

    Returns:
        str: List of the stores separated by newlines
    """
    return "\n".join(config.get("stores", ""))


def list_contexts() -> str:
    """
    List the contexts specified in the configuration object.

    Returns:
        str: List of contexts separated by newlines
    """
    return "\n".join(config.get("contexts", ""))


def validate_config() -> List[str]:
    """
    Validate a configuration file.

    Returns:
        List[str]: List of found errors
    """

    load_config()

    logs = []

    if "stores" not in config:
        config["stores"] = {}
    for name, obj in config["stores"].items():
        if "type" in obj and "extends" in obj:
            logs.append(f"Store '{name}' contains both 'type' and 'extends' keys")

        if "type" not in obj and "extends" not in obj:
            logs.append(f"Store '{name}' contains neither 'type' nor 'extends' keys")

        if "extends" in obj and obj["extends"] not in config["stores"]:
            logs.append(f"Store '{name}' extends an inexistent store '{obj['extends']}'")

    if "secrets" not in config:
        config["secrets"] = []
    for idx, obj in enumerate(config["secrets"]):
        if "store" not in obj:
            logs.append(f"Secret {idx} doesn't contain the 'store' key")
        if "secret" not in obj:
            logs.append(f"Secret {idx} doesn't contain the 'secret' key")
        if "store" in obj and obj["store"] not in config["stores"]:
            logs.append(f"Secret {idx} references an inexistent store '{obj['store']}'")
        if "generate" in obj and "type" not in obj["generate"]:
            logs.append(f"Secret {idx} generation doesn't have a type")

    if "contexts" not in config:
        config["contexts"] = {}
    for name, obj in config["contexts"].items():
        for extended in obj.get("extends", []):
            if extended not in config["contexts"]:
                logs.append(f"Context '{name}' extends an inexistent context '{extended}'")

        for var_name, var_obj in obj.get("vars", {}).items():
            if type(var_obj) is str:
                continue
            if "store" not in var_obj:
                logs.append(f"Secret '{name}/{var_name}' doesn't contain the 'store' key")
            if "store" in var_obj and var_obj["store"] not in config["stores"]:
                logs.append(f"Secret '{name}/{var_name}' references an inexistent store '{var_obj['store']}'")
            if "secret" not in var_obj:
                logs.append(f"Secret '{name}/{var_name}' doesn't contain the 'secret' key")
            if "key" in var_obj and type(var_obj["key"]) is not str:
                logs.append(
                    f"Secret '{name}/{var_name}' defines 'key' with wrong type '{type(var_obj['key'])}' (expects 'str')"
                )
            if "sensitive" in var_obj and type(var_obj["sensitive"]) is not bool:
                logs.append(
                    f"Secret '{name}/{var_name}' defines 'sensitive' with wrong type '{type(var_obj['sensitive'])}' (expects 'bool')"
                )

    return logs


def main():
    if len(sys.argv) == 2 and "version" == sys.argv[1]:
        # secenv version
        print(f"secenv version {VERSION}")
        sys.exit(0)

    load_config()
    stores = {} if no_config_available else find_stores()

    # Listing subparsers from an `argparse.ArgumentParser` is not straightforward
    # because the standard library doesn't provide a direct method to retrieve them.
    # However, one can access them indirectly by inspecting the parser's internal structures.
    #
    # The iterator is to cast it from `Iterable[any]` to a more typing-friendly value.
    #
    # It's safe to ignore the type warning as `choices` is actually a `dict`.
    parser = gen_parser(stores)
    subparsers: Dict[str, argparse.ArgumentParser] = {k: v for k, v in parser._actions[1].choices.items()}  # type: ignore

    args = parser.parse_args()

    if len(sys.argv) == 1:
        # secenv
        parser.print_help()
        return

    elif args.command == "stores":
        print(list_stores())
        return

    elif args.command == "secrets":
        if not args.secrets_command:
            # secenv secrets
            subparsers["secrets"].print_help()

        if args.secrets_command == "fill":
            # secenv secrets fill
            if "secrets" not in config:
                print("Config error: 'secrets' block is not present")
                sys.exit(1)
            if not args.store and not args.secret:
                fill_secrets(stores)
            if args.store and not args.secret:
                if args.store not in list_stores():
                    print(f"Usage error: store '{args.store}' not found")
                    sys.exit(1)
                dict_with_one_store = {args.store: stores[args.store]}
                fill_secrets(dict_with_one_store)
            if args.store and args.secret:
                if args.store not in list_stores():
                    print(f"Usage error: store '{args.store}' not found")
                    sys.exit(1)
                for secret_obj in config["secrets"]:
                    if secret_obj["store"] != args.store or secret_obj["secret"] != args.secret:
                        continue
                    generate_obj = utils.SecretType.from_config(secret_obj["generate"])
                    stores[secret_obj["store"]].fill_secret(secret_obj["secret"], generate_obj)
                    break
                else:
                    print(f"Config error: secret {args.store}/{args.secret} not found")
                    sys.exit(1)

        if args.secrets_command == "get":
            # secenv secrets get
            try:
                store_obj = stores[args.secrets_get_store]
            except KeyError:
                # Same technique as above with the subparsers
                subparsers["secrets"]._actions[1].choices["get"].print_help()  # type: ignore
                return

            unwanted_args_for_query = ["type", "command", "secrets_get_store", "secrets_command"]
            args = {k: v for k, v in vars(args).items() if k not in unwanted_args_for_query and v}
            result = read_secret(store_obj, args)
            print(result)

        return

    elif args.command == "contexts":
        if not args.contexts_command:
            # secenv contexts
            subparsers["contexts"].print_help()
            return

        if args.contexts_command == "list":
            # secenv contexts list
            print(list_contexts())
            return

        if args.contexts_command == "gen":
            # secenv contexts gen
            context_name = args.context
            if "contexts" not in config or context_name not in config["contexts"]:
                print(f"Config error: context '{context_name}' not found")
                print("Run `secenv contexts list` first")
                sys.exit(1)
            ctx = gen_context(context_name, stores)
            print(contexts_utils.format_output(ctx, args.format))
            return

    elif args.command == "validate":
        # secenv validate
        errors = validate_config()
        if not errors:
            print("Configuration valid!")
        else:
            print("\n".join(errors))
        return

    elif args.command == "sync":
        # secenv sync
        if not args.store and not args.secret:
            sync_secrets(stores)
        if args.store and not args.secret:
            if args.store not in list_stores():
                print(f"Usage error: store '{args.store}' not found")
                sys.exit(1)
            dict_with_one_store = {args.store: stores[args.store]}
            sync_secrets(dict_with_one_store)
        # TODO: sync just one secret
        # if args.store and args.secret:
        #     if args.store not in list_stores():
        #         print(f"Usage error: store '{args.store}' not found")
        #         sys.exit(1)
        #     for secret_obj in config["secrets"]:
        #         if secret_obj["store"] != args.store or secret_obj["secret"] != args.secret:
        #             continue
        #         generate_obj = utils.SecretType.from_config(secret_obj["generate"])
        #         stores[secret_obj["store"]].sync_secret(secret_obj["secret"], generate_obj)
        #         break
        #     else:
        #         print(f"Config error: secret {args.store}/{args.secret} not found")
        #         sys.exit(1)

        return

    parser.print_help()
    parser.exit()


if __name__ == "__main__":
    main()
