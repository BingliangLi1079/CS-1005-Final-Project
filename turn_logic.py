"""Grid-escape turning and line acquisition."""
import time
from safety import within_effort_bounds, check_timeout
from sensor_io import on_left, on_right


def turn_grid(drivetrain, reflectance, direction: str, cfg, sleep=time.sleep, now=time.time) -> None:
    """Perform grid-escape turn: push forward, arc, search for new line with timeout, then settle."""
    base_speed = cfg["base_speed"]
    turn_speed = cfg["turn_speed"]
    threshold = cfg["line_threshold"]

    drivetrain.set_effort(base_speed, base_speed)
    sleep(cfg["search_push_time"])
    drivetrain.stop()
    sleep(cfg["search_pause"])

    if direction == "left":
        drivetrain.set_effort(0.0, turn_speed)
    else:
        drivetrain.set_effort(turn_speed, 0.0)
    sleep(cfg["arc_time"])

    start_time = now()
    stage = 1
    while True:
        if direction == "left":
            drivetrain.set_effort(-turn_speed, turn_speed)
        else:
            drivetrain.set_effort(turn_speed, -turn_speed)

        left_val = reflectance.get_left()
        right_val = reflectance.get_right()

        if stage == 1 and left_val < threshold and right_val < threshold:
            stage = 2
            print("Cleared old line, searching for new one...")
        elif stage == 2 and (left_val > threshold or right_val > threshold):
            print("New line found")
            break

        if check_timeout(start_time, cfg["turn_timeout"]):
            print("Turn timeout")
            break
        sleep(0.01)

    drivetrain.stop()
    sleep(cfg["search_pause"])

    drivetrain.set_effort(base_speed, base_speed)
    sleep(cfg["forward_exit_time"])
    drivetrain.stop()
    sleep(cfg["intersection_delay"])


def turn_left_90(drivetrain, reflectance, cfg, sleep=time.sleep, now=time.time) -> None:
    """Wrapper to perform a left grid-escape turn."""
    turn_grid(drivetrain, reflectance, "left", cfg, sleep=sleep, now=now)


def turn_right_90(drivetrain, reflectance, cfg, sleep=time.sleep, now=time.time) -> None:
    """Wrapper to perform a right grid-escape turn."""
    turn_grid(drivetrain, reflectance, "right", cfg, sleep=sleep, now=now)
