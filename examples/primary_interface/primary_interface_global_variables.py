"""
Primary Interface - Read Global Variables
==========================================
Connect via the Primary Interface and read the global variables
declared in the currently loaded Polyscope program.

Global variables are defined in the Polyscope installation or program
and are accessible via the Primary Interface. This is useful for
monitoring named variables shared between URScript and external code.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - Primary Interface: Read Global Variables")
print("=" * 60)
print()

robot = connect_robot(enable_primary_interface=True)

try:
    # Give the interface a moment to receive the variable list
    print("Waiting for global variables list...")
    time.sleep(2)

    # --- Get all declared global variables ---
    variables = robot.primary_interface.global_variables.get_all()

    if not variables:
        print("No global variables found.")
        print("Tip: Load a program with declared variables in Polyscope first.")
    else:
        print(f"Found {len(variables)} global variable(s):\n")
        for var in variables:
            print(f"  {var.name:<30} = {var.value}  (type: {var.type})")

    # --- Lookup a specific variable by name ---
    print()
    var_name = input("Look up a variable by name (leave empty to skip): ").strip()
    if var_name:
        var = robot.primary_interface.global_variables.get_by_name(var_name)
        if var:
            print(f"  {var.name} = {var.value}  (type: {var.type})")
        else:
            print(f"  Variable '{var_name}' not found.")

finally:
    robot.disconnect()
    print("\nDisconnected.")


