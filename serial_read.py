#!/usr/bin/env python
import time
import serial
import gpout

ser = serial.Serial(
	port = '/dev/ttyUSB1',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
    ins = ser.readline()
    processedins = str(ins)[2]
    print(processedins)
    #TODO: replace the following with the proper procedure for handling alarm signal
    if(processedins == '1'):
        gpout.deactivateAlarm()
