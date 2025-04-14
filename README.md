[![Python](https://img.shields.io/badge/Python-3.5_|_3.6_|_3.7_|_3.8|_3.9_|_3.10_|_3.11_|_3.12_-blue)](#)

# Universal Robots communication SDK

Quickly create applications that communicate with an [Universal Robots](https://www.universal-robots.com) industrial robot.

SDK : Software Development Kit

🔗 **More Information:** [https://underautomation.com/fanuc](https://underautomation.com/universal-robots)  
🔗 Also available in **[🟦 .NET](https://github.com/underautomation/UniversalRobots.NET)** & **[🟨 LabVIEW](https://github.com/underautomation/UniversalRobots.vi)** & [🧊 Unity](https://github.com/underautomation/UniversalRobots.Unity)

[![UnderAutomation Universal Robots communication SDK](https://user-images.githubusercontent.com/47540360/136141853-1ec87530-d88e-467f-adb4-ec3c46d26010.png)](https://underautomation.com)

https://user-images.githubusercontent.com/47540360/143318635-6d6aaaf4-5642-457a-8ff1-4322f2defe82.mp4

## Try it

From Pypi :

```
pip install UnderAutomation.UniversalRobots
```

From this repo :

```
git clone https://github.com/underautomation/UniversalRobots.py.git
pip install pythonnet==3.0.3
```

Import features :

```py
from underautomation.universal_robots.ur import UR
from underautomation.universal_robots.connect_parameters import ConnectParameters
from underautomation.universal_robots.common.pose import Pose
from underautomation.universal_robots.rtde.rtde_input_data import RtdeInputData
from underautomation.universal_robots.rtde.rtde_output_data import RtdeOutputData
from underautomation.universal_robots.rtde.rtde_input_values import RtdeInputValues
# from underautomation.universal_robots... import ...
# etc.
```

## Features

### RTDE and Primary Interface

Full support for :

- RTDE (Real-Time Data Exchange) : read and write registers up to 500Hz
- Primary Interface :
  - Receive robot state data at 10Hz : Cartesian and angular position, robot status, inputs and outputs value, and 100+ more measurements ...
  - Send URScript
  - Get variables

```py
# Create a robot instance
robot = UR()

# Setup connection to th robot
param = ConnectParameters()
param.ip = "192.168.0.1"

# Enable primary interface to get variable values
param.primary_interface.enable = True

# Enable rtde at 5Hz (500Hz possible)
param.rtde.enable = True
param.rtde.frequency = 5

# Ask the robot for permission to write these registers
param.rtde.input_setup.add(RtdeInputData.StandardAnalogOutput0)
param.rtde.input_setup.add(RtdeInputData.InputBitRegisters, 64)

# Ask the robot to send me this data
param.rtde.output_setup.add(RtdeOutputData.ActualTcpPose)
param.rtde.output_setup.add(RtdeOutputData.ActualTcpForce)

# Connect to the robot
robot.connect(param)

# Function called when new RTDE data is received
def on_output_data_received(o, e):
    ##
    # Display robot TCP pose
    pose = robot.rtde.output_data_values.actual_tcp_pose
    # pose.X, pose.Y, pose.Z, pose.Rx, ...

    # Display robot TCP force
    force = robot.rtde.output_data_values.actual_tcp_force

    # Write data in robot controler
    inputs = RtdeInputValues()
    inputs.standard_analog_output0 = 0.2
    inputs.input_bit_registers.x64 = True
    robot.rtde.write_inputs(inputs)
    ##

# Event raised when data is received
robot.rtde.output_data_received(on_output_data_received)

# Function called when any program or installation variable changes in the robot
def on_value_updated(p, e):
    ##
    # Display all program and installation variables
    variables = robot.primary_interface.global_variables.get_all()
    name = variables[0].name
    value = variables[0].to_pose()
    type = variables[0].type
    ##

# Event raised when a program or installation variable change
robot.primary_interface.global_variables.values_updated(on_value_updated)


# Function called when masterboard data is received
def on_masterboard_data_received(p, e):
    ai0 = robot.primary_interface.masterboard_data.analog_input0
    di2 = robot.primary_interface.masterboard_data.digital_inputs.digital2

# Several other events are raised by primary interface
robot.primary_interface.masterboard_data_received(on_masterboard_data_received)

# Function called when cartesian data is received
def on_cartesian_info_received(p, e):
    x = e.X
    tcpOffsetX = e.TCPOffsetX

robot.primary_interface.cartesian_info_received(on_cartesian_info_received)

# Function called when joint data is received
def on_joint_data_received(o,e):
    shoulderAngle = e.Shoulder.Position
    elbowMode = e.Elbow.JointMode
    wrist3Speed = e.Wrist3.ActualSpeed

robot.primary_interface.joint_data_received(on_joint_data_received)
```

### Read variables

Read program and installation variables :

```py
myVar = robot.primary_interface.global_variables.get_by_name("myVar")
variables =  robot.primary_interface.global_variables.get_all()
```

### Dashboard Server

Remote control the robot : load, play, pause, and stop a robot program, power on and off, release brake, shutdown, ...

```py
# Create a new robot instance
robot = UR()

# Setup connection to th robot
param = ConnectParameters("192.168.0.56")
param.dashboard.enable=True

# Connect to the robot
robot.connect(param)

# Display a popup on the pendant
robot.dashboard.show_popup("I just remote-controlled my robot!")

# Power on the robot arm and release brakes
robot.dashboard.power_on()
robot.dashboard.release_brake()

# Load program file to polyscope
robot.dashboard.load_program("fast_bin_picking.urp")

# Start the program
robot.dashboard.play()

# Get program name and state
state = robot.dashboard.get_program_state()
```

### XML-RPC

From your robot program, remote call a function implemented in your .NET program. For example, this allows you to request a position resulting from image processing.

Robot code (URScript) :

```ruby
# Connect to the SDK and specifie the IP and port of the PC
rpc:=rpc_factory("xmlrpc","http://192.168.0.10:50000")

# Call method GetPose and wait for the reply. The replied pose will be assigned in variable "answer"
answer:=rpc.GetPose(100)
```

Python code :

```py
# XML-RPC server on port 50000
parameters.xml_rpc.enable = True
parameters.xml_rpc.port = 50000

# Event callback :
# robot.xml_rpc.xml_rpc_server_request
```

### Socket communication

The library can start a communication. The robot can connect to your server and exchange custom data.

Robot code (URScript) :

```ruby
# Connect to robot socket server in URScript
socket_open("192.168.0.10", 50001)

# Raise event SocketRequest is your app
socket_send_string("Hello from robot")

# Raise event SocketGetVar is your app
var1 := socket_get_var("MY_VAR")
```

Python code :

```py
robot = UR()

# Setup connection to th robot
param = ConnectParameters("192.168.0.1")

# Enable spcket server on port 50001
param.socket_communication.enable = True
param.socket_communication.port = 50001

# Connect to the robot
robot.connect(param)

##
# Function called when robot connects with URScipt function socket_open()
def on_socket_client_connection(o, e : SocketClientConnectionEventArgs):
   e.client.socket_write("Hello cobot <3")

robot.socket_communication.socket_client_connection(on_socket_client_connection)

# Function called when the robot sends a message with socket_write()
def on_socket_request(o,e:SocketRequestEventArgs):
   # Get robot message
   robotMessage = e.Message

robot.socket_communication.socket_request(on_socket_request)

# Send a message to all connected clients
robot.socket_communication.socket_write("123456")
##

# List of all connected clients
connectedClients = robot.socket_communication.connected_clients

# IP address and remote port of a client
clientEndpoint = connectedClients[0].end_point

# Send a message to a specific connected robot
connectedClients[0].socket_write("Hello robot [0]")

 # Handle client disconnection
def on_socket_client_disconnection(o,e):
   pass

connectedClients[0].socket_client_disconnection(on_socket_client_disconnection)
```

### SFTP

Manipulate files and folders of the robot via SFTP (Secure File Transfer Protocol) : download to the robot, import from the robot, rename, delete, move, list files in a folder...

```py
robot = UR()

# Setup connection to th robot
param = ConnectParameters("192.168.0.1")

# Enable SFTP file access
param.ssh.enable_sftp = True

# Connect to the robot
robot.connect(param)

# Enumerates files and folder
items = robot.sftp.list_directory("/home/ur/ursim-current/programs/")

# Download program file prg.urp to your local disk
robot.sftp.download_file("/home/ur/ursim-current/programs/prg.urp", "C:\\temp\\prg.urp")

# Send a local file to the robot
robot.sftp.upload_file("C:\\temp\\prg.urp", "/home/ur/ursim-current/programs/prg.urp")

# Manipulate files and directories
robot.sftp.rename_file("/home/ur/prg.urp", "/home/ur/prg2.urp")
robot.sftp.delete("/home/ur/prg.urp")
exists = robot.sftp.exists("/home/ur/prg.urp")
robot.sftp.write_all_text("/home/ur/file.txt", "Hello robot !")
```

### SSH

Open a SSH (Secure Shell) connection with the robot to execute Linux command lines, as in the terminal.

```py
robot.ssh.run_command("echo Hello > /home/ur/Desktop/NewFile.txt");
```

### Convert position types

Convert Rotation Vector to and from RPY.

```py
# Create X, Y, Z, RX, RY, RZ pose
pose = Pose(0.1, 0.2, -0.1, 0, 0.05, 0.1)

# Convert cartesian pose type to RPY or rotation vector
rpy = pose.from_rotation_vector_to_rpy()
vectorPose = pose.from_rpy_to_rotation_vector()
```

### Edit program and installation files

Open and edit program (.urp) and installation (.installation) files :

```py
# Decompile program and installation files and access inner XML
installation = URInstallation.load("C:\\temp\\default.installation")
prg = URProgram.load("C:\\temp\\prg.urp")
internalXml = prg.xml
```

## License

This SDK is a commercial library and a license _must_ be purshased. Once acquired, any application you develop can be delivered to an unlimited number of customers without royalties and without recurring subscription.

More information : [https://underautomation.com](https://underautomation.com)
