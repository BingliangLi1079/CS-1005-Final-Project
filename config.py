"""Configuration constants for XRP line navigation."""

CONFIG = {
    "line_threshold": 0.8,
    "base_speed": 0.25,
    "kp": 1.1,
    "turn_speed": 0.37,
    "forward_clear_time": 0.5,
    "arc_time": 0.6,
    "forward_exit_time": 0.25,
    "intersection_delay": 0.25,
    "turn_timeout": 5.0,
    "search_push_time": 0.6,
    "search_pause": 0.1,
}


def get(key: str):
    """Return a configuration value by key."""
    return CONFIG[key]
