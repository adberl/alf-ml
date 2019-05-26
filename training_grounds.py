import pybullet as p
import pybullet_data
from goodbot import Goodbot
from threading import Timer
from road_pi import Road

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
phyCl = p.connect(p.GUI) # SETTING UP THE ENVIRONMENT
p.setAdditionalSearchPath(pybullet_data.getDataPath())

plane = p.loadURDF("plane.urdf") # load the plane
p.setGravity(0, 0, -10) # set gravity
p.setRealTimeSimulation(1)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#road_file = open('blender_road.txt', 'r')
#file_coords = road_file.readlines()
#idx = index.Index()



#for i in file_coords:
#	coords = i.split(' ')
#	p.loadURDF("road_point.urdf", [float(coords[0]), float(coords[1]), 0.1] )

""" a road point is 0.3x0.3 coordinates big"""

#p.loadURDF("road_point.urdf", [0, 0, 0.1] )
#p.loadURDF("road_point.urdf", [0.3, 0.3, 0.1] )

p.resetDebugVisualizerCamera(25, 0, -89.9, [0, 0, 0])

road = Road('road/blender_road.txt')
robot = Goodbot("goodbot/goodbot.urdf", road.fetchStart() + [0.3])

p.setRealTimeSimulation(1)

rarr = p.B3G_RIGHT_ARROW
larr = p.B3G_LEFT_ARROW
uarr = p.B3G_UP_ARROW
darr = p.B3G_DOWN_ARROW

velocity = 30
force = 100
p.setGravity(0, 0, -30)

""" output variables """
save_length = 0
outputs_size = 22
write_list = []
file = open('data/training_data.txt', 'a')
""""""""""""""""""""""""

iteration = 0
WRITE_FREQ = 1000

while 1:
	"""  outputs  """
	is_right = 0
	is_left = 0
	is_forward = 0
	is_backward = 0
	""""""""""""""""""

	kin = p.getKeyboardEvents()

	if 120 in kin.keys() and kin[120] == p.KEY_IS_DOWN:
		file.close()
		break
	if rarr in kin.keys() and kin[rarr] == p.KEY_IS_DOWN:
		robot.turn_right()
		is_right = 1
	elif larr in kin.keys() and kin[larr] == p.KEY_IS_DOWN:
		robot.turn_left()
		is_left = 1
	else:
		robot.turn_ahead()
	if uarr in kin.keys() and kin[uarr] == p.KEY_IS_DOWN:
		robot.go_forward(velocity, force)
		is_forward = 1
	elif darr in kin.keys() and kin[darr] == p.KEY_IS_DOWN:
		robot.go_forward(-velocity, force)
		is_backward = 1
	else:
		robot.go_forward(0, 0)

	iteration += 1

	if iteration % WRITE_FREQ == 0:
		write_list = road.sensors_output(robot) + robot.sensors_pos_string() + [is_right, is_left]
		if is_forward == 0:
			continue

		print(*write_list, sep=' ', file=file)
		print('write #{}'.format(iteration/1000))

print('done')
