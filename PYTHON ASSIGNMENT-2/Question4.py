#Question4:Solve a system of linear equation using numpy.Given system 
#2x+3y=5 ,4x+y=6 solve for x and y.

import numpy as np

# Coefficient matrix A
A = np.array([[2, 3],
              [4, 1]])

# Right-hand side vector b
b = np.array([5, 6])

solution = np.linalg.solve(A, b)

# Print the solution for x and y
print(f"Solution for x and y: {solution}")

#Solution for x and y: [1.3 0.8]