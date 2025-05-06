# creating a 1-D array using a list

import numpy as np
my_11=[113,213,313,413,576]
print(f'my_11 type is: {type(my_11)}')
mynd_arr=np.array(my_11)
print('mynd_arr -->'+str(type(mynd_arr)))
print('The Array dimensions is:'+str(mynd_arr.ndim))
print('The data type of array elements is:'+str(mynd_arr.dtype))
print('The array size is:'+str(mynd_arr.size))
print('The array shape is:'+str(mynd_arr.shape))

# my_11 type is: <class 'list'>
# mynd_arr --><class 'numpy.ndarray'>
# The Array dimensions is:1
# The data type of array elements is:int64
# The array size is:5
# The array shape is:(5,)