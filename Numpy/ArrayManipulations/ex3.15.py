import numpy as np

myarr1= np.arange(24).reshape(2,3,4)
print("Eg1: splitting based on sections................")
print(f"dsplit: {np.dsplit(myarr1,2)}")
print("Eg2: splitting based on indices................")
print(f"dsplit: {np.dsplit(myarr1,[1,3])}")

# Eg1: splitting based on sections................
# dsplit: [array([[[ 0,  1],
#         [ 4,  5],
#         [ 8,  9]],

#        [[12, 13],
#         [16, 17],
#         [20, 21]]]), array([[[ 2,  3],
#         [ 6,  7],
#         [10, 11]],

#        [[14, 15],
#         [18, 19],
#         [22, 23]]])]
# Eg2: splitting based on indices................
# dsplit: [array([[[ 0],
#         [ 4],
#         [ 8]],

#        [[12],
#         [16],
#         [20]]]), array([[[ 1,  2],
#         [ 5,  6],
#         [ 9, 10]],

#        [[13, 14],
#         [17, 18],
#         [21, 22]]]), array([[[ 3],
#         [ 7],
#         [11]],

#        [[15],
#         [19],
#         [23]]])]