import os
import argparse
import getpass
from tabulate import tabulate

from basket.basket_config.maas_config import MaaSConfig
from basket.basket_config.auths_config import AuthsConfig
from basket.openai_util.openai_util import OpenaiUtil

import coloredlogs, logging
coloredlogs.install()

# TODO: Hanle fail to parse yaml file
maas_config = MaaSConfig()
auths_config = AuthsConfig()

def maas_list():
    maas_providers = maas_config.providers

    # Construct table to print
    data = [["Service", "API KEY Configured", "Base URL"]]
    align = ("left", "center", "left")
    for provider in maas_providers:
        # TODO: check auths config to get configured MaaS
        if auths_config.get_auth(provider.name):
            available_string = "*"
        else:
            available_string = ""

        data.append([provider.name, available_string, provider.url])
    print(tabulate(data, headers="firstrow", tablefmt="pretty", colalign=align))

"""
Use the MaaS as current MaaS. Request for API KEY and update the local configuration file.
"""
def maas_use(name):
    maas_provider = maas_config.get_provider(name)
    if maas_provider == None:
        logging.error("Please use a valid MaaS name in {}. You can add new MaaS in 'maas_config.yaml'.".format(maas_config.list_maas_names()))
        return
    else:
        # Try to set API KEY
        if set_maas_apikey(maas_provider.name):
            # Update local config file
            auths_config.update_current_maas(maas_provider.name)
            logging.info("Success to use MaaS: {}".format(maas_provider.name))
            maas_list()
            list_current_config()

"""
Read environemnt variable or request user to input API KEY for MaaS.
"""
def set_maas_apikey(maas_name: str) -> bool:
    if auths_config.get_auth(maas_name):
        logging.info("API KEY has been initiliazed")
        return True
    else:
        logging.warning("API KEY for {} is not initialized".format(maas_name))

        apikey_env = "{}_API_KEY".format(maas_name.upper())
        logging.info("Try to read {} from environment variable".format(apikey_env))
        apikey = os.getenv(apikey_env, "")
        if apikey == "":
            logging.warning("Fail to load API KEY from environment variable, you can export {}='ak-xxx'".format(apikey_env))

            apikey = getpass.getpass(prompt="Please input the API KEY for {}: ".format(maas_name))
            logging.info("Success to get API KEY from user input")
        else:
            logging.info("Success to get API KEY from environment variable: {}".format(apikey_env))
        
        auths_config.add_auth(maas_name, apikey)
        return True
        
"""
Reset the API KEY for the MaaS.
"""
def maas_reset(name: str) -> None:
    maas_provider = maas_config.get_provider(name)
    if maas_provider == None:
        logging.error("Please use a valid MaaS name in {}. You can add new MaaS in 'maas_config.yaml'.".format(maas_config.list_maas_names()))
        return

    if auths_config.get_auth(name):
        logging.info("API KEY has been initiliazed, remove it")

        if auths_config.remove_auth(name):
            logging.info("Success to remove API KEY for {}".format(name))
        else:
            logging.info("Fail to reset API KEY for {}".format(name))
    else:
        logging.warning("The API KEY for {} is not initialized, ignore it".format(name))

"""
List the available models for MaaS.
"""
def model_list():
    logging.info("Listing models from {}".format(auths_config.get_current_maas()))
    if maas_config.get_provider(auths_config.get_current_maas()) == None:
        logging.error("Please choose MaaS and run 'basket maas use $name'")
        return
    
    if auths_config.get_current_maas().lower() == "zhipu":
        logging.warning("Zhipu does not support geting model list from OpenAI API")
        return

    base_url = maas_config.get_provider(auths_config.get_current_maas()).url
    api_key = auths_config.get_auth(auths_config.get_current_maas()).api_key
    openai_util = OpenaiUtil(base_url, api_key)

    model_infos = openai_util.list_available_models()

    # Construct table to print
    data = [["ID"]]
    for model_info in model_infos:
        data.append([model_info["id"]])
    print(tabulate(data, headers="firstrow", tablefmt="pretty", stralign="left"))


def model_use(name):
    # Update local config file
    auths_config.update_current_model(name)
    logging.info("Success to use Model: {}".format(name))
    list_current_config()

def list_current_config():
    print_maas_info = auths_config.get_current_maas()
    if print_maas_info == "":
        print_maas_info = "NOT SET (Please run: basket maas use $name)"
    logging.info("Current maas: {}".format(print_maas_info))

    print_model_info = auths_config.get_current_model()
    if print_model_info == "":
        print_model_info = "NOT SET (Please run: basket model use $name)"
    logging.info("Current model: {}".format(print_model_info))

def check_config() -> bool:
    if auths_config.get_current_maas() == "":
        logging.warning("Current MaaS is empty")
        return False
    if auths_config.get_current_model() == "":
        logging.warning("Current model is empty")
        return False
    
    if auths_config.get_auth(auths_config.get_current_maas()) == None or auths_config.get_auth(auths_config.get_current_maas()).api_key == "":
        logging.warning("The API KEY for MaaS is empty")
        return False
    return True

def chat(text):
    logging.info(f"chat with: {text}")

    if check_config() == False:
        logging.error("Please run 'basket use maas' and 'basket use model' or reset API KEY")
        list_current_config()
        return
    
    base_url = maas_config.get_provider(auths_config.get_current_maas()).url
    api_key = auths_config.get_auth(auths_config.get_current_maas()).api_key
    model = auths_config.get_current_model()

    openai_util = OpenaiUtil(base_url, api_key, model)
    output = openai_util.chat(text)
    print(output)


def main():
    parser = argparse.ArgumentParser(description="The MaaS management tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # MaaS command
    maas_parser = subparsers.add_parser("maas", help="MaaS related commands")
    maas_subparsers = maas_parser.add_subparsers(dest="maas_command")
    maas_subparsers.add_parser("list", help="List model as a service")
    maas_use_parser = maas_subparsers.add_parser("use", help="Use a specific MaaS")
    maas_use_parser.add_argument("name", type=str, help="Name of the MaaS to use")
    maas_reset_parser = maas_subparsers.add_parser("reset", help="Reset auths of a specific MaaS")
    maas_reset_parser.add_argument("name", type=str, help="Name of the MaaS to reset")

    # Model command
    model_parser = subparsers.add_parser("model", help="Model related commands")
    model_subparsers = model_parser.add_subparsers(dest="model_command")
    model_subparsers.add_parser("list", help="List models")
    model_use_parser = model_subparsers.add_parser("use", help="Use a specific model")
    model_use_parser.add_argument("name", type=str, help="Name of the model to use")

    # Config command
    config_parser = subparsers.add_parser("config", help="List the current config")

    # Chat command
    chat_parser = subparsers.add_parser("chat", help="Chat with MaaS model")
    chat_parser.add_argument("text", type=str, help="Chat text")

    args = parser.parse_args()

    if args.command == "maas":
        if args.maas_command == "list":
            maas_list()
        elif args.maas_command == "use":
            maas_use(args.name)
        elif args.maas_command == "reset":
            maas_reset(args.name)
    elif args.command == "model":
        if args.model_command == "list":
            model_list()
        elif args.model_command == "use":
            model_use(args.name)
    elif args.command == "config":
        list_current_config()
    elif args.command == "chat":
        chat(args.text)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()