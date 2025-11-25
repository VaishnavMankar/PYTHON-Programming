#You have to have a complete understanding of function,
#first class function/closures
#then finally we will learn about decorators

def square(a):
    return a**2

s = square(5)
print(s)
#usind decorators
f = square
print(f(6))
print(f(8))
print(f.__name__)
print(square.__name__)  
print(f)
print(square)