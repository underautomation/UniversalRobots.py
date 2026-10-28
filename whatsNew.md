## Same code for PolyScope and PolyScope X

The new interface `IRobotDashboard` of the .NET library contains the commands that exist on the Dashboard Server client (PolyScope 5, CB3 and e-Series) and on the REST API client (PolyScope X): power, brakes, protective stop, safety restart, programs, robot mode, safety mode, operational mode, remote control, popups and PolyScope version. In Python, `robot.dashboard` and `robot.rest` now have these methods with the same names, so one function controls both families. The only difference: the brakes are released with `release_brake()` on `robot.dashboard` and with `brake_release()` on `robot.rest`.

Each method returns an answer with `succeed`, `message` and, for the methods that read a value, `value`.

```python
client = robot.rest if is_polyscope_x else robot.dashboard

client.power_on()
client.load_program("my_program")
client.play()

safety = client.get_safety_mode()
print(safety.value)
```

## REST API: robot state, popups and program files

The REST API client of PolyScope X has new methods:

- Robot state: `get_loaded_program`, `get_robot_mode`, `get_safety_mode`, `get_operational_mode`, `is_in_remote_control`, `get_polyscope_version` and `get_robot_api_version`.
- Popups: `show_popup`, `show_popup_with_title`, `close_popup` and `close_safety_popup`.
- Program files: `get_programs` returns a list of `RestProgramInfo` (name, description, state, creation, modification and save dates). `upload_program_file` and `upload_program_content` add a new program, `update_program_file` and `update_program_content` replace an existing program, `download_program` and `download_program_to_file` read a program.

```python
mode = robot.rest.get_robot_mode()
safety = robot.rest.get_safety_mode()

robot.rest.show_popup_with_title("Cell 3", "Load the parts")

for program in robot.rest.get_programs().value:
    print(program.name)

robot.rest.upload_program_file(r"C:\programs\pick_and_place.urpx")
robot.rest.download_program_to_file("pick_and_place", r"C:\backup\pick_and_place.urpx")
```

## Dashboard Server: safety mode, user role, resume and diagnostics

New methods of the Dashboard Server client:

- `get_safety_mode` returns a `SafetyModes` value.
- `get_user_role` returns the `UserRoles` value set with `set_user_role`.
- `resume` resumes a paused program. Only PolyScope X knows this command: on PolyScope 5, use `play`.
- `save_log` saves the log of the robot to its log history file.
- `generate_flight_report(FlightReportTypes)` generates a flight report and returns its identifier. The SDK waits up to 3 minutes for the answer.
- `generate_support_file(directory)` generates a support file in a directory of the robot and returns its name. The SDK waits up to 10 minutes for the answer.

```python
from underautomation.universal_robots.dashboard.flight_report_types import FlightReportTypes

safety = robot.dashboard.get_safety_mode()
report = robot.dashboard.generate_flight_report(FlightReportTypes.System)
print(f"Flight report {report.value}")
```

## Safety modes

The new enum `SafetyModes` lists the 21 safety modes of the robot, with `Unknown` for a value that the SDK does not know. `masterboard_data` of the Primary Interface has 3 new properties: `safety_mode_value`, `is_protective_stopped` (protective, safeguard or enabling device stop) and `safety_mode_allows_execution` (`Normal` or `Reduced`).

The new class `UrEnumHelper` converts the numbers sent by a robot to the enums of the SDK (`robot_model_from_value`, `robot_mode_from_value`, `safety_mode_from_value`, `robot_series_from_value`, `control_box_type_from_value`, `tool_flange_type_from_value`). An unknown number never raises an error: the result is the `Unknown` value of the enum. `robot_series_from_model` finds the series of a robot from its model and its software version.

```python
masterboard = robot.primary_interface.masterboard_data
if masterboard.is_protective_stopped:
    robot.dashboard.unlock_protective_stop()
```

## RTDE: software version, control box and tool flange

At connection, the RTDE client reads 3 properties of the controller: `software_version` (for example "5.26.3"), `control_box_type` (`CB5` or `CB7`) and `tool_flange_type` (`V1` or `V2`). They need PolyScope 5.26.3 or later, or PolyScope X 10.15 or later. With an older controller, `software_version` is `None` and the 2 others are `Unknown`. The connection is not changed if the controller does not give them.

```python
robot.connect(params)
print(robot.rtde.software_version, robot.rtde.control_box_type, robot.rtde.tool_flange_type)
```

## UR15 and G Series

`RobotModels` has 4 new values: `UR15`, `UR10G1750`, `UR17G1300` and `UR18G950`. `get_robot_model` of the Dashboard Server now recognizes the UR15. `RobotModels` and `RobotModes` have a new `Unknown` value. The new enum `RobotSeries` gives the series of a robot: `CB3`, `ESeries`, `URSeries` or `GSeries`.

The G Series models are not in `RobotModelsExtended`: their factory kinematic parameters are not published yet, so the kinematics of the SDK does not compute them.

## REST API fixes

- An answer of the robot with a 2xx status other than 200 is now a success. Before, `succeed` was false.
- Program names and texts that contain quotes, backslashes or line breaks are now sent correctly, and the texts of the answers are decoded correctly.

## Package information

The PyPI page links to the release notes and to the issues of `UniversalRobots.py`. The `tests` folder of the repository is no longer installed with the package. The package also contains `THIRD-PARTY-NOTICES.txt`, the notices of the third-party code included in the library.

## Python types and None

The package contains a `py.typed` file, so Pylance, mypy and pyright read its type annotations. When the .NET library returns null for an SDK object, Python now gets `None`. Before, it got an empty object: `str()` gave an empty string and reading a value raised `AttributeError`.
