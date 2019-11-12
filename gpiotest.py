import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

chan_list = [14, 15, 18]

GPIO.setup(chan_list, GPIO.OUT)

GPIO.output(chan_list, GPIO.LOW)

for i in range(0, 3):
	print("GPIO Output test: pin " + str(chan_list[i]))
	
	GPIO.output(chan_list[i], GPIO.HIGH)
	time.sleep(3)
	GPIO.output(chan_list[i], GPIO.LOW)

GPIO.cleanup()
