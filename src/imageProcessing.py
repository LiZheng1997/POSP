import cv2


def image_processing(color_image):
	# select a area we want to detect packages
	roi_image = color_image[60:480, 200:480]  # change the roi when needed

	# blurring the image to take out noisy
	color_image = cv2.GaussianBlur(roi_image, (5, 5), 15)
	# erode the image to take out unnecessary blocks

	# covert the image to gray
	color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
	return color_image
