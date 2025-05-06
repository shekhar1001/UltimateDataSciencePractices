import numpy as np
my_12=(113,213,313,413,576)
print(f'\nmy_12 type is: {type(my_12)}')
mynd_arr2=np.array(my_12)
print('mynd_arr2 -->'+str(type(mynd_arr2)))
print('The Array dimensions is:'+str(mynd_arr2.ndim))
print('The data type of array elements is:'+str(mynd_arr2.dtype))
print('The array size is:'+str(mynd_arr2.size))
print('The array shape is:'+str(mynd_arr2.shape))

mytuple=('Ric','Pic','Tic','Mic')
print('mytuple type is:'+str(type(mytuple)))
mynd_arr2=np.array(mytuple)
print('mynd_arr2 type is: -->'+str(type(mynd_arr2)))
print('mynd_arr2 --> '+str(mynd_arr2))

# my_12 type is: <class 'tuple'>
# mynd_arr2 --><class 'numpy.ndarray'>
# The Array dimensions is:1
# The data type of array elements is:int64
# The array size is:5
# The array shape is:(5,)
# mytuple type is:<class 'tuple'>
# mynd_arr2 type is: --><class 'numpy.ndarray'>
# mynd_arr2 --> ['Ric' 'Pic' 'Tic' 'Mic']