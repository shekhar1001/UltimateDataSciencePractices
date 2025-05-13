# Usage of linalg module in numpy
import numpy as np
print("Finding matrix inverse")
myarr1 = np.arange(11,15).reshape(2,2)
print(np.linalg.inv(myarr1)) # only valid for square matrices
print("Finding power of a matrix with n=0")  #only valid for square matrices
print(np.linalg.matrix_power(myarr1,0))
print("Finding power of a matrix with n>0")
print(np.linalg.matrix_power(myarr1,2))
print("Finding power of a matrix with n<0")
print(np.linalg.matrix_power(myarr1,-2)) # first inverse then power
print("Finding matrix determinant") # only valid for square matrices
print(np.linalg.det(myarr1))
print("Finding Solving linear algebra equations")
myarr2 = np.array([[1,1],[2,6]])
myarr3 = np.array([6,24])
print(np.linalg.solve(myarr2,myarr3))

# Finding matrix inverse
# [[-7.   6. ]
#  [ 6.5 -5.5]]
# Finding power of a matrix with n=0
# [[1 0]
#  [0 1]]
# Finding power of a matrix with n>0
# [[277 300]
#  [325 352]]
# Finding power of a matrix with n<0
# [[ 88.   -75.  ]
#  [-81.25  69.25]]
# Finding matrix determinant
# -1.9999999999999931
# Finding Solving linear algebra equations
# [3. 3.]