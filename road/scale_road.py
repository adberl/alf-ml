road_file = open('blender_road.txt.old', 'r')
new_road_file = open('blender_road.txt', 'w')
nr_nodes = road_file.readline()

new_road_file.write(nr_nodes)

file_coords = road_file.readlines()

min_x = +100
max_x = -100

min_y = +100
max_y = -100

list_coords = []

for coordinates in file_coords:
	
	coord = coordinates.split(' ')
	coord[0] = float(coord[0]) # x coord
	coord[1] = float(coord[1]) # y coord
	
	list_coords.append(coord)
	
	min_x = min(min_x, coord[0])
	max_x = max(max_x, coord[0])
	
	min_y = min(min_y, coord[1])
	max_y = max(max_y, coord[1])
	

x_origin = (min_x + max_x) / 2
y_origin = (min_y + max_y) / 2

scale_x = 14 / (max_x - x_origin) # maxx * scale = 14.5 -> scale = 14.5/maxx
scale_y = 14 / (max_y - y_origin)

for coord in list_coords:
	coord[0] = coord[0] - x_origin # centering x
	coord[1] = coord[1] - y_origin # centering y

	coord[0] *= scale_x
	coord[1] *= scale_y
	
	writestring = "{} {}\n".format(coord[0], coord[1])
	print(writestring)
	new_road_file.write(writestring)

	
new_road_file.close()
road_file.close()
