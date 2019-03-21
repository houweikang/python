import matplotlib.pyplot as plt
from random_walk import Randomwalk

#绘制所有点

rw = Randomwalk()
rw.fill_walk()

#绘制窗口尺寸
plt.figure(dpi=128,figsize=(10,6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=15)

#突出起点和终点
plt.scatter(0,0,c='green',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)

#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()