# Array creation using linspace() function
import numpy as np
# evenly spaced values of no. of samples as 50
# between 0 and 2 which includes both 0 and 2
print(np.linspace(0,2))
print('-'*50)

# 3 evenly spaced values between 0 and 2 and also
# including both 0 and 2
print(np.linspace(0,2,4,endpoint=False))
print('-'*50)


# 3 evenly spaced values between 0 and 2 and also
# including 0 but excluding 2 and also returning
# spacing
print(np.linspace(0,2,3,endpoint=False,retstep=True))
print('-'*50)

# 5 values between 2 to 50 including both 2 and 50
# with equally spacing int type values with spacing
# as 12.0
print(np.linspace(2,50,5,dtype=int,retstep=True))


# [0.         0.04081633 0.08163265 0.12244898 0.16326531 0.20408163
#  0.24489796 0.28571429 0.32653061 0.36734694 0.40816327 0.44897959
#  0.48979592 0.53061224 0.57142857 0.6122449  0.65306122 0.69387755
#  0.73469388 0.7755102  0.81632653 0.85714286 0.89795918 0.93877551
#  0.97959184 1.02040816 1.06122449 1.10204082 1.14285714 1.18367347
#  1.2244898  1.26530612 1.30612245 1.34693878 1.3877551  1.42857143
#  1.46938776 1.51020408 1.55102041 1.59183673 1.63265306 1.67346939
#  1.71428571 1.75510204 1.79591837 1.83673469 1.87755102 1.91836735
#  1.95918367 2.        ]
# --------------------------------------------------
# [0.  0.5 1.  1.5]
# --------------------------------------------------
# (array([0.        , 0.66666667, 1.33333333]), np.float64(0.6666666666666666))
# --------------------------------------------------
# (array([ 2, 14, 26, 38, 50]), np.float64(12.0))