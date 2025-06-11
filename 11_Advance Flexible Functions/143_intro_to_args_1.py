# make flexible function 
# *args -- also called as
# *operator


#write a code to add all the codes
def all_total(*args):
    print(args)  # it will convert into tuple
    print(type(args))
    total = 0
    for i in args:
        total += i
    return total

print(all_total(1,2,3,4,5,6,7,8,9))