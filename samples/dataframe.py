import numpy
import pandas
myarray = numpy.array([[1,2,3],[4,5,6]])
rownames = ['rover','star']
colnames = ['venus','mars','saturn']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
