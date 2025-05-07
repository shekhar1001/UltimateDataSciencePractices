import numpy as np

# Extracting 2-D diagonal elements
myndarray=np.arange(17,33).reshape(4,4)
print('2-D Original array is : \n'
      +str(myndarray))
print('The elements present at 0-diagonal :'
      +str(np.diag(myndarray,k=0)))
print('The elements present at 1-diagonal :'
      +str(np.diag(myndarray,k=1)))
print('The elements present at 2-diagonal :'
      +str(np.diag(myndarray,k=2)))
print('The elements present at -1-diagonal:'
      +str(np.diag(myndarray,k=-1)))
print('The elements present at -2-diagonal:'
      +str(np.diag(myndarray,k=-2)))
print('The elements present at -3-diagonal:'
      +str(np.diag(myndarray,k=-3)))
print('-'*50)

#  1-D construct a 2-D array using the provided elements
# and a diagonal array and here the remaining elements
# are filled with zeros
mynd_arr1=np.array([101,201,301,401,501])
print(np.diag(mynd_arr1,k=0))
print('-'*50)
mynd_arr2=np.array([101,201,301,401,501])
print(np.diag(mynd_arr2,k=1))
print('-'*50)
mynd_arr3=np.array([101,201,301,401,501])
print(np.diag(mynd_arr3,k=-1))

# 2-D Original array is : 
# [[17 18 19 20]
#  [21 22 23 24]
#  [25 26 27 28]
#  [29 30 31 32]]
# The elements present at 0-diagonal :[17 22 27 32]
# The elements present at 1-diagonal :[18 23 28]
# The elements present at 2-diagonal :[19 24]
# The elements present at -1-diagonal:[21 26 31]
# The elements present at -2-diagonal:[25 30]
# The elements present at -3-diagonal:[29]
# --------------------------------------------------
# [[101   0   0   0   0]
#  [  0 201   0   0   0]
#  [  0   0 301   0   0]
#  [  0   0   0 401   0]
#  [  0   0   0   0 501]]
# --------------------------------------------------
# [[  0 101   0   0   0   0]
#  [  0   0 201   0   0   0]
#  [  0   0   0 301   0   0]
#  [  0   0   0   0 401   0]
#  [  0   0   0   0   0 501]
#  [  0   0   0   0   0   0]]
# --------------------------------------------------
# [[  0   0   0   0   0   0]
#  [101   0   0   0   0   0]
#  [  0 201   0   0   0   0]
#  [  0   0 301   0   0   0]
#  [  0   0   0 401   0   0]
#  [  0   0   0   0 501   0]]