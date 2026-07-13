## New arm models: UR18 and UR8L

The SDK now supports two additional robot models: UR18 and UR8 Long (UR8L).

The Dashboard `get_robot_model()` method returns the correct value for these models. Denavit-Hartenberg parameters for both models are also available for kinematics calculations.

```python
# Read the robot model from the Dashboard
response = ur.dashboard.get_robot_model()
# response.value is now RobotModels.UR18 or RobotModels.UR8L for the new models

# Use DH parameters for UR18 or UR8 Long in kinematics
dh = KinematicsUtils.get_dh_parameters_from_model(RobotModelsExtended.UR18)
dh_long = KinematicsUtils.get_dh_parameters_from_model(RobotModelsExtended.UR8Long)
```
