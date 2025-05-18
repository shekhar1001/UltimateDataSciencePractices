import scipy as myscpy
# Define the objective function
def myobjective(myvar):
    return myvar[0]**2 + 3*myvar[0]*myvar[1]
# Define the constraints
def myconstraint1(myvar):
    return myvar[0]**3 + 2*myvar[0]*myvar[1] - 200
def myconstraint2(myvar):
    return myvar[0]**2 + 2*myvar[0]*myvar[1] - 50
# Define the bounds
mybounds = [(-200, 200), (-200, 200)]
# Define the constraints dictionary
myconstraints = [{'type': 'eq', 'fun':
myconstraint1},
{'type': 'ineq', 'fun':
myconstraint2}]
# Initial guess
x0 = [1, 1]
# Minimize the objective function using SLSQP method
myresult = myscpy.optimize.minimize(myobjective,x0, method='SLSQP', bounds=mybounds,constraints=myconstraints)
# Print the optimized result
print(myresult)

# message: Optimization terminated successfully
#  success: True
#   status: 0
#      fun: 58.93456942250782
#        x: [ 5.668e+00  1.576e+00]
#      nit: 6
#      jac: [ 1.607e+01  1.701e+01]
#     nfev: 19
#     njev: 6
