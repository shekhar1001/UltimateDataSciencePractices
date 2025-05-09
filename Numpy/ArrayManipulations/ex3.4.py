# using flat variable

import numpy as np
#print(help(np.ndarray.flat))
print("Eg1 ------------------------------")

np1=np.arange(1,7).reshape(2,3)
print(np1.flat)
# iterating
for loop in np1.flat:
    print(loop)


# Eg1 ------------------------------
# <numpy.flatiter object at 0x7ff3a48cf200>
# 1
# 2
# 3
# 4
# 5
# 6