import cv2
from utils import activateMachine as act


def select_bbox(color_image, sub_mask):
	es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
	th = cv2.threshold(sub_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
	eroded = cv2.erode(th, es, iterations=5)
	dilated = cv2.dilate(eroded, es, iterations=1)  # 形态学
	# eroded = cv2.erode(dilated, es, iterations=1)
	contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# 测试时候数据，area data 两个在一起的时候121870.0  116416.0 两个单件 (16654.0  35806.5)
	# (25006.5 41712.5)
	# 逻辑是：判断下是否是大件，如果是大件大于一个面积的阈值则直接位单件，如果不是的话，则计算其中有多少个轮廓距，
	# 矩阵可能相互交联，如是两个矩阵，则直接位并排件，如果位一个矩阵，则考虑分析他的深度有没有变化很大。
	count_small = 0
	count = 0  # for counting the times of identifying a contour
	pack_area = []
	for c in contours:
		count += 1
		area = cv2.contourArea(c)
		# for testing, showing the real time area data
		print('area data', area)
		if area >= 75000:
			(x, y, w, h) = cv2.boundingRect(c)
			# test for showing contours in the raw image
			cv2.rectangle(color_image, (x, y), (x + w, y + h), (255, 255, 0), 2)
			pack_area = [y, y + h, x, x + w]

		elif 15000 < area < 75000:
			count_small += 1
			if count_small >= 2:
				act.act_machine()
				print('count', count_small)
			(x, y, w, h) = cv2.boundingRect(c)
			# test for showing contours in the raw image
			cv2.rectangle(color_image, (x, y), (x + w, y + h), (255, 255, 0), 2)
			pack_area = [y, y + h, x, x + w]

		else:
			# print('no packages')
			continue
	return pack_area, count
