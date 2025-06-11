#we use enumerate function with for loop to track position of our 
#item in iterable

#How we can do this without enumerate function
name = ['abc','abcdef','harshit']
#0 -- 'abc'
#1 -- 'abcdef'
pos = 0
for i in name:
    print(f"{pos} ----> {i}")
    pos += 1
    
#with enumerate function   
for pos, i in enumerate(name):
    print(f"{pos} -----> {i}")

#Define a function which takes two arguments
# 1) list conatining string
# 2)String that you want to find in your list
# and this function will return the index of string in your list and
# if string in not present then return -1

def find_pos(l,target):
    for pos, names in enumerate(l):
        if names == target:
            return pos
    return -1 

print(find_pos(name,"harshit"))