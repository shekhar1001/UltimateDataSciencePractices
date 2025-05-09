# using transpose()
import numpy as mynp
#print(help(mynp.transpose))
print("Eg1 transpose with non-specified axis parameter of 2-D array ------------------------------")
a = mynp.arange(1,7).reshape(2,3)
myarr1 = a.transpose()
print(f"Original Array is : \n {a}")
print(f"Transposed Array is : \n {myarr1}")
print("Eg2 Transpose with specified axis parameter of 3-D array ------------------------------")
a = mynp.arange(1,25).reshape(2,3,4)
myarr2 = mynp.transpose(a,axes=(1,2,0))
print(f"Original 3-D Array is : \n {a}")
print(f"Transposed 3-D Array is : \n {myarr2}")
print(f"Shape of Original 3-D Array is : \n {a.shape}")
print(f"Shape of Transposed 3-D Array is : \n {myarr2.shape}")
print("Eg3 Using T variable------------------------------")
a = mynp.arange(1,25).reshape(2,3,4)
myarr3 = a.T
print(f"Transposed 3-D Array is : \n {myarr3}") #
(4,3,2)


# Eg1 transpose with non-specified axis parameter of 2-D array ------------------------------
# Original Array is : 
#  [[1 2 3]
#  [4 5 6]]
# Transposed Array is : 
#  [[1 4]
#  [2 5]
#  [3 6]]
# Eg2 Transpose with specified axis parameter of 3-D array ------------------------------
# Original 3-D Array is : 
#  [[[ 1  2  3  4]
#   [ 5  6  7  8]
#   [ 9 10 11 12]]

#  [[13 14 15 16]
#   [17 18 19 20]
#   [21 22 23 24]]]
# Transposed 3-D Array is : 
#  [[[ 1 13]
#   [ 2 14]
#   [ 3 15]
#   [ 4 16]]

#  [[ 5 17]
#   [ 6 18]
#   [ 7 19]
#   [ 8 20]]

#  [[ 9 21]
#   [10 22]
#   [11 23]
#   [12 24]]]
# Shape of Original 3-D Array is : 
#  (2, 3, 4)
# Shape of Transposed 3-D Array is : 
#  (3, 4, 2)
# Eg3 Using T variable------------------------------
# Transposed 3-D Array is : 
#  [[[ 1 13]
#   [ 5 17]
#   [ 9 21]]

#  [[ 2 14]
#   [ 6 18]
#   [10 22]]

#  [[ 3 15]
#   [ 7 19]
#   [11 23]]

#  [[ 4 16]
#   [ 8 20]
#   [12 24]]]