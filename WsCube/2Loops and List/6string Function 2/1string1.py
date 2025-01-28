a = "Harry Potter and Goblin of Fire"
print(a)

#To find length of the string 
print(len(a))

#To find the number of time a character is occuring
print(a.count("0"))

#To cunvert each letter into upper case
print(a.upper())

#To cunvert each letter into lower case
print(a.lower())

#To find the index of any character
print(a.index("o"))
    # to find the character in perticular range
print(a.find("o",15,34))

#To cunvert the first letter to capital 
print(a.capitalize())  #This comand only makes thee first letter capital of the string not all

#To cunvert the string into lower case
print(a.casefold())      #this comand convert every letter into lower case

#To find index number of  an character
print(a.find("o",15,35))

#To write variable inside a string
name = "John"
age = 22
b = "My name is {}, and my age is {}"
print(b.format(name, age))

#It fills the given characters and centralizes a string
print(name.center(20))