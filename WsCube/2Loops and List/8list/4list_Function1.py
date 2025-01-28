#to find the length of a list
a = ["Thor","Hulk","Ironman","Captian America"]
print(a)
print(len(a))

#to count an occurence of a perticlar element
print(a.count("Thor"))

#to add to the list
a.append("Spiderman")
print(a)

#to add to a specific location
a.insert(1,"Vision")
print(a)

#to remove from a list
a.remove("Vision")
print(a)

#to remove from a certain location 
print(a.pop(1))
print(a)