# Using random module for ndarray creation
# shuffle()

import numpy as np
# shuffling of 1-D array
mynp1=np.arange(6)
print(f'before shuffle mynp1 data is {mynp1}')
np.random.shuffle(mynp1)
print(f'after shuffle mynp1 data is {mynp1}')
print('-'*50)

# shuffling of 2-D array --shuffling around axis0
mynp2=np.random.randint(1,50,size=(4,3))
print(f'before shuffle mynp2 data is {mynp2}')
np.random.shuffle(mynp2)
print(f'after shuffle mynp2 data is {mynp2}')

# before shuffle mynp1 data is [0 1 2 3 4 5]
# after shuffle mynp1 data is [0 3 1 4 5 2]
# --------------------------------------------------
# before shuffle mynp2 data is [[23 26 25]
#  [45 29  4]
#  [22 19 33]
#  [ 8 28 10]]
# after shuffle mynp2 data is [[22 19 33]
#  [23 26 25]
#  [45 29  4]
#  [ 8 28 10]]