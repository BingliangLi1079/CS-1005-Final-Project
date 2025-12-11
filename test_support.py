"""Test support utilities with simple fakes."""
import contextlib
from types import SimpleNamespace


def fake_reflectance(left_seq, right_seq):
    """Create a stub reflectance object yielding predefined readings."""
    left_idx = {"i": 0}
    right_idx = {"i": 0}

    def _next(seq, idx):
        value = seq[min(idx["i"], len(seq) - 1)]
        if idx["i"] < len(seq) - 1:
            idx["i"] += 1
        return value

    return SimpleNamespace(
        get_left=lambda: _next(left_seq, left_idx),
        get_right=lambda: _next(right_seq, right_idx),
    )


def fake_drivetrain():
    """Create a stub drivetrain capturing set_effort/stop calls."""
    state = {"efforts": []}

    def set_effort(left, right):
        state["efforts"].append((left, right))

    def stop():
        state["efforts"].append(("stop", "stop"))

    return SimpleNamespace(set_effort=set_effort, stop=stop, state=state)


def fake_board(button_presses: int = 1):
    """Create a stub board that simulates button presses and LED blinks."""
    presses = {"count": 0}

    def is_button_pressed():
        presses["count"] += 1
        return presses["count"] >= button_presses

    led_events = {"blinks": []}

    def led_blink(times):
        led_events["blinks"].append(times)

    return SimpleNamespace(is_button_pressed=is_button_pressed, led_blink=led_blink, presses=presses, led_events=led_events)


@contextlib.contextmanager
def fast_sleep():
    """Speed up time.sleep in tests to keep loops deterministic."""
    def _sleep(_duration):
        return None
    yield _sleep


def sample_route():
    """Provide a deterministic route for tests (e.g., ["S","L","R"])."""
    return ["S", "L", "R"]
