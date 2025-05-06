# creating a 2-D array using nested list

import numpy as np
my_nested11=[[105,205,305],[405,505,605],
             [705,805,905],[1005,1105,1205]]
mynd_arr=np.array(my_nested11)
print('mynd_arr type is: -->'
      +str(type(mynd_arr)))
print('mynd_arr -->'
      +str(mynd_arr))
print('The array dimensions is:'
      +str(mynd_arr.ndim))
print('The data type of array elements is : '
      +str(mynd_arr.dtype))
print('The array size is :'
      +str(mynd_arr.size))
print('The array shape is:'
      +str(mynd_arr.shape))