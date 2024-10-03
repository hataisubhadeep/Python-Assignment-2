#Question2:Use the scipy library to numerically integrate the function f(x)=x^2 over the range [0,5].print 
 
import scipy.integrate as integrate

# Define the function f(x) = x^2
def f(x):
    return x**2

# Perform the numerical integration over the range [0, 5]
result, error = integrate.quad(f, 0, 5)

# Print the result
print(f"Numerical integration result: {result}")
print(f"Estimated error: {error}")

#Numerical integration result: 41.66666666666666
#Estimated error: 4.625929269271485e-13  