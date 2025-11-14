# NOTE: This code assumes ode_methods.py is in the same directory.
from ode_methods import IVPSolver
import math # Import math for functions like sin, cos, exp, etc.

# --- 1. Generalized ODE Function ---
def create_f_function(ode_str):
    """
    Creates the f(x, y) function dynamically from a user-provided string.
    Uses lambda and eval for simple function definition.
    """
    # Ensure math functions are available in the scope for eval
    return lambda x, y: eval(ode_str, {'x': x, 'y': y, 'math': math})

# --- 2. Get User Inputs ---
print("--- Numerical Solution of IVP (dy/dx = f(x, y)) ---")

# Differential Equation
ode_input = input("Enter the ODE function f(x, y) (e.g., 'x + y'): ")

# Initial Conditions and Step Size
x0 = float(input("Enter initial x-value (x0): "))
y0 = float(input("Enter initial y-value (y0): "))
h = float(input("Enter step size (h): "))
x_final = float(input("Enter the final x-value to find (x_final): "))

# Calculate the number of steps
if h <= 0 or (x_final - x0) / h <= 0:
    raise ValueError("Invalid step size or range.")
num_steps = int(round((x_final - x0) / h))

# --- 3. Initialize the Solver Class ---
f_xy = create_f_function(ode_input)
solver = IVPSolver(f_xy)

# --- 4. Perform the Numerical Integration for each method ---
print(f"\n--- Solving dy/dx = {ode_input} from x={x0} to x={x_final} (h={h}) ---")
print(f"Number of steps: {num_steps}\n")

# --- A. Euler's Method ---
x_euler = x0
y_euler = y0
print("A. Euler's Method:")
print(f"x={x_euler:.4f}, y={y_euler:.6f} (Start)")

for i in range(num_steps):
    y_euler = solver.euler(x_euler, y_euler, h)
    x_euler += h
    print(f"x={x_euler:.4f}, y={y_euler:.6f}")
    if x_euler >= x_final and i < num_steps - 1: break # Safety break for float precision

# --- B. Modified Euler's Method ---
x_mod_euler = x0
y_mod_euler = y0
print("\nB. Modified Euler's Method:")
print(f"x={x_mod_euler:.4f}, y={y_mod_euler:.6f} (Start)")

for i in range(num_steps):
    y_mod_euler = solver.modified_euler(x_mod_euler, y_mod_euler, h)
    x_mod_euler += h
    print(f"x={x_mod_euler:.4f}, y={y_mod_euler:.6f}")
    if x_mod_euler >= x_final and i < num_steps - 1: break

# --- C. Runge-Kutta (RK4) Method ---
x_rk4 = x0
y_rk4 = y0
print("\nC. Fourth-Order Runge-Kutta (RK4) Method:")
print(f"x={x_rk4:.4f}, y={y_rk4:.6f} (Start)")

for i in range(num_steps):
    y_rk4 = solver.runge_kutta(x_rk4, y_rk4, h)
    x_rk4 += h
    print(f"x={x_rk4:.4f}, y={y_rk4:.6f}")
    if x_rk4 >= x_final and i < num_steps - 1: break

print(f"\n--- Final Results at x = {x_final:.4f} ---")
print(f"Euler's Method:        {y_euler:.6f}")
print(f"Modified Euler's:      {y_mod_euler:.6f}")
print(f"Runge-Kutta (RK4):     {y_rk4:.6f} (Most Accurate)")