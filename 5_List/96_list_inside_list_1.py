# list inside list
matrix = [[1,2,3],[4,5,6,],[7,8,9]]
print(matrix[0])
print(matrix[1])
print(matrix[2])

print()

for i in matrix:
    print(i)
    
print()

for i in matrix:
    for j in i:
        print(j)
        
print()

print(matrix[1][1])

s = "string"
print(type(s))
print(type(matrix))