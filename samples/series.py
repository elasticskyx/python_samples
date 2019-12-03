import numpy
import pandas
myarray = numpy.array([1,2,3])
rownames = ['a','b','c']
myseries = pandas.Series(myarray,index=rownames)
print(myseries)
print("first row: %s" %myseries[0])
print("another row: %s" %myseries['b'])
