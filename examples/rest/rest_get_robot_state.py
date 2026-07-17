"""
REST API - Get Robot State (PolyscopeX)
=========================================
Connect to a PolyscopeX robot via the REST API and read the
current robot state and program state.

The REST API is available on port 80 (HTTP) and is specific to
PolyscopeX robots (UR software version 9+).
It provides a modern HTTP interface to control the robot.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - REST API: Get Robot State (PolyscopeX)")
print("=" * 60)

robot = connect_robot(enable_rest=True)

try:
    # --- Program state ---
    prog_state = robot.rest.get_program_state()
    print(f"Program state: {prog_state.value}")

finally:
    robot.disconnect()
    print("\nDisconnected.")


