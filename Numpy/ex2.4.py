import numpy as np
from datetime import datetime
myarr_1=np.array([14,15,16])
myarr_2=np.array([11,12,13])

# Conventional Python Code
def my_dot_product(myarr_1,myarr_2):
    my_result=0
    for _x,_y in zip(myarr_1,myarr_2):
        my_result += _x*_y
    return my_result
mybefore_time=datetime.now()
for myloop in range(2000000):
    my_dot_product(myarr_1, myarr_2)
myafter_time=datetime.now()
print('Time take to execute using conventional Python Approach:'
      ,myafter_time-mybefore_time)

# code using nympy library
mybefore2_time=datetime.now()
for my_loop in range(2000000):
    np.dot(myarr_1,myarr_2)
myafter2_time=datetime.now()
print('Time take to execute using Numpy Library:'
      , myafter2_time-mybefore2_time)

# Time take to execute using conventional Python Approach: 0:00:05.214202
# Time take to execute using Numpy Library: 0:00:03.331447