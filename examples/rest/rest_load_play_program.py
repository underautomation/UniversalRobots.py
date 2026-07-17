"""
REST API - Load and Play Program (PolyscopeX)
===============================================
Connect to a PolyscopeX robot via the REST API and remotely load
a program, then start it.

The REST API is available on PolyscopeX robots (UR software version 9+).
It replaces the Dashboard Server for newer robots and uses standard HTTP.

Prerequisites:
- PolyscopeX robot (version 9+)
- Robot must be powered on and brakes released
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.universal_robots.rest.robot_state_action import RobotStateAction
from underautomation.universal_robots.rest.program_state_action import ProgramStateAction

print("=" * 60)
print("  UR SDK - REST API: Load and Play Program (PolyscopeX)")
print("=" * 60)

robot = connect_robot(enable_rest=True)

try:
    # Check current program state
    state = robot.rest.get_program_state()
    print(f"Current program state: {state.value}")
    print()

    program_name = input("Enter program name to load (e.g. my_program): ").strip()
    if not program_name:
        print("No program name provided. Skipping.")
    else:
        # --- Load program ---
        print(f"\nLoading '{program_name}'...")
        load_resp = robot.rest.load_program(program_name)
        print(f"Load response: {load_resp}")

        if load_resp.succeed:
            play = input("\nProgram loaded. Start it? (y/n): ").strip().lower()
            if play == "y":
                play_resp = robot.rest.play()
                print(f"Play response: {play_resp}")

                stop = input("\nStop the program? (y/n): ").strip().lower()
                if stop == "y":
                    stop_resp = robot.rest.stop()
                    print(f"Stop response: {stop_resp}")

finally:
    robot.disconnect()
    print("\nDisconnected.")


