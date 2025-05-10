# hstack()
import numpy as np
# print(help(np.hstack))
print("Eg1 hstack for 1-D array------------------------------")
myarr1 = np.array([1, 2, 3,])
myarr2 = np.array([11,12,13,14])
myarr3 = np.hstack((myarr1,myarr2))
print(f"Hstack array is {myarr3}")
print("Eg2 2-D array shape with (3,3) and (3,2)------------------------------")
a = np.arange(1,10).reshape(3,3)
b = np.arange(1,7).reshape(3,2)
print(f" hstack array is : {np.hstack((a,b))}")
print("Eg with corrected shapes for hstack ------------------------------")
myarr4 = np.arange(1,5).reshape(2,2)
myarr5 = np.arange(5,9).reshape(2,2)
print(f" hstack array for the above : {np.hstack((myarr4,myarr5))}")


# Eg1 hstack for 1-D array------------------------------
# Hstack array is [ 1  2  3 11 12 13 14]
# Eg2 2-D array shape with (3,3) and (3,2)------------------------------
#  hstack array is : [[1 2 3 1 2]
#  [4 5 6 3 4]
#  [7 8 9 5 6]]
# Eg with corrected shapes for hstack ------------------------------
#  hstack array for the above : [[1 2 5 6]
#  [3 4 7 8]]