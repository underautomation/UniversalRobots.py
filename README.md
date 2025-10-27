![Universal Robots Python SDK hero image](https://user-images.githubusercontent.com/47540360/136141853-1ec87530-d88e-467f-adb4-ec3c46d26010.png)

<h1 align="center">Universal Robots Communication SDK for Python</h1>

<p align="center">
  <a href="https://pypi.org/project/UnderAutomation.UniversalRobots"><img src="https://img.shields.io/badge/PyPI-UnderAutomation.UniversalRobots-blue" alt="PyPI"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.7%2B-3776AB"></a>
  <a href="https://underautomation.com/universal-robots"><img src="https://img.shields.io/badge/Docs-UnderAutomation.com-ff69b4"></a>
  <a href="https://github.com/underautomation/UniversalRobots.NET"><img src="https://img.shields.io/badge/Also%20available-.NET-5c2d91"></a>
  <a href="https://github.com/underautomation/UniversalRobots.vi"><img src="https://img.shields.io/badge/LabVIEW-🟨-fede00"></a>
  <a href="https://github.com/underautomation/UniversalRobots.Unity"><img src="https://img.shields.io/badge/Unity-🧊-000000"></a>
</p>

> Build delightful, production-ready apps that talk to your Universal Robots cobots in real time.

https://user-images.githubusercontent.com/47540360/143318635-6d6aaaf4-5642-457a-8ff1-4322f2defe82.mp4

---

## 🚀 Why you'll love it

- **Instant connectivity.** Speak RTDE, Primary Interface, SSH, sockets, and SFTP with a single API.
- **Battle-tested.** Powering automation stacks in factories, labs, and classrooms around the world.
- **Friendly by design.** Pythonic abstractions, rich events, and typed helpers for poses, registers, variables, and more.

## 🧠 What is inside?

The SDK wraps the Universal Robots communication stack so you can:

- Stream telemetry up to 500 Hz with RTDE (read & write registers, sync IO, monitor forces).
- Drive URScript over the Primary Interface, fetch installation & program variables, and react to robot state changes.
- Run custom socket servers that chat with UR scripts and external tools.
- Move files back and forth with SFTP, and run shell commands securely via SSH.
- Decode `.urp` programs and `.installation` files into editable XML.
- Convert poses between rotation vectors and roll-pitch-yaw angles in one line.

## 📦 Install it

### From PyPI

```bash
pip install UnderAutomation.UniversalRobots
```

### From source

```bash
git clone https://github.com/underautomation/UniversalRobots.py.git
cd UniversalRobots.py
pip install -e .
```

## 🧪 Your first robot handshake

```python
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from underautomation.universal_robots.rtde.rtde_input_values import RtdeInputValues

robot = UR()

# Configure how we want to talk to the cobot
params = ConnectParameters("192.168.0.1")
params.primary_interface.enable = True               # Live access to variables, IO, and URScript
params.rtde.enable = True
params.rtde.frequency = 5                            # Up to 500 Hz if you need it
params.rtde.input_setup.add(RtdeInputData.StandardAnalogOutput0)
params.rtde.input_setup.add(RtdeInputData.InputBitRegisters, 64)
params.rtde.output_setup.add(RtdeOutputData.ActualTcpPose)
params.rtde.output_setup.add(RtdeOutputData.ActualTcpForce)

robot.connect(params)

# Subscribe to fresh RTDE packets
@robot.rtde.output_data_received
def on_output(sender, event):
    pose = robot.rtde.output_data_values.actual_tcp_pose
    force = robot.rtde.output_data_values.actual_tcp_force

    inputs = RtdeInputValues()
    inputs.standard_analog_output0 = 0.2
    inputs.input_bit_registers.x64 = True
    robot.rtde.write_inputs(inputs)
```

## 🕹️ Talk back to URScript via sockets

```python
from underautomation.universal_robots.socket_communication import SocketClientConnectionEventArgs, SocketRequestEventArgs

params.socket_communication.enable = True
params.socket_communication.port = 50001

@robot.socket_communication.socket_client_connection
def on_client(_, event: SocketClientConnectionEventArgs):
    event.client.socket_write("Hello cobot <3")

@robot.socket_communication.socket_request
def on_message(_, event: SocketRequestEventArgs):
    print("Robot says:", event.message)

robot.socket_communication.socket_write("123456")
```

## 📁 File ops & shell superpowers

```python
from underautomation.universal_robots.common.pose import Pose
from underautomation.universal_robots.ur_installation import URInstallation
from underautomation.universal_robots.ur_program import URProgram

params.ssh.enable_sftp = True
robot.connect(params)

items = robot.sftp.list_directory("/home/ur/ursim-current/programs/")
robot.sftp.download_file("/home/ur/ursim-current/programs/prg.urp", "C:/temp/prg.urp")
robot.ssh.run_command("echo Hello > /home/ur/Desktop/NewFile.txt")

pose = Pose(0.1, 0.2, -0.1, 0, 0.05, 0.1)
rpy = pose.from_rotation_vector_to_rpy()
program = URProgram.load("C:/temp/prg.urp")
```

## 📚 Resources

- Documentation & licensing: **https://underautomation.com/universal-robots**
- Product tour & updates: **whatsNew.md** in this repository
- Need .NET, LabVIEW, or Unity? We have you covered in the badges above.

## 🛡️ Licensing

This SDK is a commercial library. A valid license **must** be purchased to deploy it in production. Once licensed, you can ship an unlimited number of applications with zero royalties or recurring fees.

👉 Learn more & request pricing at [UnderAutomation.com](https://underautomation.com).

---

Made with ❤️ by the UnderAutomation team.
