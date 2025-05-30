# Diagonal sparse matrix
import scipy.sparse as myscpy
# Create a diagonal matrix
mydiagonal_values = [11, 12, 13, 14]
mydiagonal_offsets = [0]  # The diagonal is at offset 0
mydia_matrix =myscpy.dia_matrix((mydiagonal_values,
mydiagonal_offsets), shape=(4, 4))
print(mydia_matrix)


#   (0, 0)        11
#   (1, 1)        12
#   (2, 2)        13
#   (3, 3)        14
