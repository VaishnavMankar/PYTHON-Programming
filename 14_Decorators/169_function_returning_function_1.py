#function returning function

def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func
#in the bellow comand we are assining the inner function by assigning the inner function to var
var = outer_func()
var()
#and thats why them we call var() its execute the inner function 

def outer_func2(msg):
    def inner_func2():
        print(f"Messeg is {msg}")
    return inner_func2

var2 = outer_func2("hello there ! ")
var2()