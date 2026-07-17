"""
SFTP - Download a Program File
=================================
Connect via SFTP over SSH and download a .urp program file
from the robot controller to your local machine.

This lets you back up programs, inspect them locally, or
process them with the URPReader (XML-based .urp parser).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pathlib import Path
from examples import connect_robot

print("=" * 60)
print("  UR SDK - SFTP: Download a Program File")
print("=" * 60)
print()

robot = connect_robot(enable_sftp=True)

try:
    # List available programs first
    print("Available programs on the controller:")
    programs = robot.sftp.enumerate_programs()
    for i, p in enumerate(programs, 1):
        print(f"  {i:>3}. {p}")
    print()

    # Ask which program to download
    remote_path = input("Enter remote path to download (e.g. /programs/my_prog.urp): ").strip()
    if not remote_path:
        print("No path provided. Skipping.")
    else:
        # Build a local destination path in the current working directory
        filename = Path(remote_path).name
        local_path = str(Path.cwd() / filename)
        override = input(f"Save to '{local_path}'? (y/n): ").strip().lower()
        if override == "y":
            print(f"\nDownloading '{remote_path}'...")
            robot.sftp.download_file(remote_path, local_path)
            size = Path(local_path).stat().st_size
            print(f"Downloaded successfully: {local_path} ({size} bytes)")
        else:
            local_path = input("Enter local destination path: ").strip()
            if local_path:
                print(f"\nDownloading...")
                robot.sftp.download_file(remote_path, local_path)
                print(f"Downloaded to: {local_path}")

finally:
    robot.disconnect()
    print("\nDisconnected.")


