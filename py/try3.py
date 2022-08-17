# Importing Libraries
import serial
import time
arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=115200, timeout=.1)
a = 1
def write_read(x):
    arduino.write(bytes(str(a), 'utf-8'))
    arduino.write(bytes(str(a), 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    a = a + 1
    value = write_read(a)
    print(value) # printing the value
    time.sleep(0.1)


