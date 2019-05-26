import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
chan_list = [4, 13, 17, 22, 26, 27]
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		inputArray = []
		for i in chan_list:
			inputArray.append(GPIO.input(i))

		print(inputArray)
		time.sleep(1)
except KeyboardInterrupt:
	print("Measurement stopped by User")
	GPIO.cleanup()