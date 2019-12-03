# Scatter Plot sample
import matplotlib.pyplot as plt
import numpy
x = numpy.array([1,2,3])
y = numpy.array([2,4,6])
plt.plot(x,y)
#plt.scatter(x,y)
plt.xlabel('new x axis')
plt.ylabel('new y axis')
plt.show()
