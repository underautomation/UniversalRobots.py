"""
SFTP - Upload a Program File
================================
Connect via SFTP over SSH and upload a local .urp program file
to the robot controller.

After uploading, the program can be loaded and run via the
Dashboard Server or directly from Polyscope.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pathlib import Path
from examples import connect_robot

print("=" * 60)
print("  UR SDK - SFTP: Upload a Program File")
print("=" * 60)
print()

robot = connect_robot(enable_sftp=True)

try:
    local_path = input("Enter local .urp file path to upload: ").strip()

    if not local_path or not Path(local_path).exists():
        print("File not found. Skipping.")
    else:
        filename = Path(local_path).name
        remote_path = f"/programs/{filename}"
        confirm = input(f"Upload to '{remote_path}'? (y/n) [or enter custom remote path]: ").strip()
        if confirm.lower() == "y":
            pass  # use default remote_path
        elif confirm.lower() != "n" and confirm:
            remote_path = confirm  # user provided a custom path

        if confirm.lower() != "n":
            print(f"\nUploading '{filename}' → '{remote_path}'...")
            robot.sftp.upload_file(local_path, remote_path)
            print(f"Upload complete.")
            print("The program is now available on the controller.")
            print("Load it via: robot.dashboard.load_program('my_program.urp')")

finally:
    robot.disconnect()
    print("\nDisconnected.")


