# *args with normal parameter

def multiply_nums(num,*args):
    print(num)
    print(args)
    multiply = 1
    for i in args :
        multiply *= i
    return multiply

print(multiply_nums(1,2,3,4))
