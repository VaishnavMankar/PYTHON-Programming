#_______________________Function to read data_______________________________
def read_data(filename):
    with open(filename,"r") as f:
        lines = f.read().splitlines()

    n = int(lines[0])
    x_points = [float(lines[i]) for i in range(1,n+1)]
    y_points = [float(lines[i]) for i in range(n+1, 2*n+1)]

    return n, x_points, y_points

#______________________Newtons's Interpolation______________________________
class Interpolation:
    def __init__(self,n,x_points,y_points):
        self.n = n
        self.x_points = x_points
        self.y_points = y_points
        self.diff_table = self.build_diff_table()

    def build_diff_table(self):
        diff = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            diff[i][0] = self.y_points[i]

        for j in range(1, self.n):
            for i in range(self.n - j):
                diff[i][i] = diff[i + 1][j - 1] - diff[i][j - 1]
        return diff

    def factorial(self, num): 
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact
    
#______________________Forword interpolation_____________________________
    def forword_interpolation(self, x):
        h = self.x_points[1] - self.x_points[0]
        u = (x - self.x_points[0])/h
        
        result = self.y_points[0]
        for i in range(1,self.n):
            term = u
            for j in range(1, i):
                term *= (u - j)
            result += (term * self.diff_table[0][i])/ self.factorial(i) 

        return result, h
    
#______________________Backword Interpolation_____________________________
    def backword_interpolation(self,x):
        h = self.x_points[1] - self.x_points[0]
        u = (x - self.x_points[-1])/h

        result = self.y_points[-1]
        for i in range(1, self.n):
            term = u
            for j in range(1, self.n):
                term *= (u + j)
            result += (term * self.diff_table[self.n - i - 1][i])/self.factorial(i)
    
        return result, h
    
#__________________Divided difference interpolation ______________________
    def divided_difference(self,x):
        #divided differece table
        dd = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            dd[i][0] = self.y_points[i]

        for j in range(1,self.n):
            for i in range(self.n - j):
                dd[i][j] = (dd[i + 1][j-1] - dd[i][j-1]) / (self.x_points[i + j] - self.x_points[i])
   
        #divided difference formula 
        result = dd[0][0]
        product = 1.0
        for i in range(1,self.n):
            product *= (x - self.x_points[i - 1])
            result += dd[0][i] * product

        return result


#_________________________ Main code ________________________________________

filename = "input.txt"

n, x_points, y_points = read_data(filename)
print("number of elements (n):",n)
print("x_points =",x_points)
print("y_points = ",y_points)

interpolation = Interpolation(n, x_points, y_points)

x_value = float(input("\nEnter the value of x to interpolate: "))

y_value_f, h_f  = interpolation.forword_interpolation(x_value)
print(f"\nStep size h = {h_f}")
print(f"Forword Interpolated value at x = {x_value} is {y_value_f}")

y_value_b, h_b  = interpolation.backword_interpolation(x_value)
print(f"\nStep size h = {h_b}")
print(f"Backword Interpolated value at x = {x_value} is {y_value_b}")

y_value_dd = interpolation.divided_difference(x_value)
print("\nDivided difference Interploation")
print(f"Divided Difference Interpolation st x = {x_value} is {y_value_dd}")