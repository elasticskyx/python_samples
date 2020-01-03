from pandas import read_csv
from pandas import set_option
filename = 'datasets/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
shape = data.shape
print(shape)
types = data.dtypes
# print(types)
# peek = data.tail(20)
# print(peek)
set_option('display.width',5)
set_option('precision',2)
description = data.describe()
print(description)
class_counts = data.groupby(['age','mass']).groups
print(class_counts)
