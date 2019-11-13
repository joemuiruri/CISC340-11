import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

chan_list = (14, 15, 18, 23)

GPIO.setup(chan_list, GPIO.OUT)

for i in range(1, 6):
	if(sys.argv[i] == '0'):
		GPIO.output(chan_list, (False, False, False, False))
		print("outputting 0")
	elif(sys.argv[i] == '1'):
		GPIO.output(chan_list, (True, False, False, False))
		print("outputting 1")
	elif(sys.argv[i] == '2'):
		GPIO.output(chan_list, (False, True, False, False))
		print("outputting 2")
	elif(sys.argv[i] == '3'):
		GPIO.output(chan_list, (True, True, False, False))
		print("outputting 3")
	elif(sys.argv[i] == '4'):
		GPIO.output(chan_list, (False, False, True, False))
		print("outputting 4")
	elif(sys.argv[i] == '5'):
		GPIO.output(chan_list, (True, False, True, False))
		print("outputting 5")
	elif(sys.argv[i] == '6'):
		GPIO.output(chan_list, (False, True, True, False))
		print("outputting 6")
	elif(sys.argv[i] == '7'):
		GPIO.output(chan_list, (True, True, True, False))
		print("outputting 7")

	time.sleep(2)


GPIO.output(chan_list, (False, False, False, False))

GPIO.cleanup()
