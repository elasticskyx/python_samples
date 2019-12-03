import numpy
import pandas as pd
myarray = numpy.array([[1,2,3,9],[4,5,6,11]])
rownames = ['rover','star']
colnames = ['venus','mars','saturn','jupiter']
mydataframe = pd.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
print("\n")
# print("Method 1:")
# print("One column:\n%s" %mydataframe['venus'])
# print("Method 2:")
print("One column:\n%s" %mydataframe.saturn)
