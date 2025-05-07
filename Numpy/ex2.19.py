# Using random module for ndarray creation
# randint()

import numpy as np
import sys

# single random integer value generation in the range between 20 to 29
print(np.random.randint(20,30))
print('-'*50)

# 1-D nd-array creation of size 5 with random 
# values from 10 to 19
print(np.random.randint(10,20,size=5))
print('-'*50)

# 2-D array with high as None and random values from 0 to 49 with shape as (3,4)
print(np.random.randint(0,50,size=(3,4)))
print('-'*50)

# memory utilization is improved using dtype
a=np.random.randint(1,21,size=(30,40))
print(f'ndarray int32 size:{sys.getsizeof(a)}')
a=np.random.randint(1,21,size=(30,40),dtype='int8')
print(f'ndarray int8 size: {sys.getsizeof(a)}')


# [10 17 12 13 14]
# --------------------------------------------------
# [[25 42 42  6]
#  [19 21  2 14]
#  [15  3  4  9]]
# --------------------------------------------------
# ndarray int32 size:9728
# ndarray int8 size: 1328