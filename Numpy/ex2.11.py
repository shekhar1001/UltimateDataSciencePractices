# Creating a 1-D array with arange() function
import numpy as np
mynd_arr=np.arange(7)
print('mynd_arr is:'
      +str(mynd_arr))
print('The array dimension is:'
      +str(mynd_arr.ndim))
print('The data type of elements of array is :'
      +str(mynd_arr.dtype))
print('The array size is:'
      +str(mynd_arr.size))
print('The array shape is:'
      +str(mynd_arr.shape))
print('-'*50)
mynd_arr1=np.arange(1,7)
print('mynd_arr1 is:'
      +str(mynd_arr1))
print('The array dimension is:'
      +str(mynd_arr1.ndim))
print('The data type of elements of array is :'
      +str(mynd_arr1.dtype))
print('The array size is:'
      +str(mynd_arr1.size))
print('The array shape is:'
      +str(mynd_arr1.shape))
print('-'*50)
mynd_arr2=np.arange(1,7)
print('mynd_arr2 is:'
      +str(mynd_arr2))
print('The array dimension is:'
      +str(mynd_arr2.ndim))
print('The data type of elements of array is :'
      +str(mynd_arr2.dtype))
print('The array size is:'
      +str(mynd_arr2.size))
print('The array shape is:'
      +str(mynd_arr2.shape))
print('-'*50)
mynd_arr3=np.arange(1,3,7,dtype=float)
print('mynd_arr3 is:'
      +str(mynd_arr3))
print('The array dimension is:'
      +str(mynd_arr3.ndim))
print('The data type of elements of array is :'
      +str(mynd_arr3.dtype))
print('The array size is:'
      +str(mynd_arr3.size))
print('The array shape is:'
      +str(mynd_arr3.shape))


# mynd_arr is:[0 1 2 3 4 5 6]
# The array dimension is:1
# The data type of elements of array is :int64
# The array size is:7
# The array shape is:(7,)
# --------------------------------------------------
# mynd_arr1 is:[1 2 3 4 5 6]
# The array dimension is:1
# The data type of elements of array is :int64
# The array size is:6
# The array shape is:(6,)
# --------------------------------------------------
# mynd_arr2 is:[1 2 3 4 5 6]
# The array dimension is:1
# The data type of elements of array is :int64
# The array size is:6
# The array shape is:(6,)
# --------------------------------------------------
# mynd_arr3 is:[1.]
# The array dimension is:1
# The data type of elements of array is :float64
# The array size is:1
# The array shape is:(1,)