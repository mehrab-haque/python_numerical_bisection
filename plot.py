import numpy
from logic import func
from matplotlib import pyplot as plt

xList = numpy.linspace(-10,5,5000)
yList = func(xList)

xList=list(xList)
yList=list(yList)

for i in range(len(yList)-1):
    if i>0:
        if abs(yList[i]-yList[i-1]>10):
            xList[i-1]=numpy.nan
            yList[i-1]=numpy.nan


fig, ax = plt.subplots()
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.plot(xList,yList)
plt.ylim(-10,15)

plt.show()






