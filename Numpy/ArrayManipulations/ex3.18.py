# Elements searching of ndarray in numpy
# where()
# condition based selection

import numpy as np

# using where funtion
myarr1=np.array([10,11,12,15,19,8,39,16,57,8])
mysearch=np.where(myarr1%2==0)
print(myarr1[mysearch])

# condition based selection
myboolean_indexing=myarr1%2==0
print(myarr1[myboolean_indexing])

# [10 12  8 16  8]
# [10 12  8 16  8]