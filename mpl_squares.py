import matplotlib.pyplot as plt

x_range = list(range(1,1001))
y = [x**3 for x in x_range]
plt.scatter(x_range,y,c=y,cmap=plt.cm.Blues,edgecolors='none',s=40)
#plt.axis([0,1100,0,1100000])


plt.show()