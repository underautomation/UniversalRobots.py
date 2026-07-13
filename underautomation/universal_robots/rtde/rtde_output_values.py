from __future__ import annotations
import typing
from underautomation.universal_robots.rtde.rtde_output_setup_item import RtdeOutputSetupItem
from underautomation.universal_robots.common.joints_double_values import JointsDoubleValues
from underautomation.universal_robots.common.pose import Pose
from underautomation.universal_robots.common.cartesian_coordinates import CartesianCoordinates
from underautomation.universal_robots.common.joints_int_values import JointsIntValues
from underautomation.universal_robots.common.vector3_d import Vector3D
from underautomation.universal_robots.rtde.rtde_bit_registers_value import RtdeBitRegistersValue
from underautomation.universal_robots.rtde.rtde_int_registers_value import RtdeIntRegistersValue
from underautomation.universal_robots.rtde.rtde_double_registers_value import RtdeDoubleRegistersValue
from underautomation.universal_robots.rtde.rtde_base_values_1 import RtdeBaseValues1
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from UnderAutomation.UniversalRobots.Rtde import RtdeOutputValues as rtde_output_values
from UnderAutomation.UniversalRobots.Rtde import RtdeOutputData as rtde_output_data

class RtdeOutputValues(RtdeBaseValues1[RtdeOutputData]):
	'''Holds the current values for all RTDE output variables (robot-to-client). Updated automatically when data is received from the robot.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rtde_output_values()
		else:
			self._instance = _internal

	def get_value(self, item: RtdeOutputSetupItem) -> typing.Any:
		'''Gets the current value for the output variable described by a setup item.

		:param item: The output setup item identifying the variable and register index.
		:returns: The current value.
		'''
		return self._instance.GetValue(item._instance if item else None)

	@property
	def timestamp(self) -> float:
		'''Time elapsed since the controller was started [s]'''
		return self._instance.Timestamp

	@timestamp.setter
	def timestamp(self, value: float):
		self._instance.Timestamp = value

	@property
	def target_q(self) -> JointsDoubleValues:
		'''Target joint positions'''
		return JointsDoubleValues(self._instance.TargetQ)

	@target_q.setter
	def target_q(self, value: JointsDoubleValues):
		self._instance.TargetQ = value._instance if value else None

	@property
	def target_qd(self) -> JointsDoubleValues:
		'''Target joint velocities'''
		return JointsDoubleValues(self._instance.TargetQd)

	@target_qd.setter
	def target_qd(self, value: JointsDoubleValues):
		self._instance.TargetQd = value._instance if value else None

	@property
	def target_qdd(self) -> JointsDoubleValues:
		'''Target joint accelerations'''
		return JointsDoubleValues(self._instance.TargetQdd)

	@target_qdd.setter
	def target_qdd(self, value: JointsDoubleValues):
		self._instance.TargetQdd = value._instance if value else None

	@property
	def target_current(self) -> JointsDoubleValues:
		'''Target joint currents'''
		return JointsDoubleValues(self._instance.TargetCurrent)

	@target_current.setter
	def target_current(self, value: JointsDoubleValues):
		self._instance.TargetCurrent = value._instance if value else None

	@property
	def target_moment(self) -> JointsDoubleValues:
		'''Target joint moments (torques)'''
		return JointsDoubleValues(self._instance.TargetMoment)

	@target_moment.setter
	def target_moment(self, value: JointsDoubleValues):
		self._instance.TargetMoment = value._instance if value else None

	@property
	def actual_q(self) -> JointsDoubleValues:
		'''Actual joint positions'''
		return JointsDoubleValues(self._instance.ActualQ)

	@actual_q.setter
	def actual_q(self, value: JointsDoubleValues):
		self._instance.ActualQ = value._instance if value else None

	@property
	def actual_qd(self) -> JointsDoubleValues:
		'''Actual joint velocities'''
		return JointsDoubleValues(self._instance.ActualQd)

	@actual_qd.setter
	def actual_qd(self, value: JointsDoubleValues):
		self._instance.ActualQd = value._instance if value else None

	@property
	def actual_current(self) -> JointsDoubleValues:
		'''Actual joint currents'''
		return JointsDoubleValues(self._instance.ActualCurrent)

	@actual_current.setter
	def actual_current(self, value: JointsDoubleValues):
		self._instance.ActualCurrent = value._instance if value else None

	@property
	def joint_control_output(self) -> JointsDoubleValues:
		'''Joint control currents'''
		return JointsDoubleValues(self._instance.JointControlOutput)

	@joint_control_output.setter
	def joint_control_output(self, value: JointsDoubleValues):
		self._instance.JointControlOutput = value._instance if value else None

	@property
	def actual_tcp_pose(self) -> Pose:
		'''Actual Cartesian coordinates of the tool: (x,y,z,rx,ry,rz), where rx, ry and rz is a rotation vector representation of the tool orientation'''
		return Pose(None, None, None, None, None, None, self._instance.ActualTcpPose)

	@actual_tcp_pose.setter
	def actual_tcp_pose(self, value: Pose):
		self._instance.ActualTcpPose = value._instance if value else None

	@property
	def actual_tcp_speed(self) -> Pose:
		'''Actual speed of the tool given in Cartesian coordinates. The speed is given in [m/s] and the rotational part of the TCP speed (rx, ry, rz) is the angular velocity given in [rad/s]'''
		return Pose(None, None, None, None, None, None, self._instance.ActualTcpSpeed)

	@actual_tcp_speed.setter
	def actual_tcp_speed(self, value: Pose):
		self._instance.ActualTcpSpeed = value._instance if value else None

	@property
	def actual_tcp_force(self) -> CartesianCoordinates:
		'''Generalized forces in the TCP. It compensates the measurement for forces and torques generated by the payload'''
		return CartesianCoordinates(None, None, None, None, None, None, self._instance.ActualTcpForce)

	@actual_tcp_force.setter
	def actual_tcp_force(self, value: CartesianCoordinates):
		self._instance.ActualTcpForce = value._instance if value else None

	@property
	def target_tcp_pose(self) -> Pose:
		'''Target Cartesian coordinates of the tool: (x,y,z,rx,ry,rz), where rx, ry and rz is a rotation vector representation of the tool orientation'''
		return Pose(None, None, None, None, None, None, self._instance.TargetTcpPose)

	@target_tcp_pose.setter
	def target_tcp_pose(self, value: Pose):
		self._instance.TargetTcpPose = value._instance if value else None

	@property
	def target_tcp_speed(self) -> Pose:
		'''Target speed of the tool given in Cartesian coordinates. The speed is given in [m/s] and the rotational part of the TCP speed (rx, ry, rz) is the angular velocity given in [rad/s]'''
		return Pose(None, None, None, None, None, None, self._instance.TargetTcpSpeed)

	@target_tcp_speed.setter
	def target_tcp_speed(self, value: Pose):
		self._instance.TargetTcpSpeed = value._instance if value else None

	@property
	def actual_digital_input_bits(self) -> int:
		'''Current state of the digital inputs. 0-7: Standard, 8-15: Configurable, 16-17: Tool'''
		return self._instance.ActualDigitalInputBits

	@actual_digital_input_bits.setter
	def actual_digital_input_bits(self, value: int):
		self._instance.ActualDigitalInputBits = value

	@property
	def joint_temperatures(self) -> JointsDoubleValues:
		'''Temperature of each joint in degrees Celsius'''
		return JointsDoubleValues(self._instance.JointTemperatures)

	@joint_temperatures.setter
	def joint_temperatures(self, value: JointsDoubleValues):
		self._instance.JointTemperatures = value._instance if value else None

	@property
	def actual_execution_time(self) -> float:
		'''Controller real-time thread execution time'''
		return self._instance.ActualExecutionTime

	@actual_execution_time.setter
	def actual_execution_time(self, value: float):
		self._instance.ActualExecutionTime = value

	@property
	def robot_mode(self) -> int:
		'''Robot mode'''
		return self._instance.RobotMode

	@robot_mode.setter
	def robot_mode(self, value: int):
		self._instance.RobotMode = value

	@property
	def joint_mode(self) -> JointsIntValues:
		'''Joint control modes'''
		return JointsIntValues(self._instance.JointMode)

	@joint_mode.setter
	def joint_mode(self, value: JointsIntValues):
		self._instance.JointMode = value._instance if value else None

	@property
	def safety_mode(self) -> int:
		'''Safety mode'''
		return self._instance.SafetyMode

	@safety_mode.setter
	def safety_mode(self, value: int):
		self._instance.SafetyMode = value

	@property
	def safety_status(self) -> int:
		'''Safety status'''
		return self._instance.SafetyStatus

	@safety_status.setter
	def safety_status(self, value: int):
		self._instance.SafetyStatus = value

	@property
	def actual_tool_accelerometer(self) -> Vector3D:
		'''Tool x, y and z accelerometer values'''
		return Vector3D(self._instance.ActualToolAccelerometer)

	@actual_tool_accelerometer.setter
	def actual_tool_accelerometer(self, value: Vector3D):
		self._instance.ActualToolAccelerometer = value._instance if value else None

	@property
	def speed_scaling(self) -> float:
		'''Speed scaling of the trajectory limiter'''
		return self._instance.SpeedScaling

	@speed_scaling.setter
	def speed_scaling(self, value: float):
		self._instance.SpeedScaling = value

	@property
	def target_speed_fraction(self) -> float:
		'''Target speed fraction'''
		return self._instance.TargetSpeedFraction

	@target_speed_fraction.setter
	def target_speed_fraction(self, value: float):
		self._instance.TargetSpeedFraction = value

	@property
	def actual_momentum(self) -> float:
		'''Norm of Cartesian linear momentum'''
		return self._instance.ActualMomentum

	@actual_momentum.setter
	def actual_momentum(self, value: float):
		self._instance.ActualMomentum = value

	@property
	def actual_main_voltage(self) -> float:
		'''Safety Control Board: Main voltage'''
		return self._instance.ActualMainVoltage

	@actual_main_voltage.setter
	def actual_main_voltage(self, value: float):
		self._instance.ActualMainVoltage = value

	@property
	def actual_robot_voltage(self) -> float:
		'''Safety Control Board: Robot voltage (48V)'''
		return self._instance.ActualRobotVoltage

	@actual_robot_voltage.setter
	def actual_robot_voltage(self, value: float):
		self._instance.ActualRobotVoltage = value

	@property
	def actual_robot_current(self) -> float:
		'''Safety Control Board: Robot current'''
		return self._instance.ActualRobotCurrent

	@actual_robot_current.setter
	def actual_robot_current(self, value: float):
		self._instance.ActualRobotCurrent = value

	@property
	def actual_joint_voltage(self) -> JointsDoubleValues:
		'''Actual joint voltages'''
		return JointsDoubleValues(self._instance.ActualJointVoltage)

	@actual_joint_voltage.setter
	def actual_joint_voltage(self, value: JointsDoubleValues):
		self._instance.ActualJointVoltage = value._instance if value else None

	@property
	def actual_digital_output_bits(self) -> int:
		'''Current state of the digital outputs. 0-7: Standard, 8-15: Configurable, 16-17: Tool'''
		return self._instance.ActualDigitalOutputBits

	@actual_digital_output_bits.setter
	def actual_digital_output_bits(self, value: int):
		self._instance.ActualDigitalOutputBits = value

	@property
	def runtime_state(self) -> int:
		'''Program state'''
		return self._instance.RuntimeState

	@runtime_state.setter
	def runtime_state(self, value: int):
		self._instance.RuntimeState = value

	@property
	def elbow_position(self) -> Vector3D:
		'''Position of robot elbow in Cartesian Base Coordinates'''
		return Vector3D(self._instance.ElbowPosition)

	@elbow_position.setter
	def elbow_position(self, value: Vector3D):
		self._instance.ElbowPosition = value._instance if value else None

	@property
	def elbow_velocity(self) -> Vector3D:
		'''Velocity of robot elbow in Cartesian Base Coordinates'''
		return Vector3D(self._instance.ElbowVelocity)

	@elbow_velocity.setter
	def elbow_velocity(self, value: Vector3D):
		self._instance.ElbowVelocity = value._instance if value else None

	@property
	def robot_status_bits(self) -> int:
		'''Bits 0-3:Is power on | Is program running | Is teach button pressed | Is power button pressed'''
		return self._instance.RobotStatusBits

	@robot_status_bits.setter
	def robot_status_bits(self, value: int):
		self._instance.RobotStatusBits = value

	@property
	def safety_status_bits(self) -> int:
		'''Bits 0-10: Is normal mode | Is reduced mode | Is protective stopped | Is recovery mode | Is safeguard stopped | Is system emergency stopped | Is robot emergency stopped | Is emergency stopped | Is violation | Is fault | Is stopped due to safety'''
		return self._instance.SafetyStatusBits

	@safety_status_bits.setter
	def safety_status_bits(self, value: int):
		self._instance.SafetyStatusBits = value

	@property
	def analog_io_types(self) -> int:
		'''Bits 0-3: analog input 0 | analog input 1 | analog output 0 | analog output 1, {0=current[mA], 1=voltage[V]}'''
		return self._instance.AnalogIOTypes

	@analog_io_types.setter
	def analog_io_types(self, value: int):
		self._instance.AnalogIOTypes = value

	@property
	def standard_analog_input0(self) -> float:
		'''Standard analog input 0 [mA or V]'''
		return self._instance.StandardAnalogInput0

	@standard_analog_input0.setter
	def standard_analog_input0(self, value: float):
		self._instance.StandardAnalogInput0 = value

	@property
	def standard_analog_input1(self) -> float:
		'''Standard analog input 1 [mA or V]'''
		return self._instance.StandardAnalogInput1

	@standard_analog_input1.setter
	def standard_analog_input1(self, value: float):
		self._instance.StandardAnalogInput1 = value

	@property
	def standard_analog_output0(self) -> float:
		'''Standard analog output 0 [mA or V]'''
		return self._instance.StandardAnalogOutput0

	@standard_analog_output0.setter
	def standard_analog_output0(self, value: float):
		self._instance.StandardAnalogOutput0 = value

	@property
	def standard_analog_output1(self) -> float:
		'''Standard analog output 1 [mA or V]'''
		return self._instance.StandardAnalogOutput1

	@standard_analog_output1.setter
	def standard_analog_output1(self, value: float):
		self._instance.StandardAnalogOutput1 = value

	@property
	def io_current(self) -> float:
		'''I/O current [mA]'''
		return self._instance.IOCurrent

	@io_current.setter
	def io_current(self, value: float):
		self._instance.IOCurrent = value

	@property
	def euromap67_input_bits(self) -> int:
		'''Euromap67 input bits'''
		return self._instance.Euromap67InputBits

	@euromap67_input_bits.setter
	def euromap67_input_bits(self, value: int):
		self._instance.Euromap67InputBits = value

	@property
	def euromap67_output_bits(self) -> int:
		'''Euromap67 output bits'''
		return self._instance.Euromap67OutputBits

	@euromap67_output_bits.setter
	def euromap67_output_bits(self, value: int):
		self._instance.Euromap67OutputBits = value

	@property
	def euromap67_24_v_voltage(self) -> float:
		'''Euromap 24V voltage [V]'''
		return self._instance.Euromap67_24VVoltage

	@euromap67_24_v_voltage.setter
	def euromap67_24_v_voltage(self, value: float):
		self._instance.Euromap67_24VVoltage = value

	@property
	def euromap67_24_v_current(self) -> float:
		'''Euromap 24V current [mA]'''
		return self._instance.Euromap67_24VCurrent

	@euromap67_24_v_current.setter
	def euromap67_24_v_current(self, value: float):
		self._instance.Euromap67_24VCurrent = value

	@property
	def tool_mode(self) -> int:
		'''Tool mode'''
		return self._instance.ToolMode

	@tool_mode.setter
	def tool_mode(self, value: int):
		self._instance.ToolMode = value

	@property
	def tool_analog_input_types(self) -> int:
		'''Output domain {0=current[mA], 1=voltage[V]} Bits 0-1: tool_analog_input_0 | tool_analog_input_1'''
		return self._instance.ToolAnalogInputTypes

	@tool_analog_input_types.setter
	def tool_analog_input_types(self, value: int):
		self._instance.ToolAnalogInputTypes = value

	@property
	def tool_analog_input0(self) -> float:
		'''Tool analog input 0 [mA or V]'''
		return self._instance.ToolAnalogInput0

	@tool_analog_input0.setter
	def tool_analog_input0(self, value: float):
		self._instance.ToolAnalogInput0 = value

	@property
	def tool_analog_input1(self) -> float:
		'''Tool analog input 1 [mA or V]'''
		return self._instance.ToolAnalogInput1

	@tool_analog_input1.setter
	def tool_analog_input1(self, value: float):
		self._instance.ToolAnalogInput1 = value

	@property
	def tool_output_voltage(self) -> int:
		'''Tool output voltage [V]'''
		return self._instance.ToolOutputVoltage

	@tool_output_voltage.setter
	def tool_output_voltage(self, value: int):
		self._instance.ToolOutputVoltage = value

	@property
	def tool_output_current(self) -> float:
		'''Tool current [mA]'''
		return self._instance.ToolOutputCurrent

	@tool_output_current.setter
	def tool_output_current(self, value: float):
		self._instance.ToolOutputCurrent = value

	@property
	def tool_temperature(self) -> float:
		'''Tool temperature in degrees Celsius'''
		return self._instance.ToolTemperature

	@tool_temperature.setter
	def tool_temperature(self, value: float):
		self._instance.ToolTemperature = value

	@property
	def tcp_force_scalar(self) -> float:
		'''TCP force scalar [N]'''
		return self._instance.TcpForceScalar

	@tcp_force_scalar.setter
	def tcp_force_scalar(self, value: float):
		self._instance.TcpForceScalar = value

	@property
	def output_bit_registers0_to31(self) -> int:
		'''General purpose bits'''
		return self._instance.OutputBitRegisters0To31

	@output_bit_registers0_to31.setter
	def output_bit_registers0_to31(self, value: int):
		self._instance.OutputBitRegisters0To31 = value

	@property
	def output_bit_registers32_to63(self) -> int:
		'''General purpose bits'''
		return self._instance.OutputBitRegisters32To63

	@output_bit_registers32_to63.setter
	def output_bit_registers32_to63(self, value: int):
		self._instance.OutputBitRegisters32To63 = value

	@property
	def output_bit_registers(self) -> RtdeBitRegistersValue:
		'''64 general purpose bits. X: [64..127] - The upper range of the boolean output registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeBitRegistersValue(self._instance.OutputBitRegisters)

	@property
	def output_int_registers(self) -> RtdeIntRegistersValue:
		'''48 general purpose integer registers. X: [0..23] - The lower range of the integer output registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the integer output registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeIntRegistersValue(self._instance.OutputIntRegisters)

	@property
	def output_double_registers(self) -> RtdeDoubleRegistersValue:
		'''48 general purpose double registers. X: [0..23] - The lower range of the double output registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the double output registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeDoubleRegistersValue(self._instance.OutputDoubleRegisters)

	@property
	def input_bit_registers0_to31(self) -> int:
		'''General purpose bits (input read back). This range of the boolean output registers is reserved for FieldBus/PLC interface usage.'''
		return self._instance.InputBitRegisters0To31

	@input_bit_registers0_to31.setter
	def input_bit_registers0_to31(self, value: int):
		self._instance.InputBitRegisters0To31 = value

	@property
	def input_bit_registers32_to63(self) -> int:
		'''General purpose bits (input read back), This range of the boolean output registers is reserved for FieldBus/PLC interface usage.'''
		return self._instance.InputBitRegisters32To63

	@input_bit_registers32_to63.setter
	def input_bit_registers32_to63(self, value: int):
		self._instance.InputBitRegisters32To63 = value

	@property
	def input_bit_registers(self) -> RtdeBitRegistersValue:
		'''64 general purpose bits, X: [64..127] - The upper range of the boolean output registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeBitRegistersValue(self._instance.InputBitRegisters)

	@property
	def input_int_registers(self) -> RtdeIntRegistersValue:
		'''48 general purpose integer registers. X: [0..23] - The lower range of the integer input registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the integer input registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeIntRegistersValue(self._instance.InputIntRegisters)

	@property
	def input_double_registers(self) -> RtdeDoubleRegistersValue:
		'''48 general purpose double registers. X: [0..23] - The lower range of the double input registers is reserved for FieldBus/PLC interface usage. X: [24..47] - The upper range of the double input registers can be used by external RTDE clients (i.e URCAPS).'''
		return RtdeDoubleRegistersValue(self._instance.InputDoubleRegisters)

	@property
	def tool_output_mode(self) -> int:
		'''The current output mode'''
		return self._instance.ToolOutputMode

	@tool_output_mode.setter
	def tool_output_mode(self, value: int):
		self._instance.ToolOutputMode = value

	@property
	def tool_digital_output0mode(self) -> int:
		'''The current mode of digital output 0'''
		return self._instance.ToolDigitalOutput0mode

	@tool_digital_output0mode.setter
	def tool_digital_output0mode(self, value: int):
		self._instance.ToolDigitalOutput0mode = value

	@property
	def tool_digital_output1_mode(self) -> int:
		'''The current mode of digital output 1'''
		return self._instance.ToolDigitalOutput1Mode

	@tool_digital_output1_mode.setter
	def tool_digital_output1_mode(self, value: int):
		self._instance.ToolDigitalOutput1Mode = value

	@property
	def payload(self) -> float:
		'''Payload mass Kg'''
		return self._instance.Payload

	@payload.setter
	def payload(self, value: float):
		self._instance.Payload = value

	@property
	def payload_cog(self) -> Vector3D:
		'''Payload Center of Gravity (CoGx, CoGy, CoGz) m'''
		return Vector3D(self._instance.PayloadCOG)

	@payload_cog.setter
	def payload_cog(self, value: Vector3D):
		self._instance.PayloadCOG = value._instance if value else None

	@property
	def payload_inertia(self) -> CartesianCoordinates:
		'''Payload inertia matrix elements (Ixx,Iyy,Izz,Ixy,Ixz,Iyz] expressed in kg*m^2'''
		return CartesianCoordinates(None, None, None, None, None, None, self._instance.PayloadInertia)

	@payload_inertia.setter
	def payload_inertia(self, value: CartesianCoordinates):
		self._instance.PayloadInertia = value._instance if value else None

	@property
	def script_control_line(self) -> int:
		'''Script line number that is actually in control of the robot given the robot is locked by one of the threads in the script. If no thread is locking the robot this field is set to '0'. Script line number should not be confused with program tree line number displayed on polyscope.'''
		return self._instance.ScriptControlLine

	@script_control_line.setter
	def script_control_line(self, value: int):
		self._instance.ScriptControlLine = value

	@property
	def ft_raw_wrench(self) -> CartesianCoordinates:
		'''Raw force and torque measurement, not compensated for forces and torques caused by the payload'''
		return CartesianCoordinates(None, None, None, None, None, None, self._instance.FTRawWrench)

	@ft_raw_wrench.setter
	def ft_raw_wrench(self, value: CartesianCoordinates):
		self._instance.FTRawWrench = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RtdeOutputValues):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
