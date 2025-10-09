# Function to read data 
def read_data(filename):
    """Reads n, x_points, and y_points from the specified file."""
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    # The first line is n
    n = int(lines[0])
    # The next n lines are x_points
    x_points = [float(lines[i]) for i in range(1, n + 1)]
    # The next n lines are y_points
    y_points = [float(lines[i]) for i in range(n + 1, 2 * n + 1)]

    return n, x_points, y_points

class Interpolation:
    def __init__(self, n, x_points, y_points):
        self.n = n
        self.x_points = x_points
        self.y_points = y_points
        
        # Build the forward difference table upon initialization
        self.diff_table = self.build_forward_diff_table()

    def build_forward_diff_table(self):
        """Builds the forward difference table (used for Forward/Backward/Stirling)."""
        diff = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            diff[i][0] = self.y_points[i]

        for j in range(1, self.n):
            for i in range(self.n - j):
                diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]
        return diff

    def factorial(self, num): 
        """Computes the factorial of a number using simple loops."""
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact
        
    #______________________Newton's Forward Interpolation______________________
    def forward_interpolation(self, x):
        """Calculates interpolation using Newton's Forward Difference formula."""
        h = self.x_points[1] - self.x_points[0]
        u = (x - self.x_points[0]) / h
        
        result = self.y_points[0]
        
        for i in range(1, self.n):
            term = self.diff_table[0][i] # The i-th forward difference
            
            product_term = u
            for j in range(1, i):
                product_term *= (u - j)
            
            result += (product_term * term) / self.factorial(i) 

        return result, h
    
    #______________________Newton's Backward Interpolation______________________
    def backward_interpolation(self, x):
        """Calculates interpolation using Newton's Backward Difference formula."""
        h = self.x_points[1] - self.x_points[0]
        u = (x - self.x_points[-1]) / h

        result = self.y_points[-1]
        
        for i in range(1, self.n):
            # The i-th backward difference is located at diff_table[n - i - 1][i]
            term = self.diff_table[self.n - i][i] 
            
            product_term = u
            for j in range(1, i):
                product_term *= (u + j)
                
            result += (product_term * term) / self.factorial(i)
    
        return result, h
    
    #__________________Newton's Divided Difference Interpolation ________________
    def divided_difference(self, x):
        """Calculates interpolation using Newton's Divided Difference formula."""
        dd = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            dd[i][0] = self.y_points[i]

        # Build the divided difference table
        for j in range(1, self.n):
            for i in range(self.n - j):
                dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (self.x_points[i + j] - self.x_points[i])
   
        # Apply the divided difference formula
        result = dd[0][0]
        product = 1.0
        for i in range(1, self.n):
            product *= (x - self.x_points[i - 1])
            result += dd[0][i] * product

        return result

    #_________________________Lagrange Interpolation___________________________
    def lagrange_interpolation(self, x):
        """Calculates interpolation using Lagrange's method (Added Feature)."""
        result = 0.0
        
        # Iterate over all data points (i)
        for i in range(self.n):
            L_i = 1.0 # Lagrange basis polynomial L_i(x)
            
            # Calculate the product term L_i(x)
            for j in range(self.n):
                if i != j:
                    L_i *= (x - self.x_points[j]) / (self.x_points[i] - self.x_points[j])
            
            result += self.y_points[i] * L_i
            
        return result

    #_________________________Stirling's Central Difference______________________
    def stirlings_interpolation(self, x):
        """Calculates interpolation using Stirling's method (Added Feature - Requires evenly spaced data)."""
        h = self.x_points[1] - self.x_points[0]
        
        # Find the central reference index (r)
        r = (self.n - 1) // 2 
        x0 = self.x_points[r]
        u = (x - x0) / h
        
        result = self.y_points[r] 
        
        for j in range(1, self.n):
            term = 0.0
            
            # Calculate the product part (u^2 * (u^2 - 1^2) * ...)
            product_u_sq = 1.0
            if j % 2 == 0:
                k = j // 2
                for m in range(1, k):
                    product_u_sq *= (u*u - m*m)
                
                term_diff = self.diff_table[r - k][j]
                
                if j == 2:
                    term = (u*u / self.factorial(j)) * term_diff
                else:
                    term = (u*u * product_u_sq / self.factorial(j)) * term_diff
                
            else:
                k = (j - 1) // 2
                for m in range(1, k + 1):
                    product_u_sq *= (u*u - m*m)

                # Odd terms use the average of two adjacent central differences
                avg_diff = (self.diff_table[r - k][j] + self.diff_table[r - k - 1][j]) / 2.0
                
                if j == 1:
                    term = (u / self.factorial(j)) * avg_diff
                else:
                    term = (u * product_u_sq / self.factorial(j)) * avg_diff
            
            result += term
            
        return result