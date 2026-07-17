"""
Dashboard - Load and Play Program
===================================
Connect via the Dashboard Server and remotely load a .urp program,
then start it. This demonstrates basic remote control of the robot.

Requirements:
- The robot must be in Remote Control mode (Settings > Password > Remote Control)
- The program file must already exist on the robot controller
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - Dashboard: Load and Play Program")
print("=" * 60)

robot = connect_robot(enable_dashboard=True)

try:
    # List currently loaded program before anything
    loaded = robot.dashboard.get_loaded_program()
    print(f"Currently loaded: {loaded.value or '(none)'}")
    print()

    # Ask for the program name to load
    program_name = input("Enter program name to load (e.g. my_program.urp): ").strip()
    if not program_name:
        print("No program name provided. Skipping.")
    else:
        # --- Load program ---
        print(f"\nLoading '{program_name}'...")
        load_resp = robot.dashboard.load_program(program_name)
        print(f"Load response: {load_resp}")

        if load_resp.succeed:
            # --- Play ---
            play = input("\nProgram loaded. Start it? (y/n): ").strip().lower()
            if play == "y":
                play_resp = robot.dashboard.power_on()
                print(f"Power on response: {play_resp}")
                play_resp = robot.dashboard.release_brake()
                print(f"Release brake response: {play_resp}")
                play_resp = robot.dashboard.play()
                print(f"Play response: {play_resp}")

                stop = input("\nStop the program? (y/n): ").strip().lower()
                if stop == "y":
                    stop_resp = robot.dashboard.stop()
                    print(f"Stop response: {stop_resp}")
        else:
            print("Load failed. Check the program name and robot state.")

finally:
    robot.disconnect()
    print("\nDisconnected.")


