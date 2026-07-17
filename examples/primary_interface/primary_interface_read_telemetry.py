"""
Primary Interface - Read Robot Telemetry Packets
==================================================
Connect via the Primary Interface and subscribe to real-time telemetry
events: robot mode, joint data, TCP cartesian position, and tool data.

The Primary Interface (port 30001) streams binary data packets from the
robot controller at ~10 Hz. This is useful for monitoring robot state
without the complexity of RTDE.

Press Ctrl+C to stop.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - Primary Interface: Read Telemetry Packets")
print("=" * 60)
print("Press Ctrl+C to stop.\n")

robot = connect_robot(enable_primary_interface=True)

import time as _time
_last_print = [0.0]  # use a list so the inner functions can update it

def _should_print():
    """Throttle: print at most once per second."""
    now = _time.monotonic()
    if now - _last_print[0] >= 1.0:
        _last_print[0] = now
        return True
    return False

# --- Subscribe to robot mode updates ---
@robot.primary_interface.robot_mode_data_received
def on_robot_mode(sender, event):
    if not _should_print():
        return
    e = robot.primary_interface.robot_mode_data
    print(f"[RobotMode] connected={e.physical_robot_connected}  "
          f"power_on={e.robot_power_on}  "
          f"mode={e.robot_mode}  "
          f"program_running={e.program_running}")

# --- Subscribe to joint data ---
@robot.primary_interface.joint_data_received
def on_joints(sender, event):
    j = robot.primary_interface.joint_data
    joints = [j.base, j.shoulder, j.elbow, j.wrist1, j.wrist2, j.wrist3]
    q_deg = [round(jnt.position * 57.2958, 2) for jnt in joints]
    print(f"[Joints   ] {q_deg} deg")

# --- Subscribe to cartesian info ---
@robot.primary_interface.cartesian_info_received
def on_cartesian(sender, event):
    c = robot.primary_interface.cartesian_info
    print(f"[Cartesian] x={c.x:.4f} m  y={c.y:.4f} m  z={c.z:.4f} m  "
          f"rx={c.rx:.4f}  ry={c.ry:.4f}  rz={c.rz:.4f}")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    robot.disconnect()
    print("Disconnected.")


