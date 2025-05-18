# Compressed sparse row matrix


import numpy as mynp
import scipy.sparse as myscpy
# print(help(myscpy.csr_matrix))
myarray = mynp.array([0,0,1,0,0,2,0,3,0])
print(myscpy.csr_matrix(myarray))
print('-'*50)
myarray2 = mynp.array([[0,0,1],[0,0,2],[0,3,0]])
print('Viewing non-zero items using data property')
print(myscpy.csr_matrix(myarray2).data)
print('-'*50)
print('Counting non-zero items using count_nonzero method')
print(myscpy.csr_matrix(myarray2).count_nonzero())
print('-'*50)
print('Eliminating zero items using eliminate_zeros method')
myvar = myscpy.csr_matrix(myarray2)
myvar.eliminate_zeros()
print(myvar)

# <Compressed Sparse Row sparse matrix of dtype 'int64'
#         with 3 stored elements and shape (1, 9)>
#   Coords        Values
#   (0, 2)        1
#   (0, 5)        2
#   (0, 7)        3
# --------------------------------------------------
# Viewing non-zero items using data property
# [1 2 3]
# --------------------------------------------------
# Counting non-zero items using count_nonzero method
# 3
# --------------------------------------------------
# Eliminating zero items using eliminate_zeros method
# <Compressed Sparse Row sparse matrix of dtype 'int64'
#         with 3 stored elements and shape (3, 3)>
#   Coords        Values
#   (0, 2)        1
#   (1, 2)        2
#   (2, 1)        3