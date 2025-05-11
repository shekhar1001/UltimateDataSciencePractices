# Splitting of arrays in numpy
# split()
import numpy as np
#print(help(np.split))
print("Eg1 split for 1-D array based on sections------------------------------")
myarr1 = np.arange(1,7)
myarr2 = np.split(myarr1,3)
print(f"Array type is: {type(myarr2)}")
print(f"Subarrays are : {myarr2}")
print("Eg2 2-D array split based on sections------------------------------")
myarr3 = np.arange(1,19).reshape(6,3)
print(f"Array split ino 2 sections:{np.split(myarr3,2, axis=0)}")
print(f"Array split ino 6 sections:{np.split(myarr3,6, axis=0)}")
print("Eg3 Splitting 1-D array based on indices")
myarr4=np.arange(1,11)
myresult = np.split(myarr4,[3,6])
print(f"myresult for 1-D after splitting is:{myresult}") # splitting on indexes: 0,1,2 and
# 3,4,5 and 6,7,8,9
print("Eg4 Splitting 2-D array based on indices")
myarr5=np.arange(1,19).reshape(3,6)
myresult = np.split(myarr5,[3,5], axis=1)
print(f"myresult for 2-D after splitting is:{myresult}")

# Eg1 split for 1-D array based on sections------------------------------
# Array type is: <class 'list'>
# Subarrays are : [array([1, 2]), array([3, 4]), array([5, 6])]
# Eg2 2-D array split based on sections------------------------------
# Array split ino 2 sections:[array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]), array([[10, 11, 12],
#        [13, 14, 15],
#        [16, 17, 18]])]
# Array split ino 6 sections:[array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]]), array([[10, 11, 12]]), array([[13, 14, 15]]), array([[16, 17, 18]])]
# Eg3 Splitting 1-D array based on indices
# myresult for 1-D after splitting is:[array([1, 2, 3]), array([4, 5, 6]), array([ 7,  8,  9, 10])]
# Eg4 Splitting 2-D array based on indices
# myresult for 2-D after splitting is:[array([[ 1,  2,  3],
#        [ 7,  8,  9],
#        [13, 14, 15]]), array([[ 4,  5],
#        [10, 11],
#        [16, 17]]), array([[ 6],
#        [12],
#        [18]])]