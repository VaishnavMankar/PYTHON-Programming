def add(*args):
    total = 0
    for i in args:
        total += i
    return total
print(add(1,2,3,4,5))

l = [1,2,3,4,5,6,7,8,9]
print(add(*l)) #we use star to unpack touple or list 


#kwargs - keyword argument
def fun(**kwargs):
    print(kwargs)
    print(type)
    
fun(name = 'Vaishnav' , last_name = 'Mankar')

#kwargs, args, normal, default
#PADK -> parameter, args, default, known

def fun2(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
    
fun2('harshit',1,2,3,4, a = 1, b = 4)