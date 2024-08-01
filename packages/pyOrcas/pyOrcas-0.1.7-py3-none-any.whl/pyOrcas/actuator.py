# -*- coding: utf-8 -*-
"""   
    
   @file actuator.py
   @author Daniel Alexander <dalexander@irisdynamics.com>, work based on code by RMcWilliam's Matlab integration
   @brief Can read and write parameters, configure all haptic effects, and kinematic motions
       Classes
           Actuator
           |-Haptic
           |-Kinematic

       Usage:
           from pyOrcas import Actuator
           actuator = Actuator(port='COM3', baudrate=9600)
   
    @copyright Copyright 2024 Iris Dynamics Ltd 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    
    For questions or feedback on this file, please email <support@irisdynamics.com>. 
    
"""

from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusIOException
import struct
from .constants import *
import time


class Actuator:
    """ DEFAULT CLASS METHODS """
    def __init__(self, port:str, baudrate:int):
        """Constructs the class based on provide COM and baudrate"""
        self.client = ModbusSerialClient(method='rtu', port=port, baudrate=baudrate, parity='E', stopbits=1, bytesize=8, timeout=100)
        if self.client.connect():
            print("Modbus connection successful.")
        else:
            print("Modbus connection failed.")
            self.close()
            
        # Initialize mode handlers
        self.haptic = self._HapticMode(self)
        self.kinematic = self._KinematicMode(self)
        
        # Initialize motor properties
        self._position = 0 #Set as both property and setter
        self._force = 0 #Set as both property and setter
        self._power = 0 #Set as property
        self._temperature = 0 #Set as property
        self._voltage = 0 #Set as property
        self._errors = 0 #Set as property
        self._op_mode = 0 #Set as property
        self._velocity = 0 #Set as property
        self._acceleration = 0 #Set as property
        self._direction = None  #Set as property
        self._mode = None #Set as property
        
        # Initialize device information
        self.stator_type = None
        self.device_name = None
        self.serial_number = None
        self.revision = None
        
        self._initialize_info() #Set basic information of actuator, cannot be in init
        
        self.sleep() #Sleep the motor
        self._clear2048() #Clear communication error if possible
        
    def __str__(self):
        """String representation of the Actuator object"""
        return (          
            f"Device Name: {self.device_name}\n"
            f"Serial Number: {self.serial_number}\n"
            f"Firmware: {self.revision}\n"
        )
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Runtime exit function."""
        self.close()
        
    def __del__(self):
        """Ensure the Modbus connection is closed when the object is deleted."""
        self.close()
        
    """ GETTERS AND SETTERS """        
    @property
    def position(self):
        positionBytes=self.read_register(SHAFT_POSITION_UM,2)
        self._position=self._combine_u16_to_u32(positionBytes[0],positionBytes[1])
        return self._position
    
    @position.setter
    def position(self, position_um:int):
        positionbytes = struct.pack('>i', position_um)
        message = [1, MotorCommand, 30] + list(positionbytes)
        message_with_crc = self._append_crc(message)
        
        self.client.send(bytes(message_with_crc))
        data=self.client.recv(19)

        self._position = struct.unpack('>i', bytes(data[2:6]))[0]
        self._force = struct.unpack('>i', bytes(data[6:10]))[0]
        self._power = struct.unpack('>H', bytes(data[10:12]))[0]
        self._temperature = data[12]
        self._voltage = struct.unpack('>H', bytes(data[13:15]))[0]
        self._errors = struct.unpack('>H', bytes(data[15:17]))[0]
    
    @property
    def force(self):
        forceBytes=self.read_register(FORCE,2)
        self._position=self._combine_u16_to_u32(forceBytes[0],forceBytes[1])
        return self._force
    
    @force.setter
    def force(self, force_mN:int):
        forcebytes = struct.pack('>i', force_mN)
        message = [1, MotorCommand, 28] + list(forcebytes)
        message_with_crc = self._append_crc(message)
        
        #self._flush_input_buffer()
        self.client.send(bytes(message_with_crc))
        data=self.client.recv(19)

        self._position = struct.unpack('>i', bytes(data[2:6]))[0]
        self._force = struct.unpack('>i', bytes(data[6:10]))[0]
        self._power = struct.unpack('>H', bytes(data[10:12]))[0]
        self._temperature = data[12]
        self._voltage = struct.unpack('>H', bytes(data[13:15]))[0]
        self._errors = struct.unpack('>H', bytes(data[15:17]))[0]
    
    @property
    def power(self):
        self._power=self.read_register(POWER, 1)[0]
        return self._power
    
    @property
    def temperature(self):
        self._temperature=self.read_register(COIL_TEMP, 1)[0]
        return self._temperature
    
    @property
    def voltage(self):
        self._voltage=self.read_register(VDD_FINAL, 1)[0]
        return self._voltage
    
    @property
    def errors(self):
        self._errors=self.read_register(ERROR_0, 1)[0]
        return self._errors
    
    @property
    def op_mode(self):
        self._op_mode=self.read_register(MODE_OF_OPERATION, 1)[0]
        return self._op_mode
    
    @property
    def velocity(self):
        velocityBytes=self.read_register(SHAFT_SPEED_MMPS,2)
        self._velocity=self._combine_u16_to_u32(velocityBytes[0],velocityBytes[1])
        return self._velocity
    
    @property
    def acceleration(self):
        accelBytes=self.read_register(SHAFT_ACCEL_MMPSS,2)
        self._acceleration=self._combine_u16_to_u32(accelBytes[0],accelBytes[1])
        return self._acceleration
    
    @property
    def invert(self):
        return None
    
    @invert.setter
    def invert(self, enable:bool):
        if enable:
            self.write_registers(POS_SIGN,1)
        else:
            self.write_registers(POS_SIGN,0)
            
    @property
    def mode(self):
        self._mode=self.read_register(MODE_OF_OPERATION,1)[0]
        return self._mode
        
    def close(self):
        self.client.close()  
        
    """ INTERNAL COMMANDS """
    
    def _initialize_info(self):
        #Basic Stator Information        
        self.stator_type=self.read_register(STATOR_CONFIG, 1)[0]
        
        if self.stator_type==0:        
            self.device_name="Orca-6-24V"
        elif self.stator_type==1:  
            self.device_name="Orca-6-48V"
        elif self.stator_type==2:  
            self.device_name="Orca-15-48V"
        else:
            self.device_name="Unknown"
        
        sn_u16s=self.read_register(SERIAL_NUMBER_LOW, 2)
        self.serial_number=self._combine_u16_to_u32(sn_u16s[0],sn_u16s[1])
        
        rev=self.read_register(MAJOR_VERSION , 3)
        self.revision=f"{rev[0]}.{rev[1]}.{rev[2]}"
        
    def _clear2048(self):
        if self.errors == 2048:
            self.write_register(CTRL_REG_0, CLR_ERR)
        
    
    def _u16_to_bytes(self, data):
        """Convert a 16-bit unsigned integer to a byte array in big-endian order."""
        if isinstance(data, list):
            result = []
            for value in data:
                result.extend(struct.pack('>H', value))
            return result
        else:
            return list(struct.pack('>H', data))  
    
    
    def _int32_to_u16(self, data):
        """Convert a 32-bit integer to a 16-bit unsigned integer."""
        if not (-2**31 <= data < 2**31):
            raise ValueError("Input data is out of range for a 32-bit integer")
        byte_data = struct.pack('<i', data)
        return list(struct.unpack('<2H', byte_data))
    
    
    def _combine_u16_to_u32(self, low, high):
        """Combine two 16-bit unsigned integers into a single 32-bit unsigned integer."""
        return (high << 16) | low
    
    

    def _calculate_crc(self, message):
        """Calculate the CRC for a Modbus message."""
        crc = 0xFFFF
        polynomial = 0xA001
        for byte in message:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc >>= 1
                    crc ^= polynomial
                else:
                    crc >>= 1
        low_byte = crc & 0xFF
        high_byte = (crc >> 8) & 0xFF
        return [low_byte, high_byte]
    
    
    def _append_crc(self, message):
        """Append the CRC to the message."""
        return message + self._calculate_crc(message)
        
    """ READ AND WRITE COMMANDS """

    def read_register(self, register_address:int, num_registers:int):
        """Read Modbus registers by sending a custom message with CRC."""
        address_bytes = self._u16_to_bytes(register_address)
        num_registers_bytes = self._u16_to_bytes(num_registers)
        message = [1, Read] + address_bytes + num_registers_bytes
        message_with_crc = self._append_crc(message)
        
        self.client.send(bytes(message_with_crc))
        data = self.client.recv(Read_Msg_length + 2 * num_registers)
        
        if not data:
            print("Failed to read registers")
            return None

        read_value = []
        for i in range(num_registers):
            high_byte = data[2 * i + 3]
            low_byte = data[2 * i + 4]
            value = struct.unpack('H', struct.pack('BB', low_byte, high_byte))[0]
            read_value.append(value)

        return read_value
        
    def write_registers(self, registers_start_address:int, register_data:int):
        """Write multiple values to consecutive Modbus registers.
        Can accept an array of integers or individual integers, and will write
        consecutive registers equal to the number of arguments"""
        
        # Ensure register_data is a list
        if isinstance(register_data, int):
            register_data = [register_data]
        
        num_registers = len(register_data)
        databytes = self._u16_to_bytes(register_data)
        num_registers_bytes = self._u16_to_bytes(num_registers)
        address_bytes = self._u16_to_bytes(registers_start_address)
        byte_count = [num_registers * 2]

        message = [1, Write_Multi] + address_bytes + num_registers_bytes + byte_count + databytes
        message_with_crc = self._append_crc(message)
        
        self.client.send(bytes(message_with_crc))
        self.client.recv(Write_Msg_length)
        
    def write_stream(self, registers_start_address:int, width:int, value:int):
        address_bytes = self._u16_to_bytes(registeraddr)
        value_bytes = struct.pack('>i', value)
        message = [1, MotorWrite] + address_bytes + [width] + list(value_bytes)
        message_with_crc = self._append_crc(message)
        
        self.client.send(bytes(message_with_crc))
        data=self.client.recv(Write_Stream_Length)
        
        if len(data) == Write_Stream_Length:
            self._op_mode = data[2]
            self._position = struct.unpack('>i', bytes(data[3:7]))[0]
            self._force = struct.unpack('>i', bytes(data[7:11]))[0]
            self._power = struct.unpack('>H', bytes(data[11:13]))[0]
            self._temperature = data[13]
            self._voltage = struct.unpack('>H', bytes(data[14:16]))[0]
            self._errors = struct.unpack('>H', bytes(data[16:18]))[0]
        else:
            print("Received data length is incorrect")
        
    def read_stream(self,register_address:int,width:int):
        address_bytes = self._u16_to_bytes(register_address)
        message = [1, MotorRead] + address_bytes + [width]
        message_with_crc = self._append_crc(message)
        
        self.client.send(bytes(message_with_crc))
        data=self.client.recv(Read_Stream_Length)
        
        if len(data) == Read_Stream_Length:
            self._op_mode = data[6]
            read_value = struct.unpack('>i', data[2:6])[0]
            self._position = struct.unpack('>i', bytes(data[7:11]))[0]
            self._force = struct.unpack('>i', bytes(data[11:15]))[0]
            self._power = struct.unpack('>H', bytes(data[15:17]))[0]
            self._temperature = data[17]
            self._voltage = struct.unpack('>H', bytes(data[18:20]))[0]
            self._errors = struct.unpack('>H', bytes(data[20:22]))[0]
            
            return float(read_value)
        else:
            print("Received data length is incorrect")
    
    """ SPECIFIC ORCA FUNCTIONS """
    def sleep(self):
        """Put motor to sleep"""
        while self.read_register(MODE_OF_OPERATION,1)[0]!=1:
            self.write_registers(MODE_Reg, SleepMode)
    
    def Tune_PID(self, saturation:int, p_gain:int, i_gain:int, dv_gain:int, de_gain:int):
        sat_data=self._int32_to_u16(saturation)
        data=[p_gain,i_gain,dv_gain,de_gain]+sat_data
        
        self.write_registers(PC_PGAIN , data)
        self.write_registers(CTRL_REG_1 , 1024) #Apply tuning
        
    def autozero(self, force: int=30, exit_mode: int=1, trigger:bool=True):
        # Check if variables are valid
        if not (isinstance(exit_mode, int) and exit_mode in [1, 2, 3, 4, 5]):
            print("Error: Invalid exit mode. Must be 1: sleep, 2: force, 3: position,4: Haptic,5:Kinematic")
            return
        
        if not (isinstance(force, int) and force>=0):
            print("Error: Invalid force, must be a positive force below 800.")
            return
        
        self.write_registers(ZERO_MODE,[2, force, exit_mode])
        
        if trigger:
            self.write_registers(MODE_Reg,AutoZeroMode)
            while self.mode == 55:
                time.sleep(0.01) #Slow down loop while waiting for autozero to complete
        


    """ NESTED HAPTICS OBJECT """
    class _HapticMode:
        def __init__(self, actuator):
            self.actuator = actuator #Allows use of parent class methods in nested object
            # Initialize haptic properties
            self._softstart = None #Set as both property and setter
            
        @property
        def softstart(self):
            self._softstart=self.actuator.read_register(HAPTIC_SOFTSTART, 1)[0]
            return self._softstart
        
        @softstart.setter
        def softstart(self, time_ms:int):
            self.actuator.write_registers(HAPTIC_SOFTSTART,time_ms)

        def enable(self):
            """Enable Haptics"""
            self.actuator.write_registers(MODE_Reg, HapticMode)
            
        """ HAPTIC EFFECTS """
        def set_spring(self, ID:int, gain:int, center:int, deadzone:int, saturation: int=0, coupling: int=0, enable: bool=None):
            """Set spring components (A,B, or C). Can enable the spring optionally as well"""

            # Check if variables are valid
            if not (isinstance(ID, int) and ID in [0, 1, 2]):
                print("Error: Invalid spring ID. Must be 0, 1, or 2.")
                return
            
            if not (isinstance(coupling, int) and coupling in [0, 1, 2]):
                print("Error: Invalid coupling value. Must be 0, 1, or 2.")
                return
        
            # Check if all values are positive integers
            if not all(isinstance(x, int) and x >= 0 for x in [gain, center, deadzone, saturation]):
                print("Error: All values must be positive integers.")
                return
    
            # Constructing message
            centerLH = self.actuator._int32_to_u16(center)
            data = [gain] + centerLH + [coupling, deadzone, saturation]
            self.actuator.write_registers(int(SPRING_1 + ID * 6), data)  # setting spring parameters
            
            if enable!=None: # Set enable of spring if actually set
                self.toggle_spring(ID, enable)
        
        def toggle_spring(self, ID:int, enable: bool=True):
            """Enable spring ID to True or False"""
            effect_bits=self.actuator.read_register(HAPTIC_STATUS,1)[0]
            if enable == True:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits | (1 << (1 + ID)))
            else:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits & ~(1 << (1 + ID)))
                
        def set_oscillator(self, ID:int, gain:int, osctype:int, freq:int, duty:int, enable: bool=None):
            """Set oscilaltor components (A, or B). Can enable the effect optionally as well"""
            
            # Check if variables are valid
            if not (isinstance(ID, int) and ID in [0, 1]):
                print("Error: Invalid oscillator ID. Must be 0, or 1.")
                return
            
            if not (isinstance(osctype, int) and osctype in [0, 1, 2, 3]):
                print("Error: Invalid coupling value. Must be 0 (square), 1(sine), 2(triangle), or 3(saw).")
                return
        
            # Check if all values are positive integers
            if not all(isinstance(x, int) and x >= 0 for x in [gain, freq, duty]):
                print("Error: All values must be positive integers.")
                return
    
            # Constructing message
            data = [gain, osctype, freq, duty]
            self.actuator.write_registers(int(OSCILLATOR_1 + ID * 4), data)  # setting parameters
            
            if enable!=None: # Set enable of oscillator if actually set
                self.toggle_oscillator(ID, enable)
        
        def toggle_oscillator(self, ID:int, enable: bool=True):
            """Enable oscillator ID to True or False"""
            effect_bits=self.actuator.read_register(HAPTIC_STATUS,1)[0]
            if enable == True:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits | (1 << (6 + ID)))
            else:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits & ~(1 << (6 + ID)))
                
        def set_force(self, gain:int, enable: bool=None):
            """Set constant force. Can enable the force optionally as well"""
        
            # Check if gain is integer
            if not isinstance(gain, int):
                print("Error: Gain must be an integer")
                return
    
            # Constructing message
            data = self.actuator._int32_to_u16(gain)
            self.actuator.write_registers(CONSTANT_FORCE_MN, data)  # setting parameters
            
            if enable!=None: # Set enable of force if actually set
                self.toggle_force(enable)
        
        def toggle_force(self, enable: bool=True):
            """Enable force to True or False"""
            effect_bits=self.actuator.read_register(HAPTIC_STATUS,1)[0]
            if enable == True:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits | (1 << (0)))
            else:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits & ~(1 << (0)))
                 
        def set_damper(self, gain:int, enable: bool=None):
            """Set damper. Can enable the damper optionally as well"""
        
            # Check if gain is integer
            if not isinstance(gain, int):
                print("Error: Gain must be an integer")
                return
    
            # Constructing message
            self.actuator.write_registers(D0_GAIN_NS_MM, gain)  # setting parameters
            
            if enable!=None: # Set enable of damper if actually set
                self.toggle_damper(enable)
        
        def toggle_damper(self, enable: bool=True):
            """Enable damper to True or False"""
            effect_bits=self.actuator.read_register(HAPTIC_STATUS,1)[0]
            if enable == True:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits | (1 << (4)))
            else:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits & ~(1 << (4)))
                
        def set_inertia(self, gain:int, enable: bool=None):
            """Set inertia. Can enable the inertia optionally as well"""
        
            # Check if gain is integer
            if not isinstance(gain, int):
                print("Error: Gain must be an integer")
                return
    
            # Constructing message
            self.actuator.write_registers(I0_GAIN_NS2_MM, gain)  # setting parameters
            
            if enable!=None: # Set enable of inertia if actually set
                self.toggle_inertia(enable)
        
        def toggle_inertia(self, enable: bool=True):
            """Enable damper to True or False"""
            effect_bits=self.actuator.read_register(HAPTIC_STATUS,1)[0]
            if enable == True:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits | (1 << (5)))
            else:
                self.actuator.write_registers(HAPTIC_STATUS, effect_bits & ~(1 << (5)))
                                     
        def toggle_effects(self, f: bool=False, s0: bool=False, s1: bool=False, 
                           s2: bool=False, d: bool=False, i: bool=False, 
                           o1: bool=False, o2: bool=False)  :
            """Take booleans of the haptic effects to set value"""
            array=[o2,o1,i,d,s2,s1,s0,f]
            data=int("".join(["01"[i] for i in array]), 2)
            self.actuator.write_registers(HAPTIC_STATUS, data)
                
            
    """ NESTED KINEMATICS OBJECT """
    class _KinematicMode:
        def __init__(self, actuator):
            self.actuator = actuator #Allows use of parent class methods in nested object
            # Initialize kinematic properties
            self._motion = None #Set as both property and setter
            self._status= None #Status of the kinematic mode (idle or running)
            self._home = 0 #Home motion
            
        @property
        def motion(self):
            self._motion=self.actuator.read_register(KINEMATIC_STATUS, 1)[0] & 0x7FFF #Bitmask to remove last bit
            return self._motion
        
        @motion.setter
        def motion(self, ID:int):
            self.enable()
            self.actuator.write_registers(KIN_SW_TRIGGER,ID)
            
        @property
        def status(self):
            self._status=bool((self.actuator.read_register(KINEMATIC_STATUS, 1)[0]& 0x8000) // 32768) #Bitmask, divide by 32768
            return self._status
        
        @property
        def home(self):
            self._home=self.actuator.read_register(KIN_HOME_ID, 1)[0]
            return self._home
        
        @motion.setter
        def home(self, ID:int):
            self.enable()
            self.actuator.write_registers(KIN_HOME_ID ,ID)
            
        def enable(self):
            """Enable Kinematics"""
            self.actuator.write_registers(MODE_Reg, KinematicMode)
            
        """ KINEMATIC MOTIONS """            
        def set_motion(self,ID:int,position:int,time:int,delay:int,nextID:int,autonext:int,motion_type:int=0):
            """Set parameters of motion based on ID"""
            # Check if variables are valid
            if not (isinstance(motion_type, int) and motion_type in [0, 1]):
                print("Error: Invalid motion type. Must be 0, or 1.")
                return
            
            if not (isinstance(autonext, int) and autonext in [0, 1]):
                print("Error: Invalid autonext value. Must be 0, or 1.")
                return
            
            if not (isinstance(nextID, int) and nextID <= 31 and nextID>= 0):
                print("Error: Next ID must be from 0 t0 31")
                return
        
            # Check if all values are positive integers
            if not all(isinstance(x, int) and x >= 0 for x in [position, time, delay]):
                print("Error: All values must be positive integers.")
                return
            
            positionLH = self.actuator._int32_to_u16(position)
            timeLH = self.actuator._int32_to_u16(time)
            combined=(nextID << 3) + (motion_type << 1) + autonext
            data=positionLH+timeLH+[delay,combined]
            
            self.actuator.write_registers(KIN_REGISTER_0+ID*6,data)
            
        