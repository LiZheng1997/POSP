import numpy as np


# coordination
def depth_tool(depth, area):
	area_y = area[1] - area[0]
	area_x = area[3] - area[2]
	# depth_data = np.random.rand(area_y, area_x)
	# depth_data = np.zeros(area_y, area_x)
	depth_data = np.empty((area_y, area_x))
	# depth_data = (area_y, area_x)
	# depth_data = np.array()
	star_y = area[0]
	star_x = area[2]

	for y in range(area[0], area[1]):
		for x in range(area[2], area[3]):
			# np.append(depth_data, depth.get_distance(x, y))

			# cannot change the sequence of the get distance.
			depth_data[y-star_y][x-star_x] = depth.get_distance(x, y)
	return depth_data, area_y, area_x
