# using resize()
import numpy as np
print("Eg1 Increasing the size using functional style--------------------------")
myarr1=np.arange(1,5)
myarr2=np.resize(myarr1,(2,3))
print(f"myarr1 is: {myarr1}")
print(f"myarr2 is: {myarr2}")
print("Eg2 Increasing the size using object-oriented style -------------------")
myarr3=np.arange(1,5)
myarr3.resize((2,3))
print(f"myarr3 is: {myarr3}")

# Eg1 Increasing the size using functional style--------------------------
# myarr1 is: [1 2 3 4]
# myarr2 is: [[1 2 3]
#  [4 1 2]]
# Eg2 Increasing the size using object-oriented style -------------------
# myarr3 is: [[1 2 3]
#  [4 0 0]]