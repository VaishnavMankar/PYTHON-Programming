#Decorators - enhance the functionality of other function 

def decorator_function(any_function):
    def wrapper_function():
        print("This is awesome function")
        any_function()
    return wrapper_function

# This is awesome function
@decorator_function
def func1():
    print('This is function 1')
    
func1()

#This is awesome function
@decorator_function
def func2():
    print('This is function 2')

# func1()
# func2()   

# var = decorator_function(func1)
# var()

# func1 = decorator_function(func1)
# func1()