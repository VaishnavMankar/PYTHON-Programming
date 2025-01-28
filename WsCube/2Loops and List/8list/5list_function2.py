#to create a copy of a list
a = ["Thor","Hulk","Ironman","Captian America"]
b = []
print(b)
b = a.copy()
print(b)

#to access an element
print(a.index("Hulk"))

#to entend the list
c = ["Vision","Spiderman"]
a.extend(c)
print(a)

#to reverse the list
a.reverse()
print(a)

#to sort the list
a.sort()
print(a)

d = [7,2,4,5,9,]
d.sort()
print(d)

#to clear all the data in the list
a.clear()
print(a)