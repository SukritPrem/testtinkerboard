import sys
import time
import serial


def ReadSensor():

    try:

        #         print ("Device 1")
        #         t = serial.Serial("/dev/ttyS0",9600)
        #         n = t.write(b'\x01\x04\x00\x01\x00\x02\x20\x0B')
        print("Device 1")
        t = serial.Serial("/dev/ttyS0", 9600, timeout=2)
        n = t.write(b'\x01\x04\x00\x01\x00\x02\x20\x0B')
        print('++++++++++++++++++++')
        time.sleep(3)
    except IndexError:
        print("Device 1: Outdoor Temp/RH cann't get data")
        print("******************")
        time.sleep(6)


#     try:
#
#         GPIO.output(4, False)
#         GPIO.output(17, False)
#         GPIO.output(18, False)
#         GPIO.output(27, False)
#         GPIO.output(22, False)
#
#
#         GPIO.output(20, False)
#         GPIO.output(21, False)
#         GPIO.output(23, False)
#         GPIO.output(24, False)
#
# #         print ("Device 1")
# #         t = serial.Serial("/dev/ttyS0",9600)
# #         n = t.write(b'\x01\x04\x00\x01\x00\x02\x20\x0B')
#         print ("Device 1")
#         t = serial.Serial("/dev/ttyS0",9600, timeout = 2 )
#         n = t.write(b'\x01\x04\x00\x01\x00\x02\x20\x0B')
#
#
#         str = t.read(n)
#         str.hex()
#         a=str.hex()
#         print("Data get form sensor : ",a)
#         b=a.split('010404')  #Device0
#
#         #print(b)
#         int(b[1],16)
#
#         c=b[1]
#         c[:4]
#         int(c[:4],16)
#
#
#         tempd1=int(c[:4],16)/10
#         print("Temperature D1:",tempd1) ####
#
#         c[4:8]
#         int(c[4:8],16)
#         humid1=int(c[4:8],16)/10
#         print("Humidity D1:",humid1)  #####
#
#         time.sleep(1)
#
#         GPIO.output(4, True)
#         GPIO.output(17, True)
#         GPIO.output(18, True)
#         GPIO.output(27, True)
#         GPIO.output(22, True)
#
#         GPIO.output(20, True)
#         GPIO.output(21, True)
#         GPIO.output(23, True)
#         GPIO.output(24, True)
#         print('++++++++++++++++++++')
#         time.sleep(3)
#     except IndexError:
#         print ("Cann't get data")
#         print ("******************")
#         time.sleep(6)
