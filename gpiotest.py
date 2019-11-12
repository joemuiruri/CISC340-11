import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

chan_list = [14, 15, 18]

GPIO.setup(chan_list, GPIO.OUT)

for i in range(1, 10):
	GPIO.output(chan_list, GPIO.LOW)
	sleep(1)
	GPIO.output(chan_list, GPIO.HIGH)
	sleep(1)

GPIO.output(chan_list, GPIO.LOW)

GPIO.cleanup()
