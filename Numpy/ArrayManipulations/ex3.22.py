# Usage of dot function for matrix multiplication

import numpy as np
# print(help(np.dot))
myarr1 = np.arange(1,5).reshape(2,2)
myarr2 = np.arange(11,15).reshape(2,2)
print(myarr1)
print(myarr2)
print("using numpy function")
print(np.dot(myarr1,myarr2))
print("Using ndarray object")
print(myarr1.dot(myarr2))

# [[1 2]
#  [3 4]]
# [[11 12]
#  [13 14]]
# using numpy function
# [[37 40]
#  [85 92]]
# Using ndarray object
# [[37 40]
#  [85 92]]