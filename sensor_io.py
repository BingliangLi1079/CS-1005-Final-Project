"""Reflectance sensor helpers."""

def on_left(reflectance, threshold: float) -> bool:
    """Return True if left sensor is above the threshold."""
    return reflectance.get_left() > threshold


def on_right(reflectance, threshold: float) -> bool:
    """Return True if right sensor is above the threshold."""
    return reflectance.get_right() > threshold


def on_both(reflectance, threshold: float) -> bool:
    """Return True when both sensors exceed the threshold."""
    return on_left(reflectance, threshold) and on_right(reflectance, threshold)
