"""Entrypoint for XRP line navigation."""
from config import CONFIG
from route_runner import run_route
from start_ui import announce, wait_for_button


def get_hardware():
    """Import XRP hardware modules; raise a helpful error if unavailable."""
    try:
        from XRPLib.defaults import drivetrain, reflectance, board  # type: ignore
    except Exception as exc:  # pragma: no cover - hardware import guard
        raise RuntimeError("XRPLib hardware not available; run on the robot.") from exc
    return drivetrain, reflectance, board


def main():
    """Run the predefined route using hub-and-spoke helpers."""
    announce("=== XRP GRID LINE NAVIGATION (Grid-Escape Turn) ===")
    drivetrain, reflectance, board = get_hardware()
    wait_for_button(board, delay_s=1.5)
    route = ["S", "L", "R", "R", "R", "R"]
    run_route(drivetrain, reflectance, route, CONFIG)
    drivetrain.stop()
    announce("=== ROUTE COMPLETE ===")


if __name__ == "__main__":
    main()
