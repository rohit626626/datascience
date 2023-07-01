from matplotlib import pyplot as plt
from matplotlib import style


style.use('ggplot')
x1=[2,3,6,8]
y1=[3,5,7,10]
x2=[1,3,7,8]
y2=[2,5,8,9]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()