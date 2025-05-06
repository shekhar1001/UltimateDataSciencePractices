# list containing elements of different data type
import numpy as np
my_list=[201,301,420.5]
mynd_arr=np.array(my_list)# upcasting to float data type

print('mynd_arr -->'+str(mynd_arr))
print('Elements data type is -->'+str(mynd_arr.dtype))
