import json

TIMEZONE_FILE = "user_timezones.json"

def load_timezones():
    try:
        with open(TIMEZONE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_timezones(data):
    with open(TIMEZONE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def set_timezone(user_id, timezone):
    zones = load_timezones()
    zones[str(user_id)] = timezone
    save_timezones(zones)

def get_timezone(user_id):
    zones = load_timezones()
    return zones.get(str(user_id), None)
