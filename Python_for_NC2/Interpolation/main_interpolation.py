from interpolation_methods import Interpolation, read_data

#Main fiel code________________________________________________

filename = "input.txt"

# 1. Read data using the function from the module
try:
    n, x_points, y_points = read_data(filename)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    print("Please create the file and populate it with data.")
    exit()

print("--- Data Loaded ---")
print("Number of elements (n):",n)
print("x_points =", x_points)
print("y_points =", y_points)
print("-------------------")

# 2. Create an instance of the Interpolation class
interpolation = Interpolation(n, x_points, y_points)

# 3. Get the value to interpolate
try:
    x_value = float(input("\nEnter the value of x to interpolate: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Newton's Forward Difference
y_value_f, h_f  = interpolation.forward_interpolation(x_value)
print(f"\n--- Newton's Forward Difference ---")
print(f"Step size h = {h_f}")
print(f"Interpolated value at x = {x_value} is {y_value_f}")


# Newton's Backward Difference
y_value_b, h_b  = interpolation.backward_interpolation(x_value)
print(f"\n--- Newton's Backward Difference ---")
print(f"Step size h = {h_b}")
print(f"Interpolated value at x = {x_value} is {y_value_b}")


# Newton's Divided Difference
y_value_dd = interpolation.divided_difference(x_value)
print("\n--- Newton's Divided Difference ---")
print(f"Interpolated value at x = {x_value} is {y_value_dd}")


# Lagrange Interpolation (New Method)
y_value_lagrange = interpolation.lagrange_interpolation(x_value)
print("\n--- Lagrange Interpolation ---")
print(f"Interpolated value at x = {x_value} is {y_value_lagrange}")


# Stirling's Central Difference (New Method)
# This method is only reliable if x_points are evenly spaced.
y_value_stirling = interpolation.stirlings_interpolation(x_value)
print("\n--- Stirling's Central Difference ---")
print(f"Interpolated value at x = {x_value} is {y_value_stirling}")