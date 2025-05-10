# vstack()

import numpy as np
# print(help(np.vstack))
print("Eg1 vstack for 1-D array------------------------------")
myarr1 = np.array([1, 2, 3,])
myarr2 = np.array([11,12,13])
myarr3 = np.vstack((myarr1,myarr2))
print(f"Vstack array is {myarr3}")
print("Eg2 2-D array shape with (3,3) and (2,3)------------------------------")
a = np.arange(1,10).reshape(3,3)
b = np.arange(20,26).reshape(2,3)
print(f" vstack array is : {np.vstack((a,b))}")
# size of axis 1 of both the arrays are same

# Eg1 vstack for 1-D array------------------------------
# Vstack array is [[ 1  2  3]
#  [11 12 13]]
# Eg2 2-D array shape with (3,3) and (2,3)------------------------------
#  vstack array is : [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [20 21 22]
#  [23 24 25]]