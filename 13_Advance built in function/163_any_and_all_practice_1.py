#any and all function

def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
       total = 0
       for nums in args:
           total += nums
       return total
    else:
       return "wrong input"
   
print(my_sum(1,2,3,4,8.9,'harshit',['harshit']))
print(my_sum(1,2,3,4,8.9))