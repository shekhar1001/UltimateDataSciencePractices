import numpy as np
import sys
my11=[loop for loop in range(11,31)]
myndarray=np.array(my11)

print('The List size is a ', sys.getsizeof(my11))
print('The ndarray size is a ', sys.getsizeof(myndarray))

# The List size is a  248
# The ndarray size is a  272