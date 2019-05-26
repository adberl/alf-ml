from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense

import numpy as np
import pybullet as p
import pybullet_data

from goodbot import Goodbot
from road_pi import Road

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
phyCl = p.connect(p.GUI) # SETTING UP THE ENVIRONMENT
p.setAdditionalSearchPath(pybullet_data.getDataPath())

plane = p.loadURDF("plane.urdf") # load the plane
p.setGravity(0, 0, -10) # set gravity
p.setRealTimeSimulation(1)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" a road point is 0.3x0.3 coordinates big"""

p.resetDebugVisualizerCamera(25, 0, -89.9, [0, 0, 0])

road = Road('road/blender_road.txt')
robot = Goodbot("goodbot/goodbot.urdf", road.fetchStart() + [0.3])

p.setRealTimeSimulation(1)

velocity = 30
force = 100
p.setGravity(0, 0, -30)

json_file = open('keras/model.json', 'r')
model = json_file.read()
json_file.close()

model = model_from_json(model)

model.load_weights('keras/model.h5')

robot.go_forward(velocity, force)

while 1:

	inputArray = road.serveNet(robot)
#	print(inputArray)
	inputArray = np.reshape(inputArray, (inputArray.shape[0], 1, inputArray.shape[1]))
#	print(inputArray)
	prediction = model.predict(inputArray)
#	print(prediction) # right, left, forwards, backwards

	robot.turn_ahead()
	print(prediction[0][0], prediction[0][1], prediction[0][2])

	if(prediction[0][0] >= 0.7 or prediction[0][1] >= 0.7):
		if(prediction[0][0] > prediction[0][1]):
			robot.turn_right()
		else:
			robot.turn_left()
