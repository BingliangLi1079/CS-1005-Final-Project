"""User start and announcements."""
import time


def wait_for_button(board, delay_s: float = 1.5, sleep=time.sleep) -> None:
    """Prompt user, wait for button press, blink LED, and delay before start."""
    print("Press button to start")
    while not board.is_button_pressed():
        sleep(0.05)
    board.led_blink(3)
    print(f"Starting in {delay_s}s...")
    sleep(delay_s)


def announce(msg: str) -> None:
    """Print a status message for the operator."""
    print(msg)
