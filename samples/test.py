#Test all ML libraries are installed
import sklearn
import sys
import matplotlib
import pandas
import scipy
import numpy
print(sys.version)
print('numpy: %s' % numpy.__version__)
print('scipy: %s' % scipy.__version__)
print('pandas: %s' % pandas.__version__)
print('matplotlib: %s' % matplotlib.__version__)
print('sklearn: %s' % sklearn.__version__)
