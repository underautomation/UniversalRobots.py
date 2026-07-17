"""
Dashboard - Show Popup Message
================================
Display a popup message on the Polyscope teach pendant screen,
then close it programmatically.

Useful for notifying the operator from an external application
without physically touching the teach pendant.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  UR SDK - Dashboard: Show Popup Message")
print("=" * 60)
print()

robot = connect_robot(enable_dashboard=True)

try:
    # Show a popup on the teach pendant
    message = input("Enter popup message (default: 'Hello from Python!'): ").strip()
    if not message:
        message = "Hello from Python!"

    print(f"\nShowing popup: '{message}'")
    resp = robot.dashboard.show_popup(message)
    print(f"Response: {resp}")

    input("\nPopup is now visible on the teach pendant. Press Enter to close it...")

    # Close the popup
    close_resp = robot.dashboard.close_popup()
    print(f"Close popup: {close_resp}")

    # Add a message to the robot log
    robot.dashboard.add_to_log(f"[Python SDK] Popup shown: {message}")
    print("Message added to robot log.")

finally:
    robot.disconnect()
    print("\nDisconnected.")


