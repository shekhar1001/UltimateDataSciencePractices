# Utilizing the zeros() function in numpy

import numpy as np

# Creating 1-D array with zeros
print(np.zeros(4))
print('-'*50)

# Creating 2-D array with zeros
print(np.zeros((4,4)))
print('-'*50)

# Creating 3-D array with zeros
print(np.zeros((2,3,2)))
print('-'*50)

# Creating 4-D array with zeros
print(np.zeros((3,1,2,3)))


# [0. 0. 0. 0.]
# --------------------------------------------------
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
# --------------------------------------------------
# [[[0. 0.]
#   [0. 0.]
#   [0. 0.]]

#  [[0. 0.]
#   [0. 0.]
#   [0. 0.]]]
# --------------------------------------------------
# [[[[0. 0. 0.]
#    [0. 0. 0.]]]


#  [[[0. 0. 0.]
#    [0. 0. 0.]]]


#  [[[0. 0. 0.]
#    [0. 0. 0.]]]]