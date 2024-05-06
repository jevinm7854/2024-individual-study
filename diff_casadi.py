
import casadi as cas
# Define the variable and function
# Declare symbolic variable

x= cas . MX. sym('x') 

# Define the function f(x)
f = x**2 


# Create a CasADi function to compute the derivative
df_dx =cas.gradient(f, x)

# Compile the function
df_dx_fun = cas.Function( 'df dx', [x], [df_dx])

# Evaluate the derivative at a specific point
x_val = 2
df_dx_val = df_dx_fun(x_val)
print( "The derivative of f(x)=x^2 at x=", x_val," is ", df_dx_val)
