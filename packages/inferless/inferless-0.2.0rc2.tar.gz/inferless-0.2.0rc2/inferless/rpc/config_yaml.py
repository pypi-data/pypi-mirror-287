import json


def get_config_yaml():
    # read the file inferless.yaml in the current directory as a json string
    try:
        with open("inferless.yaml", "r") as file:
            config_yaml = file.read()
            return config_yaml
    except FileNotFoundError:
        raise Exception("Configuration file inferless.yaml not found in the current directory")
    except Exception as e:
        raise Exception(f"Error reading inferless.yaml file: {e}")
