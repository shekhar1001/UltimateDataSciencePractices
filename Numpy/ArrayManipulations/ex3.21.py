# Elements delete from ndarray in numpy
# delete()

import numpy as np
myarr1 = np.arange(10)
print("deleting element present at index 4")
myarr2 = np.delete(myarr1, 4)
print(myarr2)
print("deleting elements from indices 2 to 5")
myarr3 = np.delete(myarr1, np.s_[2:6])
print(myarr3)
myarr4 = np.arange(9).reshape(3,3)
print("Since no axis is specified. So, flattening will be done for 2-D array")
myarr5 = np.delete(myarr4,2)
print(myarr5)
print("axis-0 is specified. So deleting will be done for that row index")
myarr6 = np.delete(myarr4,1, axis=0)
print(myarr6)
print("axis-1 is specified. So deleting will be done for that column index")
myarr7 = np.delete(myarr4,1, axis=1) 
print(myarr7)

# deleting element present at index 4
# [0 1 2 3 5 6 7 8 9]
# deleting elements from indices 2 to 5
# [0 1 6 7 8 9]
# Since no axis is specified. So, flattening will be done for 2-D array
# [0 1 3 4 5 6 7 8]
# axis-0 is specified. So deleting will be done for that row index
# [[0 1 2]
#  [6 7 8]]
# axis-1 is specified. So deleting will be done for that column index
# [[0 2]
#  [3 5]
#  [6 8]]