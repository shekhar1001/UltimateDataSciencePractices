# Creating an array of object type

import numpy as np
mynd_arr=np.array([410,'Sagarmatha',410.5,True,3+7j,False]
                  ,dtype=object)
print(mynd_arr)
print('The elements data type of mynd_arr is: -->'
      +str(mynd_arr.dtype))
