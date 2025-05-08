# Broadcasting concept in numpy
import numpy as np

print('Broadcasting of 1-D array ----------')
# Broadcasting of 1-D array
myarr1=np.array([21,22,23])
myarr2=np.array([10])
print(f'myarray1 is {myarr1}')
print(f'myarray2 is {myarr2}')
print(f'myarr1+myarr2 is : {myarr1+myarr2}')

print("Broadcasting of 2-D array--------------")
myarr3= np.arange(21,27).reshape(2,3)
myarr4= np.array([10,12,13])
print(f"myarr3 is {myarr3}")
print(f"myarr4 is {myarr4}")
print(f"myarr3+myarr4 is: {myarr3+myarr4}")