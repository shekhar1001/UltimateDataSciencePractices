# using ravel()
import numpy as np
print("Eg1 using ravel method------------------------------")
myarr1 = np.arange(1,7).reshape(2,3)
myarr2 = myarr1.ravel()
print(f"myarr1 is {myarr1}")
print(f"myarr2 is {myarr2}")
print("Eg2 Making changes to the ravel array------------------------------")
myarr2[0] = 11
print(f"myarr1 after making changes to ravel array is {myarr1}")
print(f"myarr2 after making changes to ravel array is {myarr2}")
print("Eg3 Using ravel function------------------------------")
myarr3 = np.arange(1,7).reshape(2,3)
myarr4 = np.ravel(myarr3, order='F')
print(f"myarr3 is {myarr3}")
print(f"myarr4 is {myarr4}")

# Eg1 using ravel method------------------------------
# myarr1 is [[1 2 3]
#  [4 5 6]]
# myarr2 is [1 2 3 4 5 6]
# Eg2 Making changes to the ravel array------------------------------
# myarr1 after making changes to ravel array is [[11  2  3]
#  [ 4  5  6]]
# myarr2 after making changes to ravel array is [11  2  3  4  5  6]
# Eg3 Using ravel function------------------------------
# myarr3 is [[1 2 3]
#  [4 5 6]]
# myarr4 is [1 4 2 5 3 6]