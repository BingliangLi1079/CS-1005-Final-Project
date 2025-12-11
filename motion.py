"""Basic motion helpers."""
import time
from safety import within_effort_bounds


def forward_for(drivetrain, t: float, spd: float) -> None:
    """Drive forward at speed for t seconds, then stop."""
    effort = within_effort_bounds(spd)
    drivetrain.set_effort(effort, effort)
    time.sleep(t)
    drivetrain.stop()
