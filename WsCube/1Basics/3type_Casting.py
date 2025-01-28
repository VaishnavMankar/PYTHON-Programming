# name = "joy"
# age = 23
# print (type(age))
# print(type(name))

#implicit type conversion
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))

# c = a+b
# print(c)
# print(type(c))

# a = "123"    tis is s string therefore you cannot add a string with a int 
# b = 1.23                 #you havd to use explicit function to cunvert it 
# print(type(a))
# print(type(b))

# c = a+b
# print(c)
# print(type(c))

#Explicity type conversion
a = "123"
b = 1.234
print(type(a))
print(type(b))

a = int(a)
print("After conversion ",type(a))

c = a+b
print(c)
print(type(c))
