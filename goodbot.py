import pybullet as p

class Goodbot:

	start_joint_id = 2
	nr_of_sensors = 6

	def __init__(self, bot_path: str, spawn_coords: list, start_sensor_id=2, end_sensor_id=8): #bot_path is a string; coords is a list of 3 floats (spawn coords)
		""" We instantiate the bot with the path to its urdf + a road object which the sensors will read off of """
		self.start_sensor_id = start_sensor_id
		self.end_sensor_id = end_sensor_id
		self.bot = p.loadURDF(bot_path, spawn_coords, globalScaling=0.5) # loads the bot in as a self.bot
		p.setJointMotorControl2(self.bot, 9, controlMode = p.VELOCITY_CONTROL, targetVelocity = 0, force = 0) #unblocks the front wheels
		p.setJointMotorControl2(self.bot, 10, controlMode = p.VELOCITY_CONTROL, targetVelocity = 0, force = 0)

		for current in range(self.start_sensor_id, self.end_sensor_id):
			p.changeVisualShape(self.bot, current, rgbaColor=[0, 0, 1, 1])
			print(current)


	def go_forward(self, vel, force):
		""" vel is the velocity of the wheels (speed); force is the force used to get the wheels to spin that fast """
		p.setJointMotorControl2(self.bot, 0, controlMode = p.VELOCITY_CONTROL, targetVelocity = -vel, force = force)
		p.setJointMotorControl2(self.bot, 1, controlMode = p.VELOCITY_CONTROL, targetVelocity = -vel, force = force)

	def turn_right(self):
 		p.setJointMotorControl2(self.bot, 8, p.POSITION_CONTROL, targetPosition=-0.7854) #turns the front wheels by -45 degrees

	def turn_left(self):
 		p.setJointMotorControl2(self.bot, 8, p.POSITION_CONTROL, targetPosition=0.7854) #turns the front wheels by +45 degrees

	def turn_ahead(self):
		p.setJointMotorControl2(self.bot, 8, p.POSITION_CONTROL, targetPosition=0) #resets the front wheel

	def sensors_pos(self) -> list:
		sensors_pos = []
		for current in range(self.start_sensor_id, self.end_sensor_id):
			sensors_pos.append(p.getLinkState(self.bot, current)[0])
		return sensors_pos

	def sensors_pos_string(self) -> list:
		sensors_pos = []
		for current in range(self.start_sensor_id, self.end_sensor_id):
			sensors_pos.append(p.getLinkState(self.bot, current)[0][0])
			sensors_pos.append(p.getLinkState(self.bot, current)[0][1])
		return sensors_pos
	def sensor_color(self, sensorid, red, green, blue):
		p.changeVisualShape(self.bot, sensorid, rgbaColor=[red, green, blue, 1])
