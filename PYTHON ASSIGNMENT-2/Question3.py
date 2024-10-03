#Qustion3:Solve the simple optimization problem where you need to minimize th function f(x)=(x-3)^2+2 using scipy.optimize.

import numpy as np
from scipy.optimize import minimize

# Define the function to minimize
def f(x):
    return (x - 3)**2 + 2

x0 = 0  

# Perform the optimization
result = minimize(f, x0)

# Print the result
print(f"Optimal value of x: {result.x}")
print(f"Function value at the minimum: {result.fun}")

#Optimal value of x: [3.00000003]
#Function value at the minimum: 2.000000000000001