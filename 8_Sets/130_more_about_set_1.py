# in keywords in sets and from loop
s = {'a','b','c'}

#in keywords to check if item is present or not in set
if 'a' in s:
    print("present")
else:
    print("not Present")

#for loop
for item in s:
    print(item)
    
#set operation 
#union
#intersection
s1 = {1,2,3,4}
s2 = {3,4,5,6}

union_set = s1 | s2
print(union_set)

intersection_set = s1 & s2
print(intersection_set)