import json

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def get_data_source():
    config = load_config()
    return config.get("data_source", "google_sheets")

def set_data_source(source):
    config = load_config()
    config["data_source"] = source
    save_config(config)
