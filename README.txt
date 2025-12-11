README - XRP Grid Line Navigation

Run the unit tests:
- Ensure Python is available, then from the project root run:
  python -m pytest
- For coverage details, run:
  coverage run -m pytest && coverage report

Run the robot program (on hardware):
- Deploy to the XRP or run on the device with XRPLib installed:
  python main.py
- The script waits for the button press, blinks the LED, follows the grid line, performs S/L/R steps, and stops at the end.
- Adjust parameters in config.py to tune speeds, thresholds, and timings for your taped grid.
