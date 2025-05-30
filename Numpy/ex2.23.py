# Iterate elements of ndarray
import numpy as np

# Approach1: iteration using Python loop
# Iterating elements of 3-D array
myarr1 = np.array([[[34,44],[54,64]],[[74,84],
[94,104]]])
for outer in myarr1:
     for inner in outer:
          for data in inner:
              print(data)
print('-'*50)

# Approach2: iteration using nditer() function:
# class in numpy library with only one loop for
# iterating any n-D array

myarr2=np.arange(21,27).reshape(2,3)
for loop in np.nditer(myarr2):
    print(loop)
print('-'*50)

# Approach3: iteration using ndenumerate()
# function
# This function will return indexes in addition to
# elements as multidimensional
# index iterator will be returned yielding pair of
# index-tuple with the corresponding array values
for mypos,myelement in np.ndenumerate(myarr2):
    print(f'{myelement} is present at position:{mypos}')

# 34
# 44
# 54
# 64
# 34
# 44
# 54
# 64
# 74
# 84
# 94
# 104
# --------------------------------------------------
# 21
# 22
# 23
# 24
# 25
# 26
# --------------------------------------------------
# 21 is present at position:(0, 0)
# 22 is present at position:(0, 1)
# 23 is present at position:(0, 2)
# 24 is present at position:(1, 0)
# 25 is present at position:(1, 1)
# 26 is present at position:(1, 2)