from __future__ import annotations
import typing
from underautomation.universal_robots.kinematics.kinematics_result import KinematicsResult
from underautomation.universal_robots.common.i_ur_dh_parameters import IUrDhParameters
from underautomation.universal_robots.kinematics.singularity_type import SingularityType
from underautomation.universal_robots.common.robot_models_extended import RobotModelsExtended
from UnderAutomation.UniversalRobots.Kinematics import KinematicsUtils as kinematics_utils
from UnderAutomation.UniversalRobots.Kinematics import SingularityType as singularity_type
from UnderAutomation.UniversalRobots.Common import RobotModelsExtended as robot_models_extended

class KinematicsUtils:
	'''========================================================================================================= Implementation notes : --------------------------------------------------------------------------------------------------------- This class implements forward and inverse kinematics for a 6-DOF serial cobot using the analytical method described in Chen et al., IEEE ICASI 2017 ("A general analytical algorithm for collaborative robot (cobot) with 6 DOF"). The DH convention and the closed-form inverse steps follow the paper's derivations. References (equation numbers below refer to the paper): - DH homogeneous transform (Eq. (1.1)). - Forward kinematics chain product T_0^6 = Π_i T_{i-1}^i (Eq. (1.2)). - Inverse kinematics main steps: q1 from Eq. (1.12) ; q5 from Eq. (1.15) ; q6 from Eq. (1.17) ; q234 from Eq. (1.20) ; q2 from Eq. (1.25) ; q3 and q4 from Eq. (1.27). Singularity check equation used (paper text): det(J) ∝ s3 * s5 * a2 * a3 * (c2*a2 + c23*a3 + s234*d5) Paper: Chen, S., Luo, M., Abdelaziz, O., Jiang, G. "A General Analytical Algorithm for Collaborative Robot (cobot) with 6 DOF", IEEE ICASI 2017. ========================================================================================================='''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kinematics_utils()
		else:
			self._instance = _internal

	@staticmethod
	def dh_transform(theta: float, d: float, a: float, alpha: float) -> typing.List[float]:
		'''Computes the 4×4 Denavit-Hartenberg homogeneous transformation matrix for one joint.

		:param theta: Joint angle in radians.
		:param d: Link offset along the previous z-axis, in meters.
		:param a: Link length along the rotated x-axis, in meters.
		:param alpha: Link twist angle in radians.
		:returns: A 4×4 homogeneous transformation matrix.
		'''
		return kinematics_utils.DHTransform(theta, d, a, alpha)

	@staticmethod
	def homogeneous_multiply(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
		return kinematics_utils.HomogeneousMultiply(A, B)

	@staticmethod
	def forward_kinematics(jointAnglesRad: typing.List[float], dhParameters: IUrDhParameters) -> KinematicsResult:
		'''Forward kinematics : compute tool transform and intermediate transforms from joint angles (radians) and DH parameters.

		:param jointAnglesRad: Array of 6 joint angles in radians.
		:param dhParameters: Robot DH parameters.
		:returns: Tool transform and intermediate transforms.
		'''
		return KinematicsResult(kinematics_utils.ForwardKinematics(jointAnglesRad, dhParameters._instance if dhParameters else None))

	@staticmethod
	def get_nearest_solution(jointSolutions: typing.List[float], jointReference: typing.List[float]) -> typing.List[float]:
		'''Pick the solution nearest to a reference joint vector (L1 distance). Null if invalid inputs.

		:param jointSolutions: Array of candidate joint angles (6 elements each).
		:param jointReference: Reference joint angles (6 elements).
		:returns: Nearest joint angles (6 elements) or null.
		'''
		return kinematics_utils.GetNearestSolution(jointSolutions, jointReference)

	@staticmethod
	def inverse_kinematics(toolTransform: typing.List[float], dhParameters: IUrDhParameters) -> typing.List[float]:
		return kinematics_utils.InverseKinematics(toolTransform, dhParameters._instance if dhParameters else None)

	@staticmethod
	def get_singularity(elbow: float, shoulder: float, wrist1: float, wrist2: float, dhParameters: IUrDhParameters) -> SingularityType:
		'''Detects singularities using Jacobian determinant factors: sin(q5)≈0 (wrist), sin(q3)≈0 (elbow), and c2·a2 + c23·a3 + s234·d5 ≈ 0 (shoulder).

		:param elbow: Joint angle q2 in radians (shoulder joint in UR convention).
		:param shoulder: Joint angle q3 in radians (elbow joint in UR convention).
		:param wrist1: Joint angle q4 in radians (wrist 1).
		:param wrist2: Joint angle q5 in radians (wrist 2).
		:param dhParameters: Robot DH parameters.
		:returns: Flags indicating which singularities, if any, are present.
		'''
		return SingularityType(int(kinematics_utils.GetSingularity(elbow, shoulder, wrist1, wrist2, dhParameters._instance if dhParameters else None)))

	@staticmethod
	def get_dh_parameters_from_model(model: RobotModelsExtended) -> IUrDhParameters:
		'''Returns the factory Denavit-Hartenberg parameters for a given UR robot model.

		:param model: UR robot model identifier.
		:returns: DH parameters for the specified model.
		'''
		return IUrDhParameters(kinematics_utils.GetDhParametersFromModel(robot_models_extended(int(model))))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KinematicsUtils):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
