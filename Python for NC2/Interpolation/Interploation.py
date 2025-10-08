#read the data from the txt file asns store it 
with open("input.txt","r") as f:
    lines = f.read().splitlines()

#first line is n
n = int(lines[0])

#next n lines are x_points
x_points = [float(lines[i]) for i in range(1,n+1)]

y_points = [float(lines[i]) for i in range(n+1, 2*n+1)]

print("number of elemnents (n):",n)
print("x_points =",x_points)
print("y_points =",y_points)


