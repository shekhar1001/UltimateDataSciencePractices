# View vs Copy

import numpy as np

# Example View
mynp1=np.array([16,25,35,46,55])
mynp2=mynp1.view()
print(f'The original array is: {mynp1}')
print(f'The view of the original array is: {mynp2}')
print('-'*50)
mynp1[2]=100
print(f'After changing 2nd index value of mynp1,mynp1 arrray value is changed as :{mynp1}')
print(f'After changing last index value of mynp2, mynp2 array value is changed as: {mynp2}')

# Example Copy
print('*'*100)
mynp3=np.array([111,132,136,147,158])
mynp4=mynp3.copy()
print(f'The original array is: {mynp3}')
print(f'The copy of the original array is :{mynp4}')
print('-'*50)
mynp3[2]=110
print(f'After changing 2nd index value of mynp3, mynp3 array value is changed as: {mynp3}')
print(f'After chainging 2nd index value of mynp3, mynp4 array value is retained as :{mynp4}')
print('-'*50)
mynp4[-1]=331
print(f'After changing last index value of mynp4, mynp4 array value is retained as :{mynp3}')
print(f'After changing last index value of mynp4, mynp4 array value is changed as :{mynp4}')


# The original array is: [16 25 35 46 55]
# The view of the original array is: [16 25 35 46 55]
# --------------------------------------------------
# After changing 2nd index value of mynp1,mynp1 arrray value is changed as :[ 16  25 100  46  55]
# After changing last index value of mynp2, mynp2 array value is changed as: [ 16  25 100  46  55]
# ****************************************************************************************************
# The original array is: [111 132 136 147 158]
# The copy of the original array is :[111 132 136 147 158]
# --------------------------------------------------
# After changing 2nd index value of mynp3, mynp3 array value is changed as: [111 132 110 147 158]
# After chainging 2nd index value of mynp3, mynp4 array value is retained as :[111 132 136 147 158]
# --------------------------------------------------
# After changing last index value of mynp4, mynp4 array value is retained as :[111 132 110 147 158]
# After changing last index value of mynp4, mynp4 array value is changed as :[111 132 136 147 331]