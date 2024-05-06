import casadi as ca

#Load FMU file representing the Modelica model
fmu=ca.external('ModelicaModel.fmu')

# Define optimization variables
m=ca.MX.sym('m')
k=ca.MX.sym('k')
c=ca.MX.sym('c')

# Define optimization problem
x=fmu({'m':m ,'k':k, 'c':c})
opti=ca.Opti()
opti.minimize(-ca.max(x))
opti.subject_to(m>=0,k>=0,c>=0)

# Solve optimization problem
solver=ca.nlpsol('solver','ipopt',opti)
solution=solver()

# Extract optimized parameters
optimized_m=solution.value(m)
optimized_k=solution.value(k)
optimized_c=solution.value(c)

print("Optimized parameters:")
print("Mass (m): ",optimized_m)
print("Spring Constant (k): ",optimized_k)
print("Damping coefficient (c): ",optimized_c)