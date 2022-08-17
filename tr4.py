import serial
import time
arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=115200, timeout=.1)
