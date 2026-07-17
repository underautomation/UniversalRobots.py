"""
Kinematics - Forward & Inverse Kinematics (offline)
======================================================
Compute forward kinematics (FK) from joint angles and inverse
kinematics (IK) from a Cartesian TCP pose, entirely offline:
no robot connection or license required.

Steps:
  1. Select a UR robot model from the built-in catalogue
  2. Enter joint angles in degrees  →  compute FK  →  get TCP pose
  3. Optionally adjust the TCP pose  →  compute IK  →  get all joint solutions

The library uses the analytical method described in Chen et al., IEEE ICASI 2017.
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from underautomation.universal_robots.kinematics.kinematics_utils import KinematicsUtils
from underautomation.universal_robots.common.robot_models_extended import RobotModelsExtended
from underautomation.universal_robots.common.pose import Pose

print("=" * 60)
print("  UR SDK - Kinematics: Forward & Inverse (offline)")
print("=" * 60)
print()

# ─── 1. Select robot model ────────────────────────────────────────────────────
models = [(m.name, m) for m in RobotModelsExtended]
print("Available robot models:")
for i, (name, _) in enumerate(models, 1):
    print(f"  {i:>3}. {name}")
print()

choice_str = input(f"Select model [1-{len(models)}, default=1 (UR3e)]: ").strip()
try:
    choice = int(choice_str) - 1
    if not (0 <= choice < len(models)):
        choice = 0
except ValueError:
    choice = 0

model_name, model_enum = models[choice]
print(f"\nSelected: {model_name}")

# Get DH parameters for the selected model
dh = KinematicsUtils.get_dh_parameters_from_model(model_enum)

# ─── 2. Forward Kinematics ────────────────────────────────────────────────────
print("\n" + "=" * 40)
print("  FORWARD KINEMATICS")
print("=" * 40)
print("Enter 6 joint angles in degrees (press Enter for default = all zeros):")

default_angles_deg = [90.0, -90.0, 90.0, 90.0, 90.0, 0.0]
joint_angles_rad = []

for i in range(6):
    default = default_angles_deg[i]
    raw = input(f"  J{i+1} (deg) [{default}]: ").strip()
    try:
        deg = float(raw) if raw else default
    except ValueError:
        deg = default
    joint_angles_rad.append(math.radians(deg))

# Compute FK
result = KinematicsUtils.forward_kinematics(joint_angles_rad, dh)

# The FK result contains the 4x4 homogeneous tool transform as a .NET double[4,4] matrix.
# Use 2D indexing T[row, col] — do NOT use flat indexing like T[3].
T = result.tool_transform

if T is not None:
    # Pass the .NET double[4,4] matrix directly — the method expects double[,]
    tcp = Pose.from4x4_matrix_to_rotation_vector(T)

    print(f"\nTCP pose (rotation vector):")
    print(f"  x  = {tcp.x*1000:.2f} mm")
    print(f"  y  = {tcp.y*1000:.2f} mm")
    print(f"  z  = {tcp.z*1000:.2f} mm")
    print(f"  rx = {math.degrees(tcp.rx):.4f} deg  ({tcp.rx:.6f} rad)")
    print(f"  ry = {math.degrees(tcp.ry):.4f} deg  ({tcp.ry:.6f} rad)")
    print(f"  rz = {math.degrees(tcp.rz):.4f} deg  ({tcp.rz:.6f} rad)")
else:
    print("FK computation failed.")

# ─── 3. Inverse Kinematics ────────────────────────────────────────────────────
if T is not None:
    print("\n" + "=" * 40)
    print("  INVERSE KINEMATICS")
    print("=" * 40)
    print("Computing IK from the FK result (all solutions)...")

    solutions = KinematicsUtils.inverse_kinematics(T, dh)

    if solutions is not None:
        # solutions is a .NET array of arrays: each element is a 6-joint solution
        sol_list = list(solutions)
        print(f"Found {len(sol_list)} IK solution(s):\n")
        for i, sol in enumerate(sol_list, 1):
            sol_deg = [round(math.degrees(v), 3) for v in sol]
            print(f"  Solution {i}: {sol_deg} deg")

        # Pick the nearest solution to the original joint angles
        nearest = KinematicsUtils.get_nearest_solution(solutions, joint_angles_rad)
        if nearest is not None:
            nearest_deg = [round(math.degrees(v), 3) for v in list(nearest)]
            print(f"\nNearest solution to input: {nearest_deg} deg")
    else:
        print("No IK solutions found.")


