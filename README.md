# Universal Robots Communication SDK for Python

[![UnderAutomation Universal Robots SDK](https://user-images.githubusercontent.com/47540360/136141853-1ec87530-d88e-467f-adb4-ec3c46d26010.png)](https://underautomation.com/universal-robots)

[![PyPI](https://img.shields.io/badge/PyPI-UnderAutomation.UniversalRobots-blue?logo=pypi)](https://pypi.org/project/UnderAutomation.UniversalRobots)
[![Python](https://img.shields.io/badge/Python-3.7_|_3.8_|_3.9_|_3.10_|_3.11_|_3.12_|_3.13-blue?logo=python)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)](#)
[![License](https://img.shields.io/badge/License-Commercial-red)](https://underautomation.com/universal-robots/eula)

### 🤖 Effortlessly Communicate with Universal Robots Cobots

The **Universal Robots SDK for Python** enables seamless integration with UR cobots (CB-Series and e-Series) for automation, data exchange, and remote control through all native communication protocols.

> Whether you're building a custom MES/SCADA integration, a monitoring dashboard, or a test harness, this SDK provides a single Pythonic API for every UR interface.

It supports communication with **real robots** and **URSim** simulators.

🔗 **More Information:** [https://underautomation.com/universal-robots](https://underautomation.com/universal-robots)  
🔗 Also available in **[🟦 .NET](https://github.com/underautomation/UniversalRobots.NET)** & **[🟨 LabVIEW](https://github.com/underautomation/UniversalRobots.vi)** & **[🧊 Unity](https://github.com/underautomation/UniversalRobots.Unity)**

---

[⭐ Star this repo if it's useful to you!](https://github.com/underautomation/UniversalRobots.py/stargazers)  
[👁️ Watch for updates](https://github.com/underautomation/UniversalRobots.py/watchers)

---

## 🚀 TL;DR

- ⚡ **RTDE** – stream real-time robot data at up to 500 Hz (TCP pose, joint angles, forces, I/O, registers)
- 📋 **Dashboard Server** – load, play, stop programs; power on/off; robot mode (Polyscope Legacy)
- 🌐 **REST API** – full HTTP control of robot and program state (PolyscopeX only)
- 🔗 **Primary Interface** – subscribe to telemetry packets; send URScript commands
- 📂 **SFTP** – list, download and upload programs and files over SSH
- 🦾 **Kinematics** – offline forward & inverse kinematics for all UR models (no connection needed)
- 🔌 **Socket Communication** – bidirectional messaging between Python and URScript programs
- 🔑 **License management** – trial, registration, and status

> All protocols use **standard UR communication** : no custom robot options required.

---

## 🛠 Installation & Getting Started

### Prerequisites

- **Python 3.7** or higher
- A UR robot or **URSim** simulator

### Step 1 - Create a Virtual Environment

```bash
mkdir my-ur-project
cd my-ur-project

python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2 - Install the SDK

```bash
pip install UnderAutomation.UniversalRobots
```

All dependencies (including `pythonnet`) are installed automatically.

On **Linux**, also install .NET runtime and set the `PYTHONNET_RUNTIME` variable:

```bash
sudo apt-get install -y dotnet-runtime-8.0
export PYTHONNET_RUNTIME=coreclr
```

> **Alternative: install from source**
>
> ```bash
> git clone https://github.com/underautomation/UniversalRobots.py.git
> cd UniversalRobots.py
> pip install -e .
> ```

### Step 3 - Connect to Your Robot

```python
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from underautomation.universal_robots.rtde.rtde_input_values import RtdeInputValues

robot = UR()

# Configure protocols
params = ConnectParameters("192.168.0.1")

# Dashboard Server (load/play/stop programs, robot state)
params.dashboard.enable = True

# Primary Interface (telemetry packets, URScript)
params.primary_interface.enable = True

# RTDE (real-time data at up to 500 Hz)
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

# Connect (if you get a license exception, request a free trial at https://underautomation.com/license)
robot.connect(params)

# Read live TCP pose via RTDE
@robot.rtde.output_data_received
def on_rtde(sender, event):
    pose = robot.rtde.output_data_values.actual_tcp_pose
    print(f"TCP: x={pose[0]:.3f}  y={pose[1]:.3f}  z={pose[2]:.3f}")

# Send a URScript command
robot.primary_interface.script.send('popup("Hello from Python!", blocking=False)')

# Dashboard: load and start a program
robot.dashboard.load_program("my_program.urp")
robot.dashboard.play()

# SFTP: list programs on the controller
programs = robot.sftp.enumerate_programs()
for p in programs:
    print(p)

# Don't forget to disconnect
robot.disconnect()
```

---

## 🔑 Licensing

The SDK works out of the box for **30 days** (trial period) : no registration needed.

After the trial, you can:

- **Buy a license** at [underautomation.com/order](https://underautomation.com/order?sdk=universal-robots)
- **Get a new trial period immediately by email** at [underautomation.com/license](https://underautomation.com/license?sdk=universal-robots)

To register a license in code:

```python
from underautomation.universal_robots.ur import UR

license_info = UR.register_license("your-licensee", "your-license-key")
print(license_info)
```

---

## 📂 Examples

The repository includes a complete set of ready-to-run examples in the [`examples/`](examples/) folder, organized by communication protocol.

### How the Examples Work

| File                                           | Role                                                                                       |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [`examples/launcher.py`](examples/launcher.py) | **Interactive menu** : browse and run any example from a single launcher                   |
| [`examples/__init__.py`](examples/__init__.py) | **Shared helpers** : path setup, robot IP persistence, SSH credentials, license management |
| `examples/robot_config.json`                   | **Saved settings** (git-ignored) : remembers your robot IP, credentials, and license key   |

**Run an example directly:**

```bash
# First time: will ask for robot IP and save it
python examples/dashboard/dashboard_get_robot_state.py
```

**Or browse all examples with the interactive launcher:**

```bash
python examples/launcher.py
```

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║   ██╗   ██╗███╗   ██╗██╗██╗   ██╗███████╗██████╗ ███████╗ █████╗ ██╗          ║
║   ██║   ██║████╗  ██║██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║          ║
║   ...                                                                          ║
║                                                                                ║
║        Universal Robots Python SDK - Interactive Example Launcher              ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════════════╗
║                              SELECT A CATEGORY                                 ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  📋  1. DASHBOARD            (4 examples)                                      ║
║         Dashboard Server (Polyscope Legacy) - load/play/stop programs          ║
║                                                                                ║
║  🌐  2. REST                 (3 examples)                                      ║
║         REST API (PolyscopeX) - robot & program control via HTTP               ║
║                                                                                ║
║  ⚡  3. RTDE                 (3 examples)                                      ║
║         RTDE - real-time data streaming up to 500 Hz, I/O & registers          ║
║                                                                                ║
║  📂  4. SFTP                 (3 examples)                                      ║
║         SFTP - file transfer, list/download/upload programs                    ║
║                                                                                ║
║  🔗  5. PRIMARY_INTERFACE    (3 examples)                                      ║
║         Primary Interface - robot telemetry packets, send URScript             ║
║                                                                                ║
║  🦾  6. KINEMATICS           (1 example)                                       ║
║         Kinematics - offline forward & inverse kinematics                      ║
║                                                                                ║
║  🔑  7. LICENSE              (1 example)                                       ║
║         License management - activation & status                               ║
║                                                                                ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  0. Exit                                                                       ║
╚════════════════════════════════════════════════════════════════════════════════╝
```

---

### 📋 Complete Example List

#### 📋 Dashboard - Polyscope Legacy (port 29999)

| #   | Example                                                                                         | Description                                                           |
| --- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1   | [dashboard_get_robot_state.py](examples/dashboard/dashboard_get_robot_state.py)                 | Read robot mode, loaded program, program state, and Polyscope version |
| 2   | [dashboard_load_play_program.py](examples/dashboard/dashboard_load_play_program.py)             | Load a .urp program and start it remotely                             |
| 3   | [dashboard_power_on_release_brakes.py](examples/dashboard/dashboard_power_on_release_brakes.py) | Power on the robot arm and release brakes from Python                 |
| 4   | [dashboard_popup_message.py](examples/dashboard/dashboard_popup_message.py)                     | Show a popup on the teach pendant and close it programmatically       |

#### 🌐 REST API - PolyscopeX (port 80)

| #   | Example                                                                        | Description                                            |
| --- | ------------------------------------------------------------------------------ | ------------------------------------------------------ |
| 1   | [rest_get_robot_state.py](examples/rest/rest_get_robot_state.py)               | Read current robot state and program state via HTTP    |
| 2   | [rest_load_play_program.py](examples/rest/rest_load_play_program.py)           | Load and start a program via the REST API              |
| 3   | [rest_power_on_brake_release.py](examples/rest/rest_power_on_brake_release.py) | Power on the robot and release brakes via the REST API |

#### ⚡ RTDE - Real-Time Data Exchange (port 30004)

| #   | Example                                                                    | Description                                                     |
| --- | -------------------------------------------------------------------------- | --------------------------------------------------------------- |
| 1   | [rtde_read_tcp_pose.py](examples/rtde/rtde_read_tcp_pose.py)               | Stream TCP pose (x,y,z,rx,ry,rz) and joint angles in real time  |
| 2   | [rtde_read_digital_io.py](examples/rtde/rtde_read_digital_io.py)           | Monitor digital input and output states with change detection   |
| 3   | [rtde_read_write_registers.py](examples/rtde/rtde_read_write_registers.py) | Read output integer registers and write input integer registers |

#### 📂 SFTP - File Transfer over SSH (port 22)

| #   | Example                                                            | Description                                             |
| --- | ------------------------------------------------------------------ | ------------------------------------------------------- |
| 1   | [sftp_list_programs.py](examples/sftp/sftp_list_programs.py)       | List all .urp programs and browse the robot file system |
| 2   | [sftp_download_program.py](examples/sftp/sftp_download_program.py) | Download a .urp program file from the controller        |
| 3   | [sftp_upload_program.py](examples/sftp/sftp_upload_program.py)     | Upload a local .urp program file to the controller      |

#### 🔗 Primary Interface (port 30001)

| #   | Example                                                                                                   | Description                                                    |
| --- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 1   | [primary_interface_read_telemetry.py](examples/primary_interface/primary_interface_read_telemetry.py)     | Subscribe to robot mode, joint data, and cartesian info events |
| 2   | [primary_interface_send_urscript.py](examples/primary_interface/primary_interface_send_urscript.py)       | Send URScript commands directly to the robot controller        |
| 3   | [primary_interface_global_variables.py](examples/primary_interface/primary_interface_global_variables.py) | Read global variables declared in the loaded Polyscope program |

#### 🦾 Kinematics - Offline FK & IK (no connection needed)

| #   | Example                                                                            | Description                                                                    |
| --- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 1   | [kinematics_forward_inverse.py](examples/kinematics/kinematics_forward_inverse.py) | Select a UR model, compute FK from joint angles, then compute all IK solutions |

#### 🔑 License

| #   | Example                                                             | Description                                                            |
| --- | ------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1   | [license_info_example.py](examples/license/license_info_example.py) | Display license state, register a license, view all license properties |

---

## 📌 Protocol Reference

### ⚡ RTDE : Real-Time Data Exchange

RTDE is the recommended interface for high-frequency monitoring and control. It streams binary data at up to 500 Hz on port 30004 with a configurable recipe system.

**What you can do:**

- Subscribe to any combination of robot output variables (TCP pose, joint positions, forces, I/O states, temperatures, voltages, etc.)
- Write to robot input variables (digital outputs, analog outputs, integer/double/boolean registers)
- Stream at any frequency from 1 to 500 Hz (version 2 only)
- Use events (`output_data_received`) for reactive, non-blocking data handling

**Quick example:**

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
    vals = robot.rtde.output_data_values
    pose = vals.actual_tcp_pose
    force = vals.actual_tcp_force
    print(f"x={pose[0]:.3f}  Fx={force[0]:.2f} N")

    # Write back to the robot
    inputs = RtdeInputValues()
    inputs.input_int_registers.x24 = 42
    robot.rtde.write_inputs(inputs)

robot.disconnect()
```

---

### 📋 Dashboard Server : Polyscope Legacy

The Dashboard Server runs on port 29999 and exposes a text-based command interface for program lifecycle control. Compatible with all CB-Series and e-Series robots running Polyscope.

**What you can do:**

- Load, play, stop, and pause programs
- Power on/off the robot arm and release brakes
- Read robot mode, safety status, and Polyscope version
- Show and close popup messages on the teach pendant
- Set operational mode (Manual / Automatic) for remote control
- Add messages to the robot controller log

**Quick example:**

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

---

### 🌐 REST API : PolyscopeX

The REST API is available on PolyscopeX robots (Polyscope version 9+) and provides a modern HTTP-based interface for robot and program control.

**Quick example:**

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

---

### 🔗 Primary Interface

The Primary Interface (port 30001) streams binary data packets from the robot at ~10 Hz and also accepts URScript commands.

**What you can do:**

- Subscribe to robot mode, joint data, TCP cartesian position, tool data, safety data, and more
- Send URScript programs or commands to be executed immediately
- Read global variables declared in the loaded Polyscope program

**Quick example:**

```python
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters

robot = UR()
params = ConnectParameters("192.168.0.1")
params.primary_interface.enable = True
robot.connect(params)

@robot.primary_interface.cartesian_info_received
def on_cart(sender, event):
    c = robot.primary_interface.cartesian_info
    print(f"x={c.x:.3f}  y={c.y:.3f}  z={c.z:.3f}")

robot.primary_interface.script.send('set_digital_out(0, True)')
robot.disconnect()
```

---

### 📂 SFTP : File Transfer over SSH

SFTP gives full file system access to the UR controller over SSH (port 22).

**Default credentials:** user=`ur`, password=`easybot`

**What you can do:**

- List, download, and upload files
- Enumerate all `.urp` programs and `.installation` files
- Create and delete directories

**Quick example:**

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

---

### 🦾 Kinematics : Offline FK & IK

The SDK includes an offline kinematics engine with factory DH parameters for all UR models (UR3, UR5, UR10, UR3e, UR5e, UR7e, UR10e, UR12e, UR16e, UR15, UR18, UR20, UR30). No robot connection or license required.

**Quick example:**

```python
import math
from underautomation.universal_robots.kinematics.kinematics_utils import KinematicsUtils
from underautomation.universal_robots.common.robot_models_extended import RobotModelsExtended

dh = KinematicsUtils.get_dh_parameters_from_model(RobotModelsExtended.UR10e)

# Forward kinematics: joint angles → TCP pose
angles_rad = [math.radians(a) for a in [0, -90, 0, -90, 0, 0]]
result = KinematicsUtils.forward_kinematics(angles_rad, dh)
T = result.tool_transform  # 4×4 homogeneous matrix (flat list of 16 floats)

# Inverse kinematics: TCP pose → all joint solutions
solutions = KinematicsUtils.inverse_kinematics(T, dh)
nearest = KinematicsUtils.get_nearest_solution(solutions, angles_rad)
print([math.degrees(v) for v in nearest])
```

---

## 📚 Resources

- Documentation & licensing: **https://underautomation.com/universal-robots**
- Also available in [.NET](https://github.com/underautomation/UniversalRobots.NET), [LabVIEW](https://github.com/underautomation/UniversalRobots.vi), and [Unity](https://github.com/underautomation/UniversalRobots.Unity)

---

Made with ❤️ by the [UnderAutomation](https://underautomation.com) team.
