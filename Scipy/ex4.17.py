# Optimizers in Scipy

# Finding roots of an equation:X+cos(x)
import scipy as myscpy
from math import cos
def myeq_func(x):
    return 2*x+cos(x)
myrootvar=myscpy.optimize.root(myeq_func,1)
# args as function and initial guess
print(myrootvar.x)
print('-'*50)
print(myrootvar)


# [-0.45018361]
# --------------------------------------------------
#  message: The solution converged.
#  success: True
#   status: 1
#      fun: [-3.109e-15]
#        x: [-4.502e-01]
#   method: hybr
#     nfev: 11
#     fjac: [[-1.000e+00]]
#        r: [-2.435e+00]
#      qtf: [-2.970e-09]