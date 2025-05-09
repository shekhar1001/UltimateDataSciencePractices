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

# Dimension of myarr1 is : 2,size of myarr1 is :6 and shape of myarr1 is : (2, 3)
# Dimension of myarr2 is : 2, size of myarr2 is :6 and shape of myarr2 is : (2, 3)
# Numpy array 1 is: [[21 31 41]
#  [52 62 72]]
# Numpy array 2 is: [[21 22 23]
#  [24 25 26]]
# --------------------------------------------------
# Addition of 2 numpy arrays is [[42 53 64]
#  [76 87 98]]
# --------------------------------------------------
# Subtraction of 2 numpy arrays is [[ 0  9 18]
#  [28 37 46]]
# --------------------------------------------------
# Multiplication of 2 numpy arrays is [[ 441  682  943]
#  [1248 1550 1872]]
# --------------------------------------------------
# Division of 2 numpy arrays is [[1.         1.40909091 1.7826087 ]
#  [2.16666667 2.48       2.76923077]]
# --------------------------------------------------
# Floor division of 2 numpy arrays is [[1 1 1]
#  [2 2 2]]
# --------------------------------------------------
# Modulus of 2 numpy arrays is [[ 0  9 18]
#  [ 4 12 20]]
# --------------------------------------------------
# Power of 2 numpy arrays is [[-1595931050845505211  2144576063759554881  6681134104860204761]
#  [-4872613321838166016  1298077544687337472                    0]]