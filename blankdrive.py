import pybullet as p
import pybullet_data
from goodbot import Goodbot
from threading import Timer
from road import Road

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
phyCl = p.connect(p.GUI) # SETTING UP THE ENVIRONMENT
p.setAdditionalSearchPath(pybullet_data.getDataPath())

plane = p.loadURDF("plane.urdf") # load the plane
p.setGravity(0, 0, -10) # set gravity
p.setRealTimeSimulation(1) 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# BIG IMPORTANT!!!!!!
# a road point is 0.3x0.3 coordinates big

p.resetDebugVisualizerCamera(25, 0, -89.9, [0, 0, 0])

robot = Goodbot("goodbot/goodbot.urdf", [0, 0, 0])

rarr = p.B3G_RIGHT_ARROW
larr = p.B3G_LEFT_ARROW
uarr = p.B3G_UP_ARROW
darr = p.B3G_DOWN_ARROW

velocity = 30
force = 100
p.setGravity(0, 0, -30)


xSlider = p.addUserDebugParameter("positionx", -500, 500, 0)
ySlider = p.addUserDebugParameter("positiony", -500, 500, 0)

tile = p.loadURDF("road/road_point.urdf", [15, 15, 0.1] )

count = 0

while 1:

	if count == 1000:
		rp_x = p.readUserDebugParameter(xSlider)
		rp_y = p.readUserDebugParameter(ySlider)

		p.removeBody(tile)
		tile = p.loadURDF("road/road_point.urdf", [rp_x, rp_y, 0.1] )

	kin = p.getKeyboardEvents()

	if p.B3G_END in kin.keys() and kin[p.B3G_END] == p.KEY_IS_DOWN:
		file.close()
		break
	if rarr in kin.keys() and kin[rarr] == p.KEY_IS_DOWN:
		robot.turn_right()
	elif larr in kin.keys() and kin[larr] == p.KEY_IS_DOWN:
		robot.turn_left()
	else:
		robot.turn_ahead()
	if uarr in kin.keys() and kin[uarr] == p.KEY_IS_DOWN:
		robot.go_forward(velocity, force)
	elif darr in kin.keys() and kin[darr] == p.KEY_IS_DOWN:
		robot.go_forward(-velocity, force)
	else:
		robot.go_forward(0, 0)

