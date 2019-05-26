import math

road_points_list = [] # list of lists, contains lists of 3 floats of coordinates

road_file = open('road/blender_road.txt', 'r')
roadpts_count = int(road_file.readline())
file_coords = road_file.readlines()

processed_file = open('data/processed_data_pi.txt', 'w')

ref_distance = 0.36

for i in file_coords:

	coords = i.split(' ')
	rp_x = float(coords[0])
	rp_y = float(coords[1])
	road_points_list.append([rp_x, rp_y])

# we're doing the math after we have all the data, rather than on the fly because my old laptop couldn't handle that
print('processing the file ...')
total = 0
with open('data/training_data.txt') as training_file:
	for line in training_file:
		if len(line.strip()) == 0:
			continue
		line_split = line.split(' ')
		tempstr = ''

		for i in range(0,6):
			total += 1
			rdpt_id = int(line_split[i])
			sensor_x = float(line_split[2*i+6])
			sensor_y = float(line_split[2*i+7])
			distance = math.sqrt( (sensor_x-road_points_list[rdpt_id][0])**2 + (sensor_y-road_points_list[rdpt_id][1])**2 )
			tempstr += ("0" if distance >  ref_distance else "1") + ' '
		tempstr += line_split[18] + ' ' + line_split[19].rstrip('\n') + ' ' + ('1' if line_split[18] == line_split[19].rstrip('\n') else '0') + '\n'
		processed_file.write(tempstr)
print('processed {} lines of data'.format(total/6))
