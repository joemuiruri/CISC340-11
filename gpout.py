import RPi.GPIO as GPIO
import sys
import time

def deactivateAlarm():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    chan_list = [4, 17, 18, 23] 
    GPIO.setup(chan_list, GPIO.OUT)
    GPIO.output(chan_list, (True, False, False, False)) #setting alarm termination signal to basys3

    time.sleep(2) #waiting 2 seconds guarantees basys3 receives termination signal

    GPIO.output(chan_list, (False, False, False, False)) #resetting signal
    GPIO.cleanup()
