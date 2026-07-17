"""
RTDE - Read Digital I/O States
================================
Connect via RTDE and read the current state of all digital inputs
and digital outputs from the robot controller.

Uses the ActualDigitalInputBits and ActualDigitalOutputBits fields:
- Bits 0-7  : Standard digital I/O
- Bits 8-15 : Configurable digital I/O
- Bits 16-17: Tool digital I/O

Press Ctrl+C to stop continuous monitoring.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from examples import setup_license, get_robot_ip

print("=" * 60)
print("  UR SDK - RTDE: Read Digital I/O States")
print("=" * 60)
print("Press Ctrl+C to stop.\n")

setup_license()
robot_ip = get_robot_ip()

robot = UR()
params = ConnectParameters(robot_ip)
params.rtde.enable = True
params.rtde.frequency = 5  # 5 Hz is plenty for I/O monitoring

params.rtde.output_setup.add(RtdeOutputData.ActualDigitalInputBits, 0)
params.rtde.output_setup.add(RtdeOutputData.ActualDigitalOutputBits, 0)
params.rtde.output_setup.add(RtdeOutputData.ActualTcpPose, 0)

print(f"\nConnecting to {robot_ip} (RTDE @ 5 Hz)...")
robot.connect(params)
print("Connected! Monitoring I/O...\n")

last_inputs  = None
last_outputs = None
last_tcp_pose = None

@robot.rtde.output_data_received
def on_data(sender, event):
    global last_inputs, last_outputs

    vals = robot.rtde.output_data_values
    din  = vals.actual_digital_input_bits   # integer bitmask
    dout = vals.actual_digital_output_bits  # integer bitmask
    tcp_pose = vals.actual_tcp_pose

    last_inputs  = din
    last_outputs = dout
    last_tcp_pose = tcp_pose

    print("  Digital INPUTS  (bits 0-17):", format(din  or 0, "018b")[::-1][:18])
    print("  Digital OUTPUTS (bits 0-17):", format(dout or 0, "018b")[::-1][:18])
    print("  (read left-to-right = DI0..DI17 / DO0..DO17)")
    print("  TCP POSE:", tcp_pose)
    print()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    robot.disconnect()
    print("Disconnected.")


