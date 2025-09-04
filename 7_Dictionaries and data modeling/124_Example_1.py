#exercise
#define a function that takes a number(n)
#return a dictionary containing cube of numbers fro 1 to n

#example
#cube_finding(3)
#{1:1,2:8,3:27}
 
#cube finding
def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes

print(cube_finder(10))