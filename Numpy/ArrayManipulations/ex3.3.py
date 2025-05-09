# using flatten()
import numpy as np
print("Eg1 Displaying flatten method example with default order='C'-------------")
myarr1=np.arange(1,7).reshape(2,3)
myarr2 = myarr1.flatten()
print(f"myarr1 is {myarr1}")
print(f"myarr2 is {myarr2}")
print("Eg2 Changing the original array value will not be reflected in the flatten array------------------------------")
myarr1[0,0]=13
print(f"myarr1 is {myarr1}")
print(f"myarr2 is {myarr2}")
print("Eg3 with order='F'------------------------------")
myarr3=myarr1.flatten('F')
print(f"Flatten array myarr3  is {myarr3}")

# Eg1 Displaying flatten method example with default order='C'-------------
# myarr1 is [[1 2 3]
#  [4 5 6]]
# myarr2 is [1 2 3 4 5 6]
# Eg2 Changing the original array value will not be reflected in the flatten array------------------------------
# myarr1 is [[13  2  3]
#  [ 4  5  6]]
# myarr2 is [1 2 3 4 5 6]
# Eg3 with order='F'------------------------------
# Flatten array myarr3  is [13  4  2  5  3  6]