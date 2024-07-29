import os
import configparser

def create_config():
    config = configparser.ConfigParser()
    config["API_KEYS"] = {"OPEN_AI_API_KEY": "", "ANTHROPIC_API_KEY": ""}
    config["USER_CFG"] = {"FIRST_USE": 1, "MODEL": "", "ollama_installed": 0}
    home_dir = os.path.expanduser("~")
    config_file = os.path.join(home_dir, ".aicli_config.ini")
    with open(config_file, "w") as configfile:
        config.write(configfile)
    