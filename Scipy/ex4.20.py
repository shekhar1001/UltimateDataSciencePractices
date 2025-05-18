# Block sparse row matrix
import numpy as mynp
import scipy.sparse as myscpy
 # Creating a dense matrix
mydense_matrix = mynp.array([[11, 12, 0, 0],
                         [13, 14, 15, 0],
                         [0, 16, 71, 18],
                         [0, 0, 19, 100]])
 # Converting the dense matrix to BSR format
mybsr_matrix = myscpy.bsr_matrix(mydense_matrix,
blocksize=(2, 2))
print(mybsr_matrix)

# (0, 0)        11
# (0, 1)        12
# (1, 0)        13
# (1, 1)        14
# (0, 2)        0
# (0, 3)        0
# (1, 2)        15
# (1, 3)        0
# (2, 0)        0
# (2, 1)        16
# (3, 0)        0
# (3, 1)        0
# (2, 2)        71
# (2, 3)        18
# (3, 2)        19
# (3, 3)        100
