"""
REST API - Power On and Brake Release (PolyscopeX)
====================================================
Connect to a PolyscopeX robot via the REST API and perform the
standard startup sequence: power on the arm, then release the brakes.

This brings the robot from IDLE to RUNNING state entirely from Python,
without touching the teach pendant.

Prerequisites:
- PolyscopeX robot (version 9+)
- Robot in Remote Control mode
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.universal_robots.rest.robot_state_action import RobotStateAction

print("=" * 60)
print("  UR SDK - REST API: Power On & Brake Release (PolyscopeX)")
print("=" * 60)
print()

robot = connect_robot(enable_rest=True)

try:
    confirm = input("Power on the robot and release brakes via REST API? (y/n): ").strip().lower()
    if confirm != "y":
        print("Aborted.")
    else:
        # Step 1 - Power on
        print("\nPowering on...")
        resp = robot.rest.power_on()
        print(f"  Power on     : {resp}")

        # Step 2 - Release brakes
        print("Releasing brakes...")
        resp = robot.rest.brake_release()
        print(f"  Brake release: {resp}")

        print("\nRobot should now be in RUNNING state.")

finally:
    robot.disconnect()
    print("\nDisconnected.")


