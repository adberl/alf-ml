import argparse

parser = argparse.ArgumentParser(description='Scales your road to fit within the map boundaries.')

parser.add_argument('-i', action='store', required=True, help='Input file, first line must contain the number of coordinates', dest='input_file')
parser.add_argument('-o', action='store', required=True, help='Output file, will contain scaled road', dest='output_file')

parsed_arguments = parser.parse_args()

road_file = open(parsed_arguments.input_file, 'r')
new_road_file = open(parsed_arguments.output_file, 'w')

nr_nodes = road_file.readline()
new_road_file.write(nr_nodes)

file_coords = road_file.readlines()

min_x = float('inf')
max_x = -min_x
min_y = float('inf')
max_y = -min_y

list_coords = []

for coordinates in file_coords:
	
	coord = [float(item) for item in coordinates.split(' ')]
	
	list_coords.append(coord)
	
	min_x = min(min_x, coord[0])
	max_x = max(max_x, coord[0])
	
	min_y = min(min_y, coord[1])
	max_y = max(max_y, coord[1])
	

x_origin = (min_x + max_x) / 2
y_origin = (min_y + max_y) / 2

scale_x = 14 / (max_x - x_origin)
scale_y = 14 / (max_y - y_origin)

for coord in list_coords:
	coord[0] = coord[0] - x_origin # centering x
	coord[1] = coord[1] - y_origin # centering y

	coord[0] *= scale_x
	coord[1] *= scale_y
	
	writestring = "{} {}\n".format(coord[0], coord[1])
	new_road_file.write(writestring)

new_road_file.close()
road_file.close()
