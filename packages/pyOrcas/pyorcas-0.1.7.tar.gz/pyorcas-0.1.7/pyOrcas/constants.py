# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:36:22 2024

@author: DAlexander
"""
#CTRL_Reg 0 commands:
RESET=1
CLR_ERR=2 
ZERO_POS=4 
INVERT=8


# Modbus Function Codes
Read = 3
Write = 6
Write_Multi = 16
MotorCommand = 100
MotorRead = 104
MotorWrite = 105

Read_Msg_length = 5 #base length of read msg
Write_Msg_length = 8 #Message length received when writing registers
Write_Stream_Length = 20 #Message length when writing stream
Read_Stream_Length = 24 #Message length when reading stream

# Modes of Operation
SleepMode = 1
ForceMode = 2
PositionMode = 3
HapticMode = 4
KinematicMode = 5
AutoZeroMode = 55

# Control Registers
CTRL_REG_0 = 0
CTRL_REG_1 = 1
CTRL_REG_2 = 2
MODE_Reg = 3
CTRL_REG_4 = 4

# Motor Registers
KIN_SW_TRIGGER = 9 #Kinematic triggering register

PC_PGAIN = 133 #P gain, starting register for updating all PID

POS_SIGN = 152 #Direction of motor

ZERO_MODE = 171 #Zeroing mode of the motor

MODE_OF_OPERATION = 317 #Current mode of operation

KINEMATIC_STATUS = 319 #Current status and motion

VDD_FINAL = 338 #Motor Supply Voltage
SHAFT_POSITION_UM = 342 #Lower 2 bytes, upper 2 bytes at 343
SHAFT_SPEED_MMPS = 344 #Lower bytes of shaft speed
SHAFT_ACCEL_MMPSS = 346  #Lower bytes of shaft acceleration
FORCE = 348 #Lower bytes of force
POWER = 350 #Sensed power
AVG_POWER = 355 #Average power of actuator
COIL_TEMP = 356 #Estimated coil temperature

SERIAL_NUMBER_LOW = 406 #Register for Low bytes of serial number, 407 for high bytes

MAJOR_VERSION = 408 #Register for major firmware version, next two registers account for minor and revision numbers
STATOR_CONFIG = 418 #Register for the motor type

ERROR_0 = 432 #Currently latched errors

HAPTIC_STATUS = 641 #Sets haptic effects
CONSTANT_FORCE_MN = 642 #Register to set constant force
SPRING_1 = 644 #First register of spring registers

D0_GAIN_NS_MM = 662 #Registers for the Damper
I0_GAIN_NS2_MM = 663 #Register for the inertia effect

OSCILLATOR_1 = 664 #Register for the first Oscillator, used to index over all settings

HAPTIC_SOFTSTART = 673 #Register for softstart in haptic mode

KIN_REGISTER_0 = 780 #First register of kinematic settings, every 6 is new kinematic

KIN_HOME_ID = 972 #Register for home position
