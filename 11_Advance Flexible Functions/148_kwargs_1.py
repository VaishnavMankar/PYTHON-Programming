#kwargs (keywords arguments)
# **kwords(double star operator)

#This is use to print the data as dictionary
def func(**kwargs):
    print(kwargs)
    
def func2(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
    
func(first_name = "Vaishnav", last_name = "Mankar")
func2(first_name = "Vaishnav", last_name = "Mankar")

d = {'name': 'Harshit','age':22}
func(**d)