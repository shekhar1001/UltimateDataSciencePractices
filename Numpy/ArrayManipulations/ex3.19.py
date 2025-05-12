# Elements insert into ndarray
# insert()

import numpy as np
# print(help(np.insert))
myarr1= np.array([10,11,12,15,19,8,39,16,57,8])
myarr2 = np.insert(myarr1,[1,4],[87,89])
print(myarr2) # inserting 87 before index 1 and 89
# before index 4
myarr3 = np.insert(myarr1,2,33.56) # float --->
# int as the original array contains int values
print(myarr3)
myarr4 = np.insert(myarr1,2,True) # addition of
# value 1 before index position 2
print(myarr4)
# If axis not defined for 2-D array, then 2D will
# be flattened to 1-D
# and then insertion will happen
myarr5 = np.arange(4).reshape(2,2)
myarr6 = np.insert(myarr5,2,10)
print(myarr6)
# when axis = 0 or -2 is defined then insertion of
# rows after broadcasting will happpen
myarr7 = np.insert(myarr5,1,10, axis=0)
print(myarr7)
print('-'*50)
# when axis = 1 or -1 is defined then insertion of
# columns after broadcasting will happpen
myarr8 = np.insert(myarr5,1,10, axis=-1)
print(myarr8)

# 10 87 11 12 15 89 19  8 39 16 57  8]
# [10 11 33 12 15 19  8 39 16 57  8]
# [10 11  1 12 15 19  8 39 16 57  8]
# [ 0  1 10  2  3]
# [[ 0  1]
#  [10 10]
#  [ 2  3]]
# --------------------------------------------------
# [[ 0 10  1]
#  [ 2 10  3]]