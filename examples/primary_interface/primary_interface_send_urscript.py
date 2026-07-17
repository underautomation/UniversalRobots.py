"""
Primary Interface - Send URScript Command
==========================================
Connect via the Primary Interface and send a URScript command
directly to the robot controller.

URScript is executed immediately on the robot. This is the simplest
way to move the robot or interact with digital I/O from Python.

WARNING: The robot will move! Make sure the area is clear and the robot
is in a safe position before running motion commands.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - Primary Interface: Send URScript Command")
print("=" * 60)
print()
print("WARNING: If you send a motion command, the robot WILL move!")
print()

robot = connect_robot(enable_primary_interface=True)

try:
    # --- Option 1: send a simple non-motion URScript ---
    print("Example 1 - Read a digital output via URScript (popup on teach pendant):")
    script = 'popup("Hello from Python SDK!", title="SDK Test", blocking=False)'
    print(f"  Sending: {script}")
    result = robot.primary_interface.script.send(script)
    print(f"  Result : {result}")
    print()

    # --- Option 2: let the user type their own script ---
    user_script = input(
        "Enter a URScript to send (leave empty to skip):\n"
        "  Example: set_digital_out(0, True)\n"
        "> "
    ).strip()

    if user_script:
        result = robot.primary_interface.script.send(user_script)
        print(f"  Result: {result}")
    else:
        print("Skipped.")

finally:
    robot.disconnect()
    print("\nDisconnected.")


