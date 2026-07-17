"""
Dashboard - Get Robot State
============================
Connect via the Dashboard Server and read the current robot state:
robot mode, loaded program, program running state, and Polyscope version.

The Dashboard Server is available on port 29999 on all Polyscope robots
(CB-Series and e-Series). It does not require any special robot option.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - Dashboard: Get Robot State")
print("=" * 60)

robot = connect_robot(enable_dashboard=True)

try:
    # --- Robot mode (RUNNING, IDLE, POWER_OFF, ...) ---
    mode_resp = robot.dashboard.get_robot_mode()
    print(f"Robot mode     : {mode_resp.value}")

    # --- Loaded program ---
    prog_resp = robot.dashboard.get_loaded_program()
    loaded = prog_resp.value if prog_resp.value else "(none)"
    print(f"Loaded program : {loaded}")

    # --- Program running state ---
    running_resp = robot.dashboard.is_program_running()
    print(f"Program running: {running_resp.value}")

    # --- Polyscope version ---
    ver_resp = robot.dashboard.get_polyscope_version()
    print(f"Polyscope ver  : {ver_resp.value}")

    # --- Safety status ---
    safety_resp = robot.dashboard.get_safety_status()
    print(f"Safety status  : {safety_resp.value}")

finally:
    robot.disconnect()
    print("\nDisconnected.")


