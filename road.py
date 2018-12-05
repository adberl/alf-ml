import pybullet as p
from rtree import index
from goodbot import Goodbot

import numpy as np

class Road:

	idx_prop = index.Property()
	idx = index.Index(properties = idx_prop)
	road_points_list = [] # list of lists, contains lists of 3 floats of coordinates

	def __init__(self, road_path: str, visualize=True):  #road_path is the relative path to the road text file which contains the coords;
		road_file = open(road_path, 'r')
		self.number = int(road_file.readline())
		file_coords = road_file.readlines()

		idx_id = 0
		for i in file_coords:
			coords = i.split(' ')
			rp_x = float(coords[0])
			rp_y = float(coords[1])
			rp_half = 0.15

			self.idx.insert(idx_id, ((rp_x - rp_half), (rp_y - rp_half), (rp_x + rp_half), (rp_y + rp_half)))
			self.road_points_list.append([rp_x, rp_y])
			if visualize: p.loadURDF("road/road_point.urdf", [rp_x, rp_y, 0.1] )
			idx_id += 1

	def serveNet(self, bot: Goodbot, start_sensor=0, end_sensor=6) -> np.array:

		sens_pos = bot.sensors_pos()
		data_array = []
		
		for i in range(start_sensor, end_sensor):
			rdpt_id = list(self.idx.nearest((sens_pos[i][0], sens_pos[i][1]), 1))[0]
			
			xsq = (sens_pos[i][0] - self.road_points_list[rdpt_id][0])**2		
			ysq = (sens_pos[i][1] - self.road_points_list[rdpt_id][1])**2		
			dist = np.sqrt(xsq + ysq)

			data_array.append(dist)
		
		return np.array(data_array).reshape(1, -1)
		

	def sensors_output(self, bot: Goodbot) -> list:
		sensors = bot.sensors_pos()
		closest_id = []
		for sens_pos in sensors:
			closest_id.append(list(self.idx.nearest((sens_pos[0], sens_pos[1]), 1))[0])

		return closest_id

	def fetchStart(self) -> list:
		return [self.road_points_list[0][0], self.road_points_list[0][1]]
