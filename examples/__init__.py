"""
Helper for UniversalRobots.py examples
- Automatic sys.path setup
- Persistent robot configuration management
- License management
- Connect helpers per protocol
"""
import sys
import json
from pathlib import Path

# ==============================================================================
# Path setup for imports
# ==============================================================================
def setup_path():
    root = Path(__file__).parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

setup_path()

# ==============================================================================
# Configuration file management
# ==============================================================================
_config_file = Path(__file__).parent / "robot_config.json"

def _load_config():
    """Load saved configuration from file."""
    if _config_file.exists():
        try:
            with open(_config_file, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def _save_config(config):
    """Save configuration to file."""
    with open(_config_file, 'w') as f:
        json.dump(config, f, indent=2)

def _get_setting(key, prompt, default=None, hide_default=False):
    """
    Generic helper to get a setting from the user.
    If already saved, proposes it as default. Otherwise, asks the user and saves it.

    Args:
        key: Config key to load/save
        prompt: Display prompt for the user
        default: Default value if none saved
        hide_default: If True, shows '****' instead of the saved value (for passwords)

    Returns:
        str: The setting value
    """
    config = _load_config()
    saved = config.get(key, default)

    if saved is not None:
        display = "****" if hide_default and saved else saved
        user_input = input(f"{prompt} [{display}]: ").strip()
        value = user_input if user_input else saved
    else:
        value = input(f"{prompt}: ").strip()

    # Save if value has changed or is new
    if value != config.get(key):
        config[key] = value
        _save_config(config)

    return value

# ==============================================================================
# Robot IP / Connection
# ==============================================================================
def get_robot_ip():
    """
    Gets the UR controller IP address.
    If already saved, proposes it as default.

    Returns:
        str: Robot IP address (e.g. 192.168.0.1)
    """
    return _get_setting("robot_ip", "Robot IP address")

# ==============================================================================
# SSH / SFTP settings
# ==============================================================================
def get_ssh_username():
    """
    Gets the SSH username for the UR controller.
    Default UR SSH user is 'ur'.

    Returns:
        str: SSH username
    """
    return _get_setting("ssh_username", "SSH username", default="ur")

def get_ssh_password():
    """
    Gets the SSH password for the UR controller.
    Default UR SSH password is 'easybot'.

    Returns:
        str: SSH password
    """
    return _get_setting("ssh_password", "SSH password", default="easybot", hide_default=True)

# ==============================================================================
# License management
# ==============================================================================
def setup_license():
    """
    Checks the current license state and handles registration.

    - If already licensed or in trial: prints license info
    - If expired or invalid: asks user for licensee/key and registers
    - If user has no key: shows URL to request a free trial

    Returns:
        LicenseInfo: The current license information
    """
    from underautomation.universal_robots.ur import UR
    from underautomation.universal_robots.license.license_state import LicenseState

    # Try loading saved license credentials
    config = _load_config()
    saved_licensee = config.get("licensee", "")
    saved_key = config.get("license_key", "")

    # Register saved license if available
    if saved_licensee and saved_key:
        license_info = UR.register_license(saved_licensee, saved_key)
    else:
        # Check default trial state without credentials
        from underautomation.universal_robots.license.license_info import LicenseInfo
        license_info = LicenseInfo(None, None)

    state = license_info.state

    # If license is valid (Licensed, Trial, or ExtraTrial), just display info
    if state == LicenseState.Licensed or state == LicenseState.Trial or state == LicenseState.ExtraTrial:
        print("=" * 60)
        print("LICENSE INFO")
        print("=" * 60)
        print(license_info)
        print("=" * 60)
        return license_info

    # License is invalid, expired, or needs maintenance
    print("=" * 60)
    print("LICENSE REGISTRATION REQUIRED")
    print("=" * 60)
    print(f"Current license state: {license_info}")
    print()
    print("If you don't have a license key, you can request a free")
    print("trial license immediately by email from:")
    print("  https://underautomation.com/license")
    print()

    licensee = input("Enter licensee (company/name) [leave empty to skip]: ").strip()
    if not licensee:
        print("Skipping license registration. Running in current mode.")
        return license_info

    key = input("Enter license key: ").strip()
    if not key:
        print("No key provided. Skipping registration.")
        return license_info

    # Register the license
    license_info = UR.register_license(licensee, key)

    # Save credentials
    config["licensee"] = licensee
    config["license_key"] = key
    _save_config(config)

    print()
    print("LICENSE REGISTERED:")
    print(license_info)
    print("=" * 60)

    return license_info

# ==============================================================================
# Helper: Connect to robot with selected protocols
# ==============================================================================
def connect_robot(
    enable_dashboard=False,
    enable_primary_interface=False,
    enable_rtde=False,
    enable_sftp=False,
    enable_rest=False,
    rtde_frequency=10,
):
    """
    Creates a UR instance, sets up license, asks for connection settings,
    and connects with the specified protocols enabled.

    Args:
        enable_dashboard: Enable Dashboard Server (port 29999)
        enable_primary_interface: Enable Primary Interface (port 30001)
        enable_rtde: Enable RTDE real-time data exchange (port 30004)
        enable_sftp: Enable SFTP file transfer over SSH
        enable_rest: Enable REST API (PolyscopeX only)
        rtde_frequency: RTDE output frequency in Hz (default 10)

    Returns:
        UR: Connected robot instance
    """
    from underautomation.universal_robots.ur import UR
    from underautomation.universal_robots.connect_parameters import ConnectParameters

    # Setup license first
    setup_license()

    # Get robot address
    robot_ip = get_robot_ip()

    # Create robot and connection parameters
    robot = UR()
    params = ConnectParameters(robot_ip)

    # Configure protocols
    params.dashboard.enable = enable_dashboard
    params.primary_interface.enable = enable_primary_interface

    if enable_rtde:
        params.rtde.enable = True
        params.rtde.frequency = rtde_frequency

    if enable_sftp:
        params.ssh.enable = True
        params.ssh.enable_sftp = True
        params.ssh.username = get_ssh_username()
        params.ssh.password = get_ssh_password()

    if enable_rest:
        params.rest.enable = True

    # Disable unused protocols
    params.socket_communication.enable = False
    params.xml_rpc.enable = False

    # Log active protocols
    protocols = []
    if enable_dashboard:        protocols.append("Dashboard")
    if enable_primary_interface: protocols.append("Primary Interface")
    if enable_rtde:             protocols.append("RTDE")
    if enable_sftp:             protocols.append("SFTP")
    if enable_rest:             protocols.append("REST")
    print(f"\nConnecting to {robot_ip} ({', '.join(protocols)})...")

    try:
        robot.connect(params)
    except Exception as e:
        error_msg = str(e)
        if any(kw in error_msg.lower() for kw in ("license", "trial", "expired")) or \
                "InvalidLicenseException" in type(e).__name__:
            readable = error_msg.split("\n")[0].strip() if "\n" in error_msg else error_msg
            safe_msg = readable.encode("ascii", errors="replace").decode("ascii")
            print(f"\nLicense error: {safe_msg}")
            print("\nPlease register a valid license first.")
            print("Get a free trial at: https://underautomation.com/license")
            raise SystemExit(1)
        raise

    print("Connected successfully!\n")
    return robot
