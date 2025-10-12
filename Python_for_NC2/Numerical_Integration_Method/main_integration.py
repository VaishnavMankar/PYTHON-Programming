from integration_methods import NumericalIntegration
from sympy import integrate, Symbol, sympify, lambdify
import numpy as np 
#_________________________ Main code ________________________________________

#Get User Input
print("Numerical Integration Calculator")

try:
    # Get function from user (e.g., "x**2 + 2*x", "sin(x)", "exp(x)")
    func_str = input("Enter the function f(x) (use 'x' as the variable, e.g., x**2 + 2*x): ")
    
    # Get the limits and n from the user
    a = float(input("Enter the lower limit (a): "))
    b = float(input("Enter the upper limit (b): "))
    n = int(input("Enter the number of subintervals (n): "))
except ValueError:
    print("Invalid input. Please enter numbers for limits and an integer for n.")
    exit()

if a >= b or n <= 0:
    print("Invalid input: Ensure a < b and n > 0.")
    exit()

#Define Symbolic and Numerical Functions
x = Symbol('x')

try:
    #Convert string to SymPy expression for exact integral
    symbolic_func = sympify(func_str)
    
    #Create a numerical function for the numerical methods (using numpy for safety/efficiency)
    func_numerical = lambdify(x, symbolic_func, 'numpy')

except (SyntaxError, TypeError, NameError) as e:
    print(f"\nError in function definition: {e}")
    print("Please ensure your function uses valid Python/SymPy syntax (e.g., use '**' for power, 'np.sin' is not needed here as 'lambdify' handles it).")
    exit()


#Calculate Exact Integral (using SymPy)
exact_integral = integrate(symbolic_func, (x, a, b))


#Perform Numerical Integration
integrator = NumericalIntegration(n, a, b, func_numerical)

h = integrator.get_h()

# Calculate results for all three methods
trap_result = integrator.trapezoidal_rule()
simp1_3_result = integrator.simpson_one_third_rule()
simp3_8_result = integrator.simpson_three_eighths_rule()

print("\n---------------------------------------------------")
print(f"Function: f(x) = {func_str}")
print(f"Limits: [{a}, {b}] | Intervals (n): {n} | Step size (h): {h}")
print("---------------------------------------------------")

# Print the table header
print("Method | Approx. Value | Abs. Error")
print("-" * 45)

print(f"Exact Value (SymPy) | {float(exact_integral)} | 0.0")

#Trapezoidal Rule
abs_err_trap = abs(float(exact_integral) - trap_result)
print(f"Trapezoidal Rule | {trap_result} | {abs_err_trap}")

#Simpson's 1/3 Rule
if isinstance(simp1_3_result, (int, float)):
    abs_err_s13 = abs(float(exact_integral) - simp1_3_result)
    print(f"Simpson's 1/3 Rule | {simp1_3_result} | {abs_err_s13}")
else:
    print(f"Simpson's 1/3 Rule | {simp1_3_result} | N/A")

#Simpson's 3/8 Rule
if isinstance(simp3_8_result, (int, float)):
    abs_err_s38 = abs(float(exact_integral) - simp3_8_result)
    print(f"Simpson's 3/8 Rule | {simp3_8_result} | {abs_err_s38}")
else:
    print(f"Simpson's 3/8 Rule | {simp3_8_result} | N/A")