# vsplit()
import numpy as np

myarr1= np.arange(1,17).reshape(4,4)
print("Eg1: splitting based on sections................")
print(f"vsplit:2 {np.vsplit(myarr1,2)}")
print(f"vsplit:4 {np.vsplit(myarr1,4)}")
print("Eg2: splitting based on indices................")
print(f"vsplit:2 {np.vsplit(myarr1,[2,3])}")

# Eg1: splitting based on sections................
# vsplit:2 [array([[1, 2, 3, 4],
#        [5, 6, 7, 8]]), array([[ 9, 10, 11, 12],
#        [13, 14, 15, 16]])]
# vsplit:4 [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]]), array([[13, 14, 15, 16]])]
# Eg2: splitting based on indices................
# vsplit:2 [array([[1, 2, 3, 4],
#        [5, 6, 7, 8]]), array([[ 9, 10, 11, 12]]), array([[13, 14, 15, 16]])]