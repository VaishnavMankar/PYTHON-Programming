# def decorator_function(any_function):
#     def wrapper_function():
#         print("This is awesome function")
#         any_function()
#     return wrapper_function

# # This is awesome function
# @decorator_function
# def func1(a):
#     print('This is function 1')
# func1()

#this will not work because out rapper function is not taking value in decorator function
#if ve have values in our function we should use *args and **kwargs

def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        print("This is awesome function")
        any_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print(f"This is a function with argument {a}")
    
func('abcd')

def decorator_function2(any_function):
    def wrapper_function(*args,**kwargs):
        print("This is awesome function")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function2
def add(a,b):
    return a+b

print(add(2,3))
