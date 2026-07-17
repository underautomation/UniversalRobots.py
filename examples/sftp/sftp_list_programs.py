"""
SFTP - List Programs on the Controller
=========================================
Connect via SFTP over SSH and list all .urp programs available
on the robot controller.

SFTP gives you full file system access to the UR controller.
Default SSH credentials: user='ur', password='easybot'.

Programs are typically stored in /programs/ on the robot.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - SFTP: List Programs on Controller")
print("=" * 60)
print()

robot = connect_robot(enable_sftp=True)

try:
    # --- List all .urp programs using the built-in helper ---
    print("Enumerating .urp programs on the controller...")
    programs = robot.sftp.enumerate_programs()
    print(f"Found {len(programs)} program(s):\n")
    for i, prog in enumerate(programs, 1):
        print(f"  {i:>3}. {prog}")

    # --- Also list the programs directory manually ---
    print()
    directory = input("List directory contents (default: /programs/): ").strip()
    if not directory:
        directory = "/programs/"

    print(f"\nContents of '{directory}':")
    files = robot.sftp.list_directory(directory)
    for f in files:
        kind = "DIR " if f.is_directory else "FILE"
        print(f"  [{kind}] {f.name}")

finally:
    robot.disconnect()
    print("\nDisconnected.")


