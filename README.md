# Universal Robots Communication SDK for Python

[![UnderAutomation Universal Robots SDK](https://user-images.githubusercontent.com/47540360/136141853-1ec87530-d88e-467f-adb4-ec3c46d26010.png)](https://underautomation.com/universal-robots)

[![PyPI](https://img.shields.io/pypi/v/UnderAutomation.UniversalRobots?label=PyPI&logo=pypi)](https://pypi.org/project/UnderAutomation.UniversalRobots/)
[![PyPI downloads](https://img.shields.io/pypi/dm/UnderAutomation.UniversalRobots?label=Downloads&logo=pypi)](https://pypi.org/project/UnderAutomation.UniversalRobots/)
[![Python](https://img.shields.io/badge/Python-3.7_to_3.13-blue)](#compatibility)
[![Platforms](https://img.shields.io/badge/OS-Windows_Linux_macOS-informational)](#compatibility)
[![License](https://img.shields.io/badge/license-commercial-blue)](https://underautomation.com/universal-robots/eula)

**UnderAutomation.UniversalRobots** is a Python package that communicates with Universal Robots cobots
(CB-Series, e-Series and the newer models, PolyScope and PolyScope X) through the standard interfaces of
the controller: RTDE, Dashboard Server, REST API, Primary Interface, SFTP, sockets and XML-RPC. It also
computes the forward and inverse kinematics offline. No URCap and no option is needed on the robot.

It works with real robots and with the URSim simulator.

- Product page: [underautomation.com/universal-robots](https://underautomation.com/universal-robots)
- Documentation: [underautomation.com/universal-robots/documentation/get-started-python](https://underautomation.com/universal-robots/documentation/get-started-python)
- Also available for [.NET](https://github.com/underautomation/UniversalRobots.NET), [LabVIEW](https://github.com/underautomation/UniversalRobots.vi) and [Unity](https://github.com/underautomation/UniversalRobots.Unity)

## What you can do

- **RTDE:** read the robot data at up to 500 Hz (TCP pose, joint angles, forces, I/O, registers) and write
  inputs and registers.
- **Dashboard Server** (PolyScope): load, play and stop programs, power on and off, release the brakes,
  read the robot mode.
- **REST API** (PolyScope X): control the robot state and the programs over HTTP.
- **Primary Interface:** receive the data packets of the robot and send URScript commands.
- **SFTP:** list, download and upload programs and files over SSH.
- **Kinematics:** offline forward and inverse kinematics for every UR model, without connection.
- **Socket communication:** exchange messages between Python and a URScript program.
- **License:** trial, registration and state of the license.

## How it works

The package wraps the .NET library `UnderAutomation.UniversalRobots.dll` with
[pythonnet](https://github.com/pythonnet/pythonnet). The DLL is inside the package: `pip install` installs
everything, including pythonnet.

- **Windows:** the DLL runs on the .NET Framework 4.x of Windows. Nothing else to install.
- **Linux and macOS:** install the .NET runtime (for example .NET 8), then tell pythonnet to use it before
  you start Python:

  ```bash
  # Debian and Ubuntu, for example
  sudo apt-get install -y dotnet-runtime-8.0
  export PYTHONNET_RUNTIME=coreclr
  ```

  Without this variable, pythonnet uses Mono, its default runtime on Linux and macOS. You can also choose
  the runtime in your code, before the first import of the package:

  ```python
  from pythonnet import load
  load("coreclr")
  ```

## Installation

Python 3.7 to 3.13 is supported (the limit of pythonnet 3.0.5). Install the package in a virtual
environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux and macOS
source .venv/bin/activate

pip install UnderAutomation.UniversalRobots
```

Or install it from the sources of this repository:

```bash
git clone https://github.com/underautomation/UniversalRobots.py.git
cd UniversalRobots.py
pip install -e .
```

## Getting started

```python
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData

# The SDK runs in trial mode for 30 days. Register your key to remove the trial limit.
# UR.register_license("Your Company", "your-license-key")

robot = UR()

params = ConnectParameters("192.168.0.1")

# Dashboard Server: load, play and stop programs, robot state
params.dashboard.enable = True

# Primary Interface: data packets, URScript
params.primary_interface.enable = True

# RTDE: robot data at up to 500 Hz
params.rtde.enable = True
params.rtde.frequency = 10
params.rtde.output_setup.add(RtdeOutputData.ActualTcpPose)
params.rtde.output_setup.add(RtdeOutputData.ActualQ)
params.rtde.input_setup.add(RtdeInputData.InputIntRegisters, 24)

# SFTP file transfer over SSH
params.ssh.enable = True
params.ssh.enable_sftp = True
params.ssh.username = "ur"
params.ssh.password = "easybot"

robot.connect(params)

# Read the TCP pose with RTDE
@robot.rtde.output_data_received
def on_rtde(sender, event):
    pose = robot.rtde.output_data_values.actual_tcp_pose
    print(f"TCP: x={pose[0]:.3f}  y={pose[1]:.3f}  z={pose[2]:.3f}")

# Send a URScript command
robot.primary_interface.script.send('popup("Hello from Python!", blocking=False)')

# Dashboard: load and start a program
robot.dashboard.load_program("my_program.urp")
robot.dashboard.play()

# SFTP: list the programs of the controller
for program in robot.sftp.enumerate_programs():
    print(program)

robot.disconnect()
```

## From .NET names to Python names

The Python API is the .NET API with Python names. The
[.NET documentation](https://underautomation.com/universal-robots/documentation) applies to Python.

| .NET | Python |
| --- | --- |
| Method `robot.Dashboard.LoadProgram("my_program.urp")` | `robot.dashboard.load_program("my_program.urp")` |
| Property `parameters.Rtde.Frequency` | `params.rtde.frequency` |
| Static method `UR.RegisterLicense(...)` | `UR.register_license(...)` |
| Enum value `RtdeOutputData.ActualTcpPose` | `RtdeOutputData.ActualTcpPose` |
| Event `robot.Rtde.OutputDataReceived` | decorator `@robot.rtde.output_data_received` |
| Array `double[]` | list-like object, use `list(...)` to copy it |

Each type is in the module named after it, in snake case:
`UnderAutomation.UniversalRobots.Rtde.RtdeOutputData` is
`underautomation.universal_robots.rtde.rtde_output_data.RtdeOutputData`.

## Examples

The folder [`examples`](examples) contains scripts ready to run, one folder per interface.

| File | Role |
| --- | --- |
| [`examples/launcher.py`](examples/launcher.py) | Menu to browse and run every example |
| [`examples/__init__.py`](examples/__init__.py) | Shared helpers: robot address, SSH credentials, license |
| `examples/robot_config.json` | Saved settings (ignored by git): robot address, credentials and license key |

The first run asks the address of the robot and saves it. Run a script from the root of the repository, or
open the launcher:

```bash
python examples/dashboard/dashboard_get_robot_state.py
python examples/launcher.py
```

### Dashboard Server, PolyScope (port 29999)

| Script | What it does |
| --- | --- |
| [dashboard_get_robot_state.py](examples/dashboard/dashboard_get_robot_state.py) | Reads the robot mode, the loaded program, the program state and the PolyScope version |
| [dashboard_load_play_program.py](examples/dashboard/dashboard_load_play_program.py) | Loads a .urp program and starts it |
| [dashboard_power_on_release_brakes.py](examples/dashboard/dashboard_power_on_release_brakes.py) | Powers on the arm and releases the brakes |
| [dashboard_popup_message.py](examples/dashboard/dashboard_popup_message.py) | Shows a popup on the teach pendant, then closes it |

### REST API, PolyScope X (port 80)

| Script | What it does |
| --- | --- |
| [rest_get_robot_state.py](examples/rest/rest_get_robot_state.py) | Reads the robot state and the program state |
| [rest_load_play_program.py](examples/rest/rest_load_play_program.py) | Loads and starts a program |
| [rest_power_on_brake_release.py](examples/rest/rest_power_on_brake_release.py) | Powers on the robot and releases the brakes |

### RTDE (port 30004)

| Script | What it does |
| --- | --- |
| [rtde_read_tcp_pose.py](examples/rtde/rtde_read_tcp_pose.py) | Reads the TCP pose (x, y, z, rx, ry, rz) and the joint angles |
| [rtde_read_digital_io.py](examples/rtde/rtde_read_digital_io.py) | Reads the digital inputs and outputs and shows their changes |
| [rtde_read_write_registers.py](examples/rtde/rtde_read_write_registers.py) | Reads output integer registers and writes input integer registers |

### SFTP (port 22)

| Script | What it does |
| --- | --- |
| [sftp_list_programs.py](examples/sftp/sftp_list_programs.py) | Lists the .urp programs and browses the file system of the robot |
| [sftp_download_program.py](examples/sftp/sftp_download_program.py) | Downloads a .urp program from the controller |
| [sftp_upload_program.py](examples/sftp/sftp_upload_program.py) | Uploads a local .urp program to the controller |

### Primary Interface (port 30001)

| Script | What it does |
| --- | --- |
| [primary_interface_read_telemetry.py](examples/primary_interface/primary_interface_read_telemetry.py) | Receives the robot mode, the joint data and the Cartesian data |
| [primary_interface_send_urscript.py](examples/primary_interface/primary_interface_send_urscript.py) | Sends URScript commands to the controller |
| [primary_interface_global_variables.py](examples/primary_interface/primary_interface_global_variables.py) | Reads the global variables of the loaded program |

### Kinematics (no connection)

| Script | What it does |
| --- | --- |
| [kinematics_forward_inverse.py](examples/kinematics/kinematics_forward_inverse.py) | Selects a UR model, computes the forward kinematics, then every inverse kinematics solution |

### License

| Script | What it does |
| --- | --- |
| [license_info_example.py](examples/license/license_info_example.py) | Shows the license state, registers a license and shows its properties |

## Interfaces

### RTDE

RTDE sends the robot data at up to 500 Hz on port 30004. You choose the outputs to read and the inputs to
write.

- Read any set of outputs: TCP pose, joint positions, forces, I/O, temperatures, voltages...
- Write inputs: digital and analog outputs, integer, double and boolean registers.
- Choose the frequency, from 1 to 500 Hz (RTDE version 2).
- Handle each new sample in the `output_data_received` event.

```python
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from underautomation.universal_robots.rtde.rtde_input_values import RtdeInputValues

robot = UR()
params = ConnectParameters("192.168.0.1")
params.rtde.enable = True
params.rtde.frequency = 125
params.rtde.output_setup.add(RtdeOutputData.ActualTcpPose)
params.rtde.output_setup.add(RtdeOutputData.ActualTcpForce)
params.rtde.output_setup.add(RtdeOutputData.ActualDigitalOutputBits)
params.rtde.input_setup.add(RtdeInputData.InputIntRegisters, 24)
robot.connect(params)

@robot.rtde.output_data_received
def on_data(sender, event):
    values = robot.rtde.output_data_values
    pose = values.actual_tcp_pose
    force = values.actual_tcp_force
    print(f"x={pose[0]:.3f}  Fx={force[0]:.2f} N")

    # Write to the robot
    inputs = RtdeInputValues()
    inputs.input_int_registers.x24 = 42
    robot.rtde.write_inputs(inputs)

robot.disconnect()
```

### Dashboard Server (PolyScope)

The Dashboard Server listens on port 29999. It controls the programs and the robot state, on CB-Series and
e-Series robots.

- Load, play, stop and pause programs.
- Power the arm on and off, release the brakes.
- Read the robot mode, the safety status and the PolyScope version.
- Show and close popups on the teach pendant.
- Set the operational mode (manual or automatic) for remote control.
- Add messages to the log of the controller.

```python
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters

robot = UR()
params = ConnectParameters("192.168.0.1")
params.dashboard.enable = True
robot.connect(params)

robot.dashboard.power_on()
robot.dashboard.release_brake()
robot.dashboard.load_program("my_program.urp")
robot.dashboard.play()

mode = robot.dashboard.get_robot_mode()
print(f"Robot mode: {mode.value}")

robot.disconnect()
```

### REST API (PolyScope X)

The REST API exists on PolyScope X robots. It controls the robot and the programs
over HTTP.

```python
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters

robot = UR()
params = ConnectParameters("192.168.0.1")
params.rest.enable = True
robot.connect(params)

robot.rest.power_on()
robot.rest.brake_release()
robot.rest.load_program("my_program")
robot.rest.play()
state = robot.rest.get_program_state()
print(state.value)

robot.disconnect()
```

### Primary Interface

The Primary Interface (port 30001) sends data packets about 10 times per second and accepts URScript
commands.

- Receive the robot mode, the joint data, the TCP position, the tool data, the safety data and more.
- Send URScript programs or commands, executed at once.
- Read the global variables of the loaded program.

```python
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters

robot = UR()
params = ConnectParameters("192.168.0.1")
params.primary_interface.enable = True
robot.connect(params)

@robot.primary_interface.cartesian_info_received
def on_cartesian(sender, event):
    c = robot.primary_interface.cartesian_info
    print(f"x={c.x:.3f}  y={c.y:.3f}  z={c.z:.3f}")

robot.primary_interface.script.send('set_digital_out(0, True)')
robot.disconnect()
```

### SFTP

SFTP gives access to the file system of the controller over SSH (port 22). The default user is `ur`, with
the password `easybot`.

- List, download and upload files.
- List the `.urp` programs and the `.installation` files.
- Create and delete folders.

```python
params.ssh.enable = True
params.ssh.enable_sftp = True
params.ssh.username = "ur"
params.ssh.password = "easybot"
robot.connect(params)

programs = robot.sftp.enumerate_programs()
robot.sftp.download_file("/programs/my_prog.urp", "C:/backup/my_prog.urp")
robot.sftp.upload_file("C:/new_prog.urp", "/programs/new_prog.urp")
```

### Kinematics

The SDK computes the forward and inverse kinematics offline, with the factory Denavit-Hartenberg
parameters of every UR model: UR3, UR5, UR10, UR3e, UR5e, UR7e, UR10e, UR12e, UR16e, UR8 Long, UR15,
UR18, UR20 and UR30. No connection and no license are needed.

```python
import math
from underautomation.universal_robots.kinematics.kinematics_utils import KinematicsUtils
from underautomation.universal_robots.common.robot_models_extended import RobotModelsExtended

dh = KinematicsUtils.get_dh_parameters_from_model(RobotModelsExtended.UR10e)

# Forward kinematics: joint angles to TCP pose
angles_rad = [math.radians(a) for a in [0, -90, 0, -90, 0, 0]]
result = KinematicsUtils.forward_kinematics(angles_rad, dh)
T = result.tool_transform  # 4x4 homogeneous matrix (flat list of 16 floats)

# Inverse kinematics: TCP pose to every joint solution
solutions = KinematicsUtils.inverse_kinematics(T, dh)
nearest = KinematicsUtils.get_nearest_solution(solutions, angles_rad)
print([math.degrees(v) for v in nearest])
```

## Compatibility

- **Python:** 3.7 to 3.13, with pythonnet 3.0.5.
- **Operating systems:** Windows (.NET Framework), Linux and macOS (.NET runtime and `export PYTHONNET_RUNTIME=coreclr`).
- **Robots:** CB-Series (CB3), e-Series and the newer models, PolyScope and PolyScope X, and URSim.

## License

This SDK needs a commercial license. A 30-day trial starts at the first use, no key needed. After the
trial, register your key in your code:

```python
from underautomation.universal_robots.ur import UR

license_info = UR.register_license("Your Company", "your-license-key")
print(license_info)
```

- License agreement: [underautomation.com/universal-robots/eula](https://underautomation.com/universal-robots/eula) and [License.md](License.md)
- New trial period by email: [underautomation.com/license](https://underautomation.com/license?sdk=universal-robots)
- Prices and order: [underautomation.com/order](https://underautomation.com/order?sdk=universal-robots)

## Support

- Documentation: [underautomation.com/universal-robots/documentation](https://underautomation.com/universal-robots/documentation)
- Issues: [GitHub Issues](https://github.com/underautomation/UniversalRobots.py/issues)
- Contact: [underautomation.com/contact](https://underautomation.com/contact)
