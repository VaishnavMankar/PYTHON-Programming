#scope

x = 5 # global variable 

def fun():
    global x
    x = 7 # local variable
    return x

print(x)
print(fun())
print(x)


print(x)