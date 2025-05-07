# Utilizing the ones() function in numpy
import numpy as np

# Creating 1-D array with ones
print(np.ones(4))
print('-'*50)

# Creating 2-D array with ones
print(np.ones((4,2),dtype=int))
print('-'*50)

# Creating 3-D array with ones
print(np.ones((3,2,3),dtype=int))

# [1. 1. 1. 1.]
# --------------------------------------------------
# [[1 1]
#  [1 1]
#  [1 1]
#  [1 1]]
# --------------------------------------------------
# [[[1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]]]