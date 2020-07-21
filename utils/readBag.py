# Import os.path for file path manipulation
import os.path
# Import argparse for command-line options
import argparse
import pyrealsense2 as rs

# this module is aimed at reading bags from the bag file, and users should show the path in
# the terminal, where is the path to read the bag file.


def read_bag(config):

	# Create object for parsing command-line options
	parser = argparse.ArgumentParser(description="Read recorded bag file and display depth stream in jet colormap.\
	                                Remember to change the stream resolution, fps and format to match the recorded.")
	# Add argument which takes path to a bag file as an input
	parser.add_argument("-i", "--input", type=str, help="Path to the bag file")
	# Parse the command line arguments to an object
	args = parser.parse_args()
	# testing the data, only for testing
	args.input = '/home/lizheng/Documents/Pick_Out_Single_package/data/liangjian/20200710152835.bag'
	# Safety if no parameter have been given
	if not args.input:
		print("No input paramater have been given.")
		print("For help type --help")
		exit()
	# Check if the given file have bag extension
	if os.path.splitext(args.input)[1] != ".bag":
		print("The given file is not of correct file format.")
		print("Only .bag files are accepted")
		exit()
	# Tell config that we will use a recorded device from file to be used by the pipeline through playback.
	rs.config.enable_device_from_file(config, args.input)
