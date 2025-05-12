# append()
import numpy as np
# print(help(np.append))
myarr1 = np.arange(10)
print("In 1-D array, since element added is offloat type, all the elements will be converted to float type")
myarr2 = np.append(myarr1, 10.5)
print(myarr2)
myarr3 = np.append(myarr1, '10.5')
print(myarr3)
print("2-D array: axis is not specified. So will flattened to 1-D array")
myarr4 = np.arange(6).reshape(2,3)
myarr5 = np.append(myarr4,10)
print(myarr5)
print("If I/P array is 2-D array and axis is specified, then appended array must also be 2-Darray otherwise error")
myarr6 = np.arange(10,16).reshape(2,3)
myarr7 = np.append(myarr4,myarr6, axis=0)
print(myarr7)
print("appending to columns for 2-D array")
myarr8 = np.append(myarr4,myarr6, axis=1)
print(myarr8)

# In 1-D array, since element added is offloat type, all the elements will be converted to float type
# [ 0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.5]
# ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' '10.5']
# 2-D array: axis is not specified. So will flattened to 1-D array
# [ 0  1  2  3  4  5 10]
# If I/P array is 2-D array and axis is specified, then appended array must also be 2-Darray otherwise error
# [[ 0  1  2]
#  [ 3  4  5]
#  [10 11 12]
#  [13 14 15]]
# appending to columns for 2-D array
# [[ 0  1  2 10 11 12]
#  [ 3  4  5 13 14 15]]