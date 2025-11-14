class IVPSolver:
    """
    A class containing standard numerical methods for solving a first-order ODE:
    dy/dx = f(x, y), with initial condition y(x0) = y0.
    """

    def __init__(self, f_function):
        """
        Initializes the solver with the differential equation function.
        f_function is the function f(x, y) that defines the ODE.
        """
        self.f = f_function
    
    # --- 1. Euler's Method ---
    def euler(self, x_n, y_n, h):
        """
        Calculates the next y-value using Euler's method.
        y(n+1) = y(n) + h * f(x_n, y_n)
        """
        f_val = self.f(x_n, y_n)
        y_n_plus_1 = y_n + h * f_val
        return y_n_plus_1

    # --- 2. Modified Euler's Method (Heun's Method) ---
    def modified_euler(self, x_n, y_n, h):
        """
        Calculates the next y-value using the Modified Euler's (Heun's) method.
        """
        # Predictor Step
        y_n_plus_1_star = y_n + h * self.f(x_n, y_n)
        
        # Corrector Step
        x_n_plus_1 = x_n + h
        slope_avg = (self.f(x_n, y_n) + self.f(x_n_plus_1, y_n_plus_1_star)) / 2
        
        y_n_plus_1 = y_n + h * slope_avg
        return y_n_plus_1

    # --- 3. Fourth-Order Runge-Kutta Method (RK4) ---
    def runge_kutta(self, x_n, y_n, h):
        """
        Calculates the next y-value using the Fourth-Order Runge-Kutta (RK4) method.
        """
        # Step 1: Slope at the start point
        k1 = h * self.f(x_n, y_n)
        
        # Step 2: Slope at the midpoint using k1
        k2 = h * self.f(x_n + h/2, y_n + k1/2)
        
        # Step 3: Slope at the midpoint using k2
        k3 = h * self.f(x_n + h/2, y_n + k2/2)
        
        # Step 4: Slope at the endpoint using k3
        k4 = h * self.f(x_n + h, y_n + k3)
        
        # Weighted average update
        y_n_plus_1 = y_n + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        return y_n_plus_1