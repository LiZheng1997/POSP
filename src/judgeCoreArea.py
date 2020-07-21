import cv2
# judging the area in a image whether or not packages are in the middle of the camera view


def judge_core_area(image, area):
	flag = False
	# print(image.shape)
	height, width = image.shape
	# print((0, int(height / 4)), (width, int(3 / 4 * height)))
	h = area[1] - area[0]
	w = area[3] - area[2]
	core_point = [area[2] + int(w / 2), area[0] + int(h / 2)]
	cv2.rectangle(image, (int(width/4), int(height / 4)), (int(3 / 4 * width), int(3 / 4 * height)), (255, 255, 255), 1)
	if int(height / 4) < core_point[1] < int(3 / 4 * height) and int(width/4) < core_point[0] < int(3 / 4 * width):
		print('in the core area', core_point)
		flag = True
	return flag
