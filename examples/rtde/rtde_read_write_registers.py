"""
RTDE - Read and Write Integer Registers
==========================================
Connect via RTDE and demonstrate bidirectional data exchange using
the general-purpose integer output registers (output_int_register_24..47)
and input integer registers (input_int_register_24..47).

Use case: exchange values between an external application and a URScript
program running on the robot.

The upper range (registers 24-47) is reserved for external RTDE clients.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from underautomation.universal_robots.rtde.rtde_input_values import RtdeInputValues
from examples import setup_license, get_robot_ip

print("=" * 60)
print("  UR SDK - RTDE: Read & Write Integer Registers")
print("=" * 60)
print()

setup_license()
robot_ip = get_robot_ip()

robot = UR()
params = ConnectParameters(robot_ip)
params.rtde.enable = True
params.rtde.frequency = 10


# Subscribe to integer input registers (PC → robot)
params.rtde.input_setup.add(RtdeInputData.InputIntRegisters, 24)  # int_register_24
params.rtde.output_setup.add(RtdeOutputData.InputIntRegisters, 24)  # int_register_24

print(f"\nConnecting to {robot_ip} (RTDE @ 10 Hz)...")
robot.connect(params)
print("Connected!\n")

# --- Read: display the current value of output register 24 ---
packet_count = 0


written = False

@robot.rtde.output_data_received
def on_data(sender, event):
    global packet_count
    packet_count += 1
    if packet_count % 10 == 0:
        val = robot.rtde.output_data_values.input_int_registers.x24
        if written:
            print(f"  output_int_register_24 = {val}")

print("Streaming output_int_register_24 for 3 seconds...")
time.sleep(3)

val = robot.rtde.output_data_values.input_int_registers.x24

print(f"  output_int_register_24 = {val}")

# --- Write: send a value to input register 24 (readable by URScript) ---
value_str = input("\nEnter integer value to write to input_int_register_24: ").strip()
try:
    value = int(value_str)
    inputs = RtdeInputValues()
    inputs.input_int_registers.x24 = value
    robot.rtde.write_inputs(inputs)
    written = True

    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped by user.")
except ValueError:
    print("Invalid integer. Skipping write.")
finally:
    robot.disconnect()
    print("Disconnected.")

