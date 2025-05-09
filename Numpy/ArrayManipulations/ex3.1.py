# using reshape()
import numpy as np
print("Eg-1 1-D array conversion to 2-D array with by default C style order ------")
myarr1=np.arange(1,7)
myarr2=myarr1.reshape(2,3)
print(f'myarr1 is: {myarr1}')
print(f'myarr2 is: {myarr2}')
print('Eg-2 modifying the 2nd index value of original array------')
myarr1[1]=12
print(f'myarr1 after modification in the original array is: {myarr1}')
print(f'myarr2 after modification in the reshaped array is: {myarr2}')

print('Eg-3 F Style order --------')
myarr3=np.arange(1,7)
myarr4=myarr3.reshape(2,3,order='F')
print(f'myarr3 is : {myarr3}')
print(f'myarr4 is : {myarr4}')

# Eg-1 1-D array conversion to 2-D array with by default C style order ------
# myarr1 is: [1 2 3 4 5 6]
# myarr2 is: [[1 2 3]
#  [4 5 6]]
# Eg-2 modifying the 2nd index value of original array------
# myarr1 after modification in the original array is: [ 1 12  3  4  5  6]
# myarr2 after modification in the reshaped array is: [[ 1 12  3]
#  [ 4  5  6]]
# Eg-3 F Style order --------
# myarr3 is : [1 2 3 4 5 6]
# myarr4 is : [[1 3 5]
#  [2 4 6]]