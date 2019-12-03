import numpy
import pandas as pd
myarray = numpy.array([[1,2,3],[4,5,6]])
rownames = ['rover','star']
colnames = ['venus','mars','saturn']
mydataframe = pd.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
