import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utils import saveData as sd


def plt_depth_model(depth_data, coordination_y, coordination_x):
	print('=====>>>>>>>>>plot a real time depth diagram')
	fig = plt.figure()
	ax = Axes3D(fig)

	axis_x = np.linspace(0, 10, coordination_x)
	axis_y = np.linspace(0, 10, coordination_y)
	axis_z = depth_data * 100  # scale the depth data for a better view of the difference between packages

	sd.save_data(axis_x, axis_y, axis_z)

	axis_x, axis_y = np.meshgrid(axis_x, axis_y)

	# choose different diagram to view depth data in 3D
	# ax.scatter(axis_x, axis_y, axis_z, c='y')
	# ax.plot_surface(axis_x, axis_y, axis_z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
	# ax.contourf(axis_x, axis_y, axis_z, zdir='z', offset=-2, cmap='rainbow')
	# use grid diagram wireframe for plotting
	ax.plot_wireframe(axis_x, axis_y, axis_z)

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()
