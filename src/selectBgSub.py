import cv2

def select_bg_sub(mode):

	if mode == 0:
		backsub = cv2.createBackgroundSubtractorMOG2()
	elif mode == 1:
		backsub = cv2.createBackgroundSubtractorKNN()
	else:
		print('no matching value in this program.')
		return 0
	return backsub