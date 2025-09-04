from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper(*args,**kwars):
        print(f"you are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwars)
    return wrapper
    

@print_function_data
def add(a,b):
    '''This function takes two number as argument and return their sum'''
    return a+b

print(add(4,5))
#output 
#you are calling add function
#This function takes two numbers as parameter and return their sum
#9