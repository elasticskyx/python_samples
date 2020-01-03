from numpy import loadtxt
filename = 'datasets/pima-indians-diabetes.data.csv'
raw_data = open(filename,'rt')
data = loadtxt(raw_data, delimiter=",")
print(data.shape)
