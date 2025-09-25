import typing
from underautomation.universal_robots.kinematics.kinematics_result import KinematicsResult
from underautomation.universal_robots.common.i_ur_dh_parameters import IUrDhParameters
from underautomation.universal_robots.kinematics.singularity_type import SingularityType
from underautomation.universal_robots.common.robot_models_extended import RobotModelsExtended
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.UniversalRobots.dll')))
from UnderAutomation.UniversalRobots.Kinematics import KinematicsUtils as kinematics_utils

class KinematicsUtils:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kinematics_utils()
		else:
			self._instance = _internal
	@staticmethod
	def dh_transform(theta: float, d: float, a: float, alpha: float) -> typing.List[float]:
		return kinematics_utils.DHTransform(theta, d, a, alpha)
	@staticmethod
	def homogeneous_multiply(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
		return kinematics_utils.HomogeneousMultiply(A, B)
	@staticmethod
	def forward_kinematics(jointAnglesRad: typing.List[float], dhParameters: IUrDhParameters) -> KinematicsResult:
		return KinematicsResult(kinematics_utils.ForwardKinematics(jointAnglesRad, dhParameters._instance))
	@staticmethod
	def get_nearest_solution(jointSolutions: typing.List[float], jointReference: typing.List[float]) -> typing.List[float]:
		return kinematics_utils.GetNearestSolution(jointSolutions, jointReference)
	@staticmethod
	def inverse_kinematics(toolTransform: typing.List[float], dhParameters: IUrDhParameters) -> typing.List[float]:
		return kinematics_utils.InverseKinematics(toolTransform, dhParameters._instance)
	@staticmethod
	def get_singularity(elbow: float, shoulder: float, wrist1: float, wrist2: float, dhParameters: IUrDhParameters) -> SingularityType:
		return SingularityType(kinematics_utils.GetSingularity(elbow, shoulder, wrist1, wrist2, dhParameters._instance))
	@staticmethod
	def get_dh_parameters_from_model(model: RobotModelsExtended) -> IUrDhParameters:
		return IUrDhParameters(kinematics_utils.GetDhParametersFromModel(model._instance))
