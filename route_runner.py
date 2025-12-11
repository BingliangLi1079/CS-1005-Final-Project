"""Run a route comprised of S/L/R steps."""
from line_follow import follow_until_intersection
from motion import forward_for
from turn_logic import turn_left_90, turn_right_90


def run_route(drivetrain, reflectance, route: list[str], cfg, sleep=None) -> None:
    """Execute a sequence of S/L/R steps using line follow and turning primitives."""
    sleep_fn = sleep
    for step in route:
        follow_until_intersection(drivetrain, reflectance, cfg, sleep=sleep_fn or __import__("time").sleep)
        if step == "L":
            turn_left_90(drivetrain, reflectance, cfg, sleep=sleep_fn or __import__("time").sleep)
        elif step == "R":
            turn_right_90(drivetrain, reflectance, cfg, sleep=sleep_fn or __import__("time").sleep)
        elif step == "S":
            forward_for(drivetrain, cfg["forward_exit_time"], cfg["base_speed"])
        else:
            print(f"Unknown route step: {step}")
