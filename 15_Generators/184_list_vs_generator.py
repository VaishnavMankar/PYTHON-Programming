#list vs generator
#memory usages, time
#When to use list, when to use generator

import time

t1 = time.time()
l = [i**2 for i in range(10000000)] #10 million
t2 = time.time() - t1
print(t2 - t1)

# t1 = time.time()
# g =  (i**2 for i in range(10000000)) #10 million
# t2 = time.time() - t1
# print(t2 - t1)
#gnerator takes one memorry location at one time

# list vs generator. When should we use it.
# we use list when we want to perform operation inside list and you want ot store the data
# If you want a list which you dont wna to use again and again then we use generator 