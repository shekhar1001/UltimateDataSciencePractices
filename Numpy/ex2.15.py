# Utilizing the full() function in numpy
import numpy as np

# Creating 1-D array
print(np.full(shape=4,fill_value=2))
print('-'*50)

# Creating 2-D array
print(np.full((3,2),fill_value=2))
print('-'*50)

# Creating 3-D array
print(np.full((3,2,3),fill_value=2))

# [2 2 2 2]
# --------------------------------------------------
# [[2 2]
#  [2 2]
#  [2 2]]
# --------------------------------------------------
# [[[2 2 2]
#   [2 2 2]]

#  [[2 2 2]
#   [2 2 2]]

#  [[2 2 2]
#   [2 2 2]]]