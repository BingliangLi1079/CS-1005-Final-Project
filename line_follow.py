"""Line-follow loop until an intersection is detected."""
import time
from safety import within_effort_bounds
from sensor_io import on_both


def follow_until_intersection(drivetrain, reflectance, cfg, sleep=time.sleep) -> None:
    """Follow the line with PD correction until both sensors see the line; stop then pause."""
    threshold = cfg["line_threshold"]
    base_speed = cfg["base_speed"]
    kp = cfg["kp"]

    while True:
        if on_both(reflectance, threshold):
            drivetrain.stop()
            print("Intersection detected")
            drivetrain.set_effort(base_speed, base_speed)
            sleep(cfg["forward_clear_time"])
            drivetrain.stop()
            sleep(cfg["intersection_delay"])
            return

        err = reflectance.get_right() - reflectance.get_left()
        cor = kp * err
        left = within_effort_bounds(base_speed - cor)
        right = within_effort_bounds(base_speed + cor)
        drivetrain.set_effort(left, right)
        sleep(0.01)
