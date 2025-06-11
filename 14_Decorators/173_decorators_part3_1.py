from functools import wraps
def decorator_function2(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        '''This is wrapper function'''
        print("This is awesome function")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function2
def add(a,b):
    '''This is add function'''
    return a+b
print(add.__doc__)
print(add.__name__)