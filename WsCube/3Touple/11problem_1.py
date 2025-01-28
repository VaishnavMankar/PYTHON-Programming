# Write a program to find max and min in a set.
a = {12,56,34,8,90,1,57}
maximum = max(a)
minimum = min(a)
print("The maximum vlue in the iset is ",maximum)
print("The minimum value in the set is ",minimum)

# Write a program to find common elements in three lists using sets.
b = [1,5,6,8,2]
c = [4,5,6,7]
d = [1,9,6,2,5]

print("The common element in the given three list are ",set(b) & set(c) & set(d))
# Write a program to find the difference between two sets.
e = {1,5,6,8,2}
f = {1,9,6,2,5}
print(e.difference(f))

# Write a Python program to remove an item from a set if it is present in the set.
g = {1,5,6,8,2}
g.discard(8)
print(g)

# Write a Python program to check if a set is a subset of another set.
h = {1,2,3,4,5,6}
i = {2,3,4}
print(i.issubset(h))