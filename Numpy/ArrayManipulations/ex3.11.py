# dstack()
import numpy as np

print("Eg1 dstack for 1-D array------------------------------")
myarr1 = np.array([1, 2, 3,])
myarr2 = np.array([11,12,13])
myarr3 = np.dstack((myarr1,myarr2))
print(f"dstack array is {myarr3}")
print(f"dstack 1-D array shape is {myarr3.shape}")
print("d stack for 2-D array------------------------------")
a = np.arange(11,17).reshape(3,2)
b = np.arange(1,7).reshape(3,2)
print(f" dstack 2-D array is :{np.dstack((a,b))}")
print(f" dstack 2-D array shape is : {np.dstack((a,b)).shape}")

# Eg1 dstack for 1-D array------------------------------
# dstack array is [[[ 1 11]
#   [ 2 12]
#   [ 3 13]]]
# dstack 1-D array shape is (1, 3, 2)
# d stack for 2-D array------------------------------
#  dstack 2-D array is :[[[11  1]
#   [12  2]]

#  [[13  3]
#   [14  4]]

#  [[15  5]
#   [16  6]]]
#  dstack 2-D array shape is : (3, 2, 2)