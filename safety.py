"""Safety helpers for clamping and timing."""
import time


def within_effort_bounds(value: float) -> float:
    """Clamp motor effort to [-1.0, 1.0]."""
    return max(min(value, 1.0), -1.0)


def check_timeout(start_time: float, timeout: float) -> bool:
    """Return True when elapsed time exceeds timeout."""
    return (time.time() - start_time) > timeout
