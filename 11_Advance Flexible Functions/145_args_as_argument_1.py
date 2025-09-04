def multiply_num(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply
#how to use *  as an argument

print(multiply_num(2,3))

nums = [1,2,3]
print(multiply_num(*nums)) #whenever you want to pass a list tupe * in frunt of variable name
#this in known as unpacking 
#this will pass element