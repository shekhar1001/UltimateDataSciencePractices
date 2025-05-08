# Arithmetic operators in numpy
import numpy as np
myarr1 = np.array([ [21,31,41], [52,62,72] ])
myarr2 = np.arange(21,27).reshape(2,3)

print(f"Dimension of myarr1 is : {myarr1.ndim},size of myarr1 is :{myarr1.size} and shape of myarr1 is : {myarr1.shape}")
print(f"Dimension of myarr2 is : {myarr2.ndim}, size of myarr2 is :{myarr2.size} and shape of myarr2 is : {myarr2.shape}")
print(f'Numpy array 1 is: {myarr1}')
print(f'Numpy array 2 is: {myarr2}')
# performing addition
print('-'*50)
print(f"Addition of 2 numpy arrays is {np.add(myarr1,myarr2)}")
# performing subtraction
print('-'*50)
print(f"Subtraction of 2 numpy arrays is {np.subtract(myarr1,myarr2)}")
# performing multiplication
print('-'*50)
print(f"Multiplication of 2 numpy arrays is {np.multiply(myarr1,myarr2)}")
# performing division
print('-'*50)
print(f"Division of 2 numpy arrays is {np.divide(myarr1,myarr2)}")
# performing floor division
print('-'*50)
print(f"Floor division of 2 numpy arrays is {np.floor_divide(myarr1,myarr2)}")
# performing modulus
print('-'*50)
print(f"Modulus of 2 numpy arrays is {np.mod(myarr1,myarr2)}")
# performing power
print('-'*50)
print(f"Power of 2 numpy arrays is {np.power(myarr1,myarr2)}")