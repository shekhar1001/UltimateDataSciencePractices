# Multiple arrays joining into a single array
# concatenate()
import numpy as np

print("Eg1 1-D array concatenation------------------------------")
myarr1= np.arange(4)
myarr2= np.arange(5)
print(f"Concatenation array 1-D is {np.concatenate((myarr1,myarr2))}")
print("Eg2 2-D array concatenation with/without axes parameter------------------------------")
myarr3 = np.arange(1,7).reshape(2,3)
myarr4 = np.array([[10,11,12],[13,14,15]])
print(f"Vertical concatenation: {np.concatenate((myarr3,myarr4), axis=0)}")
print('-'*50)
print(f"Horizontal concatenation:{np.concatenate((myarr3,myarr4), axis=1)}")
print('-'*50)
print(f"Flat and then concatenation:{np.concatenate((myarr3,myarr4), axis=None)}")
print("Eg3 out parameter and dtype usage------------------------------")
# After concatenation, using the 'out' parameter,
# we can store
# the result in an array, but the result and out
# must be in the same shape.
myarr5 = np.arange(5)
myarr6 = np.arange(3)
myempty = np.empty(8, dtype=str)
print(f"out and dtype usage:{np.concatenate((myarr5,myarr6), out=myempty)}")

# Eg1 1-D array concatenation------------------------------
# Concatenation array 1-D is [0 1 2 3 0 1 2 3 4]
# Eg2 2-D array concatenation with/without axes parameter------------------------------
# Vertical concatenation: [[ 1  2  3]
#  [ 4  5  6]
#  [10 11 12]
#  [13 14 15]]
# --------------------------------------------------
# Horizontal concatenation:[[ 1  2  3 10 11 12]
#  [ 4  5  6 13 14 15]]
# --------------------------------------------------
# Flat and then concatenation:[ 1  2  3  4  5  6 10 11 12 13 14 15]
# Eg3 out parameter and dtype usage------------------------------
# out and dtype usage:['0' '1' '2' '3' '4' '0' '1' '2']