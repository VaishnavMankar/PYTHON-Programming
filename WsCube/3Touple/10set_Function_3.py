a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor"}

#union
print("Union")
print(a.union(b))

#Difference
print("difference")
print(a.difference(c))

#Difference Update
# print("difference update")
# a.difference_update(c)
# print(a)

#intersection
print("intersection")
print(a.intersection(c))

#intersection update
# print("intersection_update")
# a.intersection_update(c)
# print(a)

#symmetric Difference 
print("Symmetric Difference")
print(a.symmetric_difference(c))

#symmetric Difference Update
print("Symmetric difference update")
a.symmetric_difference_update(c)
print(a)