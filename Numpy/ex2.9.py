# Creating an array with a specific dtype

import numpy as np
# int type
mynd_arr=np.array([101,201,510.8,0]
                  ,dtype=int)
print(mynd_arr)
# Float type
mynd_arr=np.array([101,201,510.8,0]
                  ,dtype=float)
print(mynd_arr)
# Boolean type
mynd_arr=np.array([101,201,510.8,0,'Booltype','False']
                  ,dtype=bool)
print(mynd_arr)

# Complex type
mynd_arr=np.array([101,201,510.8,0]
                  ,dtype=complex)
print(mynd_arr)

# str type
mynd_arr=np.array([101,201,510.8,0]
                  ,dtype=str)
print(mynd_arr)

# [101 201 510   0]
# [101.  201.  510.8   0. ]
# [ True  True  True False  True  True]
# [101. +0.j 201. +0.j 510.8+0.j   0. +0.j]
# ['101' '201' '510.8' '0']