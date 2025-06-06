# Single integration
import scipy.integrate as myscpy
def myfunc(x):
    return x**2

# print(help(myscpy.quad))
myresult, myerror = myscpy.quad(myfunc, 0, 1)
print("My answer if simple integral is:",
myresult)
print("the error is:", myerror)

# My answer if simple integral is: 0.33333333333333337
# the error is: 3.700743415417189e-15