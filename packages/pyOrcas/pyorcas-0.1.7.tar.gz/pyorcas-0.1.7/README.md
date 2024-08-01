# pyOrcas

A Python package for communicating with the Orca motor using Modbus.

## Installation

```sh
pip install pyOrcas
```

## The Actuator Structure

The Actuator class in pyOrcas provides a modbus driven interface to interact with the Orca motors. Here's an overview of its structure and the available methods:

### Initialization

To initialize the Actuator object, provide the COM port and baud rate:

```sh
from pyOrcas import Actuator

actuator = Actuator(port='COM3', baudrate=9600)
#Update com port and baud rate to match the motor. Higher baud rates enable higher speeds.

```
### Closing the Port

Closing the serial port is important to ensure continued capability. When the object is deleted, it automatically closes the port. Recommendations:

1. At the end 

#### Properties

The Actuator class has several properties for reading various states and parameters:

1. position: Gets or sets the position of the actuator in micrometers.
2. force: Gets or sets the force exerted by the actuator in milliNewtons.
3. power: Gets the current power consumption of the actuator.
4. temperature: Gets the current temperature of the actuator.
5. voltage: Gets the current voltage of the actuator.
6. errors: Gets any error codes from the actuator.
7. op_mode: Gets the current operation mode of the actuator.

### Methods

The Actuator class provides several methods for communication and control:

1. close(): Closes the Modbus connection.
2. read_register(register_address, num_registers): Reads Modbus registers.
3. write_registers(registers_start_address, register_data): Writes multiple values to consecutive Modbus registers.
4. write_stream(registers_start_address, width, value): Writes a stream to the Modbus.
5. read_stream(register_address, width): Reads a stream from the Modbus.

Refer to the following user guide for documentation on the commands. https://irisdynamics.com/hubfs/Website/Downloads/Orca/Approved/UG210912_Orca_Series_Modbus_RTU_User_Guide.pdf

6. sleep(): Puts the motor to sleep.
7. Tune_PID(saturation, p_gain, i_gain, dv_gain, de_gain): Tunes the PID controller.

#### Haptic Mode

The Actuator class has a nested _HapticMode class for handling haptic effects. Here are the available methods:

1. enable(): Enables the haptic mode.
2. set_spring(ID, gain, center, deadzone, saturation, coupling=0, enable=None): Sets the parameters of a spring effect. ID: 0, 1, 2
3. toggle_spring(ID, enable=True): Enables or disables a spring effect.
4. set_oscillator(ID, gain, osctype, freq, duty, enable=None): Sets the parameters of an oscillator effect. ID: 0, 1
5. toggle_oscillator(ID, enable=True): Enables or disables an oscillator effect.
6. set_force(gain, enable=None): Sets a constant force effect.
7. toggle_force(enable=True): Enables or disables the constant force effect.
8. set_damper(gain, enable=None): Sets a damper effect.
9. toggle_damper(enable=True): Enables or disables the damper effect.
10. set_inertia(gain, enable=None): Sets an inertia effect.
11. toggle_inertia(enable=True): Enables or disables the inertia effect.
12. toggle_effects(f=False, s0=False, s1=False, s2=False, d=False, i=False, o1=False, o2=False): Toggles multiple haptic effects at once.

#### Kinematic Mode

The Actuator class has a nested _KinematicMode class for handling kinematic motions. Here are the available methods:

1. enable(): Enables the kinematic mode.
2. set_motion(ID, position, time, delay, nextID, autonext, motion_type=0): Sets the parameters of a kinematic motion.
3. trigger(ID): Triggers a kinematic motion by its ID.

## Updating the PyPI Release

To update the PyPI release of pyOrcas, follow these steps:

1. Update the version number in setup.py.

2. Build the distribution:
```sh
python setup.py sdist bdist_wheel
```
3. Upload the package to PyPI:
```sh
twine upload dist/*
```

Make sure you have twine installed and configured with your PyPI credentials.