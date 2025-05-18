
import scipy as myscpy

def myfunc_eqn(x):
      return x**2 + 3*x + 5
myvarmin = myscpy.optimize.minimize(myfunc_eqn, 0,
method='BFGS')
print(myvarmin)

#  message: Optimization terminated successfully.
#   success: True
#    status: 0
#       fun: 2.75
#         x: [-1.500e+00]
#       nit: 2
#       jac: [ 0.000e+00]
#  hess_inv: [[ 5.000e-01]]
#      nfev: 6
#      njev: 3