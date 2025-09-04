# name = input("enter you name: ")
# age = input("Enter your age: ")

#insteg taking input in multiple line take input in single line

name,age = input("Enter your name and age ").split() #here the split is defile by space
print(name)
print(age)

name2,age2 = input("Enterr your name and afge ").split(",")
print(name2)
print(age2)