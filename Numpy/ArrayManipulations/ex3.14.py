# hsplit()
import numpy as np

myarr1= np.arange(1,9).reshape(2,4)
print("Eg1: splitting based on sections................")
print(f"hsplit:2 {np.hsplit(myarr1,2)}")
print("Eg2: splitting based on indices................")
print(f"hsplit: {np.hsplit(myarr1,[2,3])}")

# Eg1: splitting based on sections................
# hsplit:2 [array([[1, 2],
#        [5, 6]]), array([[3, 4],
#        [7, 8]])]
# Eg2: splitting based on indices................
# hsplit: [array([[1, 2],
#        [5, 6]]), array([[3],
#        [7]]), array([[4],
#        [8]])]