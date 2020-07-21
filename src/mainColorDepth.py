import pyrealsense2 as rs
import cv2
import numpy as np
from src import selectBgSub as sbs, imageProcessing as ip, selectBbox as sb, judgeCoreArea as jca
from utils import calculateDepthTool as cdt, plotDepthModel as pdm, showImages as si


def main(pipeline, height, width, clipping_distance, align):
	# Create colorizer object
	colorizer = rs.colorizer()
	# initiate the backsubtractor
	backsub = sbs.select_bg_sub(0)
	# bbox = np.zeros()
	# roi_image = []
	try:
		while True:
			# Wait for a coherent pair of frames: depth and color
			frames = pipeline.wait_for_frames()

			# Align the depth frame to color frame
			aligned_frames = align.process(frames)

			# Get aligned frames
			depth_frame = aligned_frames.get_depth_frame()  # aligned_depth_frame is a 640x480 depth image
			color_frame = aligned_frames.get_color_frame()

			# depth_frame = frames.get_depth_frame()
			# color_frame = frames.get_color_frame()
			if not depth_frame or not color_frame:
				continue

			# Convert images to numpy arrays
			color_image = np.asanyarray(color_frame.get_data())
			# Convert depth_frame to numpy array to render image in opencv
			depth_image = np.asanyarray(depth_frame.get_data())
			# print('depth image', depth_frame.size)

			# change the image to bgr if the raw one is bgr format
			bgr_image = cv2.cvtColor(color_image.copy(), cv2.COLOR_RGB2BGR)
			bgr_image = ip.image_processing(bgr_image)

			sub_mask = backsub.apply(bgr_image)
			area, count = sb.select_bbox(bgr_image, sub_mask)
			area = np.array(area)

			if area.size is not 0:
				tag = jca.judge_core_area(bgr_image, area)
				if tag:  # and count >= 3
					print('area----->', area)
					crop_raw_area = np.array([area[0] + 50, area[1] + 70, area[2] + 190, area[3] + 210])
					raw_area = np.array([area[0] + 60, area[1] + 60, area[2] + 200, area[3] + 200])

					roi_image = bgr_image[area[0]:area[1], area[2]:area[3]]
					# cv2.imshow('roi image ', roi_image)
					# get the depth data of each pixel
					# Colorize depth frame to jet colormap
					depth_color_frame = colorizer.colorize(depth_frame)
					depth_color_image = np.asanyarray(depth_color_frame.get_data())
					crop_depth_image = depth_color_image[crop_raw_area[0]:crop_raw_area[1],
					                   crop_raw_area[2]:crop_raw_area[3]]
					# crop_depth_image = depth_color_image[raw_area[0]:raw_area[1], \
					#                    raw_area[2]:raw_area[3]]
					# cv2.imshow('crop depth image', crop_depth_image)

					depth_set, cord_y, cord_x = cdt.depth_tool(depth_frame, raw_area)

					images = si.ManyImgs(0.4, ([color_image, bgr_image], [roi_image, crop_depth_image],
					                           [color_image, sub_mask]))  #
					cv2.namedWindow('Integrated Images', cv2.WINDOW_AUTOSIZE)
					cv2.imshow('Integrated Images', images)
					pdm.plt_depth_model(depth_set, cord_y, cord_x)

					key = cv2.waitKey(1)
					if key == 27:
						cv2.destroyAllWindows()
						break

			# Colorize depth frame to jet colormap
			depth_color_frame = colorizer.colorize(depth_frame)
			depth_color_image = np.asanyarray(depth_color_frame.get_data())

			# Apply colormap on depth image (image must be converted to 8-bit per pixel first)
			depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

	# Stack both images horizontally
	# images = np.hstack((depth_colormap, color_image))

	# Show images for testing
	# cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
	# cv2.imshow('RealSense', images)
	# cv2.imshow('depth image', depth_color_image)
	# cv2.imshow('depth color image', depth_colormap)
	# cv2.imshow('raw color image', color_image)
	# cv2.imshow('bgr image', bgr_image)
	# cv2.imshow('background subtraction', sub_mask)
	finally:
		# Stop streaming
		pipeline.stop()
