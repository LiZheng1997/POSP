import pandas as pd
import numpy as np


def save_data(axis_x, axis_y, axis_z):

	data_array = [[axis_x], [axis_y], [axis_z]]

	np_data = np.array(data_array)
	np_data = np_data.T
	np.array(np_data)

	df = pd.DataFrame(
		np_data, columns=['X', 'Y', 'Z']
	)
	df.to_csv('./test.csv',  encoding="utf-8-sig", header=False, index=False)


