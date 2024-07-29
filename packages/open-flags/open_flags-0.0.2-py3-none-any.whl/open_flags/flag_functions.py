import os
from .flag_map import FLAG_MAP

def get_flag_svg(country, region):
    key = f"{country}/{region}"
    if key not in FLAG_MAP:
        raise ValueError(f"SVG not found for {country}-{region}")
    with open(os.path.join(os.path.dirname(__file__), 'flags', FLAG_MAP[key]), 'r') as f:
        return f.read()

def get_all_flags():
    return list(FLAG_MAP.keys())

def get_flags_by_country(country):
    return [key for key in FLAG_MAP if key.startswith(f"{country}/")]
