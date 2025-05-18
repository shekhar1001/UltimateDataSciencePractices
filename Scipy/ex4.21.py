# Coordinate list matrix

import numpy as mynp
import scipy.sparse as myscpy
myrows = mynp.array([0, 0, 0, 1, 1, 1])
mycols = mynp.array([0, 1, 2, 0, 1, 2])
mydata = mynp.array([11, 12, 13, 14, 15, 16])
mymatrix = myscpy.coo_matrix((mydata, (myrows,
mycols)))
print(mymatrix)
#   (0, 0)        11
#   (0, 1)        12
#   (0, 2)        13
#   (1, 0)        14
#   (1, 1)        15
#   (1, 2)        16
