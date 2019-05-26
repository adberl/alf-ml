#from keras.models import Sequential
#from keras.models import model_from_json
#from keras.layers import Dense

import numpy as np
import RPi.GPIO as GPIO

#loading model
"""
json_file = open('keras/model.json', 'r')
model = json_file.read()
json_file.close()

model = model_from_json(model)

model.load_weights('keras/model.h5')
"""
#loading model done

#setting up GPIO

GPIO.setmode(GPIO.BCM)
chan_list = [4, 17, 27, 22, 13, 26]
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

outpin_list = [18, 24, 25, 12]
GPIO.setup(outpin_list, GPIO.OUT)

while 1:

	inputArray = []
	for i in chan_list:
		inputArray.append(GPIO.input(i))

	#input array example: [[[2.02718298 2.02750389 2.6589112  2.65972677 2.62878356 2.63189203]]]
	inputArray = [[inputArray]]
	print(inputArray)
	prediction = model.predict(np.asarray(inputArray))
	print(prediction[0][0], prediction[0][1], prediction[0][2])

	if(prediction[0][0] >= 0.2 or prediction[0][1] >= 0.2):
		if(prediction[0][0] > prediction[0][1]): #turn right
			GPIO.output([18, 25, 12], GPIO.LOW)
			GPIO.output(24, GPIO.HIGH)
		else: #turn left
			GPIO.output([18, 25, 12], GPIO.LOW)
			GPIO.output(12, GPIO.HIGH)
	else:
		GPIO.output([12, 24], GPIO.HIGH)

GPIO.cleanup()
