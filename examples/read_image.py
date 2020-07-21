import cv2 as cv

image = cv.imread('data/test_data/0003_Color.png')
# cv.namedWindow('RealSense', cv.WINDOW_AUTOSIZE)
cv.imshow('RealSense', image)

key = cv.waitKey()
if key == 27:
	cv.destroyAllWindows()