"""
Dashboard - Power On and Release Brakes
=========================================
Connect via the Dashboard Server and power on the robot arm,
then release the brakes so the robot is ready to move.

This is the standard sequence to bring a powered-off robot to
the RUNNING state without touching the teach pendant.

Prerequisites:
- Robot must be in Remote Control mode
- No safety violations or protective stops must be active
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - Dashboard: Power On & Release Brakes")
print("=" * 60)
print()

robot = connect_robot(enable_dashboard=True)

try:
    # Check current mode first
    mode = robot.dashboard.get_robot_mode()
    print(f"Current robot mode: {mode.value}")
    print()

    confirm = input("Power on the robot and release brakes? (y/n): ").strip().lower()
    if confirm != "y":
        print("Aborted.")
    else:
        # Step 1 - Power on the robot arm
        print("\nPowering on...")
        resp = robot.dashboard.power_on()
        print(f"  Power on : {resp}")

        # Step 2 - Release brakes (initialises the arm)
        print("Releasing brakes...")
        resp = robot.dashboard.release_brake()
        print(f"  Brakes   : {resp}")

        # Confirm new mode
        mode = robot.dashboard.get_robot_mode()
        print(f"\nNew robot mode: {mode.value}")

finally:
    robot.disconnect()
    print("\nDisconnected.")


