# string
name = "Vaishnav"
#string slicing 
print(name[0:4])
print(name[:-1])
print(name[::-1])
print(name[::2])

#taking two user input
# user_name, age = input("enter your name and age : ").split()
# print(user_name)
# print(age)

#len function
print(len(name))

#lower,upper and tiale method
print(name.lower())
print(name.upper())
print(name.title())

#finding element in an string
a_pos = name.find("a")
a_pos_2 = name.find("a",a_pos+1)
print(a_pos_2)

#center method
print(name.center(len(name)+8,"*"))

#replace methid
print(name.replace("V","H")) 