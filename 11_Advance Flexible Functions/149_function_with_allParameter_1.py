#function with all parameters
#very important to understand

#PADK

#parameters
#*args
#default parameters
#**kwargs

def func(name = 'unknown',age = 24):
    print(name)
    print(age)
    
func()
func("",26)
func("harshit",47)

def func2(name,*args,last_name = "unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
    
func2('harshit',1,2,3,4, a = 1, b = 5)