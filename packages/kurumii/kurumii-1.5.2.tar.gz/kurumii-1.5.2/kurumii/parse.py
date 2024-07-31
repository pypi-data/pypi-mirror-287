import re
import difflib

POSSIBILITIES = {
    "sec": "s", "secs": "s", "second": "s", "seconds": "s",
    "mi": "m", "min": "m", "mins": "m", "minute": "m", "minutes": "m",
    "h": "h", "hr": "h", "hrs": "h", "hour": "h", "hours": "h",
    "d": "d", "day": "d", "days": "d",
    "mo": "mo", "month": "mo", "months": "mo",
    "w": "w", "week": "w", "weeks": "w",   
    "y": "y", "year": "y", "years": "y",
    "ms": "ms", "millisecond": "ms", "milliseconds": "ms",
    "m": "m", "s": "s"
}

def parse_into_sec(time_str, custom_units=None, return_unknown=False, handle_typos=True):
    """Parses a time string into seconds.*

    - Args:
        - param time_str: The time string to parse.
        - custom_units: Optional dictionary of custom time units and their conversion to seconds.
        - return_unknown: If True, returns a tuple of (total_seconds, unknown_units).
        - handle_typos: If True, attempts to correct typos in time units.

    - Returns:
        - The total number of seconds represented by the time string.
        - If return_unknown is True, returns a tuple of (total_seconds, unknown_units).
    """

    # Default time units and their conversion to seconds
    time_units = {
        "ms": 0.001,
        "s": 1,
        "m": 60,
        "h": 3600,
        "d": 86400,
        "w": 604800,
        "mo": 2592000,
        "y": 31536000
    }

    # Add custom units if provided
    if custom_units:
        if isinstance(custom_units, dict):
            time_units.update(custom_units)
        elif isinstance(custom_units, list):
            for unit_dict in custom_units:
                time_units.update(unit_dict)

    time_str = time_str.replace(",", ".")
    time_str = time_str.lower()
    
    # Regular expression to match time units
    pattern = re.compile(r"(\d*\.?\d+)\s*([a-zA-Z]+)")
    matches = pattern.findall(time_str)
    
    total_seconds = 0
    unknown_units = []

    def get_closest_unit(unit):
        if handle_typos:
            choices = list(POSSIBILITIES.keys())
            closest_matches = difflib.get_close_matches(unit, choices, n=1, cutoff=0.8)
            return POSSIBILITIES.get(closest_matches[0], unit) if closest_matches else unit
        return unit

    for value, unit in matches:
        unit = unit.lower()  # case insensitive matching
        normalized_unit = get_closest_unit(unit)
        if normalized_unit in time_units:
            total_seconds += float(value) * time_units[normalized_unit]
        else:
            unknown_units.append([unit, value])

    if return_unknown:
        return total_seconds, unknown_units if unknown_units else None
    return total_seconds