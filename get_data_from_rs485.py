"""
######################################################################

Simple Modbus Sensor Polling Code
Coded By "The Intrigued Engineer" over a coffee

Minimal Modbus Library Documentation
https://minimalmodbus.readthedocs.io/en/stable/

Thanks For Watching!!!

######################################################################
"""

import minimalmodbus  # Don't forget to import the library!!

mb_address = 1  # Modbus address of sensor

# Make an "instrument" object called sensy_boi (port name, slave address (in decimal))
sensy_boi = minimalmodbus.Instrument('COM7', mb_address)

sensy_boi.serial.baudrate = 9600				# BaudRate
sensy_boi.serial.bytesize = 8					# Number of data bits to be requested
# Parity Setting here is NONE but can be ODD or EVEN
sensy_boi.serial.parity = minimalmodbus.serial.PARITY_NONE
sensy_boi.serial.stopbits = 1					# Number of stop bits
sensy_boi.serial.timeout = 0.5					# Timeout time in seconds
# Mode to be used (RTU or ascii mode)
sensy_boi.mode = minimalmodbus.MODE_RTU

# Good practice to clean up before and after each execution
sensy_boi.clear_buffers_before_each_transaction = True
sensy_boi.close_port_after_each_call = True

# Uncomment this line to print out all the properties of the setup a the begining of the loop
# print(sensy_boi)

print("")
print("Requesting Data From Sensor...")  # Makes it look cool....

# NOTE-- Register addresses are offset from 40001 so inputting register 0 in the code is actually 40001, 3 = 40004 etc...

# Example of reading SINGLE register
# Arguments - (register address, number of decimals, function code, Is the value signed or unsigned)
# Uncomment to run this to just get temperature data

#single_data= sensy_boi.read_register(1, 1, 3, False)
#print (f"Single register data = {single_data}")

# Get list of values from MULTIPLE registers
# Arguments - (register start address, number of registers to read, function code)
data = sensy_boi.read_registers(0, 3, 3)
print(data)

# Piece of mind close out
sensy_boi.serial.close()
print("Ports Now Closed")
