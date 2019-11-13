import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

chan_list = [14, 15, 18, 23]

GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(chan_list, (False, False, False, False))
time.sleep(3)

GPIO.output(chan_list, (True, False, False, False))
time.sleep(3)

GPIO.output(chan_list, (False, False, False, False))
GPIO.cleanup()
