import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

chan_list = [14, 15, 18]

GPIO.setup(chan_list, GPIO.OUT)

for i in range(1, 6):
	if(sys.argv[i] == 0):
		GPIO.output(chan_list, (GPIO.LOW, GPIO.LOW, GPIO.LOW))
	elif(sys.argv[i] == 1):
		GPIO.output(chan_list, (GPIO.LOW, GPIO.LOW, GPIO.HIGH))
	elif(sys.argv[i] == 2):
		GPIO.output(chan_list, (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
	elif(sys.argv[i] == 3):
		GPIO.output(chan_list, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
	elif(sys.argv[i] == 4):
		GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW, GPIO.LOW))
	elif(sys.argv[i] == 5):
		GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
	elif(sys.argv[i] == 6):
		GPIO.output(chan_list, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
	elif(sys.argv[i] == 7):
		GPIO.output(chan_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

	time.sleep(0.1)


GPIO.cleanup()
