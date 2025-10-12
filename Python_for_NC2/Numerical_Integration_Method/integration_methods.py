# integration_methods.py

class NumericalIntegration:
    def __init__(self, n, a, b, func_numerical):
        self.n = n
        self.a = a
        self.b = b
        self.h = (b - a) / n
        self._f = func_numerical # Store the function to be evaluated numerically
        
    def get_h(self):
        """Returns the step size h."""
        return self.h

    def f(self, x):
        """Evaluates the function at a given point x."""
        return self._f(x)
        
    #_________________________Trapezoidal Rule_______________________________
    def trapezoidal_rule(self):
        """Calculates the integral using the Trapezoidal Rule."""
        
        # Formula: h/2 * [f(a) + f(b) + 2 * sum(f(x_i))]
        
        sum_terms = self.f(self.a) + self.f(self.b)
        
        for i in range(1, self.n):
            x_i = self.a + i * self.h
            sum_terms += 2 * self.f(x_i)
            
        result = (self.h / 2) * sum_terms
        return result

    #_______________________Simpson's 1/3 Rule_______________________________
    def simpson_one_third_rule(self):
        """
        Calculates the integral using Simpson's 1/3 Rule.
        Requires n (number of subintervals) to be even.
        """
        if self.n % 2 != 0:
            return "Error: Simpson's 1/3 Rule requires an EVEN number of subintervals (n)."
            
        # Formula: h/3 * [f(a) + f(b) + 4 * sum(f(x_odd)) + 2 * sum(f(x_even))]
        
        sum_terms = self.f(self.a) + self.f(self.b)
        
        for i in range(1, self.n):
            x_i = self.a + i * self.h
            
            if i % 2 != 0:
                # Odd terms (i = 1, 3, 5, ...) are multiplied by 4
                sum_terms += 4 * self.f(x_i)
            else:
                # Even terms (i = 2, 4, 6, ...) are multiplied by 2
                sum_terms += 2 * self.f(x_i)
                
        result = (self.h / 3) * sum_terms
        return result

    #_______________________Simpson's 3/8 Rule_______________________________
    def simpson_three_eighths_rule(self):
        """
        Calculates the integral using Simpson's 3/8 Rule.
        Requires n (number of subintervals) to be a multiple of 3.
        """
        if self.n % 3 != 0:
            return "Error: Simpson's 3/8 Rule requires n to be a MULTIPLE OF 3."
        
        # Formula: 3h/8 * [f(a) + f(b) + 3*sum(f(x_i where i is NOT a multiple of 3)) + 2*sum(f(x_i where i IS a multiple of 3))]
        
        sum_terms = self.f(self.a) + self.f(self.b)
        
        for i in range(1, self.n):
            x_i = self.a + i * self.h
            
            if i % 3 == 0:
                # Terms at multiples of 3 are multiplied by 2
                sum_terms += 2 * self.f(x_i)
            else:
                # All other terms are multiplied by 3
                sum_terms += 3 * self.f(x_i)
                
        result = (3 * self.h / 8) * sum_terms
        return result