from casadi import *
x = SX.sym('x')
y = SX.sym('y')
z = SX.sym('z')

f= x**2 + 100*z**2

g= z+(1-x)**2-y

nlp = {'x':vertcat(x,y,z), 'f':f , 'g': g}

sol = nlpsol('S', 'ipopt', nlp)
print(sol)

x0 = [2.5, 3.0, 0.75]  # Initial guess

# Solve the optimization problem
r = sol(x0=x0, lbg=0, ubg=0)

x_opt = r['x']

print('Optimal solution 1:  ', x_opt)
print("\n")


# from casadi import *

# Define symbolic variables
x = SX.sym('x')
y = SX.sym('y')

# Define objective function
f = (x -2)**2 + (y - 3)**2

# Define constraints
g1 = x + y >= 2
g2 = x - y <= 3

# Create dictionary representing the optimization problem
nlp = {'x': vertcat(x, y), 'f': f, 'g': vertcat(g1, g2)}

# Create an NLP solver instance
solver = nlpsol('solver', 'ipopt', nlp)

# Define initial guess and bounds
x0 = [5.0, 0.0]  # Initial guess
lbx = [-inf, -inf]  # Lower bounds
ubx = [inf, inf]  # Upper bounds

# Solve the optimization problem
sol = solver(x0=x0, lbx=lbx, ubx=ubx)

# Extract the optimal solution
x_opt = sol['x']

# Print the optimal solution
print('Optimal solution 2:', x_opt)


# example that demostrates casadi is useful, benefit in terms of modelica and control.
# minimize, maximize given some equation
# casadi and uav toolbox 





