import pyrealsense2 as rs
from utils import readBag as rb
from src import mainColorDepth as mcd

if __name__ == "__main__":
	# config the resolution depends on which platform you use.
	# 480x270 one raspberry pi, choose a suitable one for testing
	#
	w = 480  # 720  # 480
	h = 640  # 1280  # 640
	pipeline = rs.pipeline()
	config = rs.config()
	config.enable_stream(rs.stream.depth, h, w, rs.format.z16, 15)
	config.enable_stream(rs.stream.color, h, w, rs.format.bgr8, 15)
	rb.read_bag(config)

	# Start streaming
	profile = pipeline.start(config)
	# Getting the depth sensor's depth scale (see rs-align example for explanation)
	depth_sensor = profile.get_device().first_depth_sensor()
	depth_scale = depth_sensor.get_depth_scale()
	# We will be removing the background of objects more than
	#  clipping_distance_in_meters meters away
	clipping_distance_in_meters = 1  # 1 meter
	clipping_d = clipping_distance_in_meters / depth_scale
	# Create an align object
	# rs.align allows us to perform alignment of depth frames to others frames
	# The "align_to" is the stream type to which we plan to align depth frames.
	align_to = rs.stream.color
	al = rs.align(align_to)

	mcd.main(pipeline, h, w, clipping_d, al)
