import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 设置三维坐标
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)  # XY平面的网格数据
Z = (1 - X / 2 + X ** 7 + Y ** 5) * np.exp(-X ** 2 - Y ** 2)
print(np.array(Z).shape)

# 画3d图
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.jet)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
# 等高线图
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')  # zdir= x/y/x 轴的等高线 offset=等高线的位置

# plt.show()