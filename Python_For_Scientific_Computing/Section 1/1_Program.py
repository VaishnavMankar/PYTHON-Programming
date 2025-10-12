#Define a variable and print its value(int, float, string, boolean)
a = 1
b = 2.34355
c = "Vaishnav"
d = True
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")


#print the data type of the variables
print(f"data type of a is {type(a)}")
print(f"data type of b is {type(b)}")
print(f"data type of c is {type(c)}")
print(f"data type of d is {type(d)}")

#Perform operations on the variavles and print its value
print(f"Addition : {a + b}")
print(f"Subtraction : {a - b}")
print(f"Multiplication : {a * b}")
print(f"Power : {a**b}")
print(f"Float devision : {a/b}")
print(f"Int devision : {a//b}")
print(f"Reminder : {a%b}")

#Use the comparison operators and print the value
print(f"Equal to : a == b {a == b}")
print(f"Not Equal to : a != b {a != b}")
print(f"Greater than : a > b {a > b}")
print(f"Smaller than : a < b {a < b}")
print(f"Greater than or equal to : a >= b {a >= b}")
print(f"Smaller than or equal to : a <= b {a <= b}")

#Use the linput() function to take input from the user
name = input("Enter your name : ")
age = int(input("Enter your age in numbers : "))
height = float(input("Enter your height in cm : "))
is_student = input("Are you a student (True/False) : ")

string = "Hello my namde is vaIShnaV ManKAr and i'm a student"
print(string.lower())
print(string.upper())
print(string.title())
print(string.capitalize())
print(string.count("a"))
print(string.count("a",10,30))
print(string.find("is"))
print(string.replace("VaIShnaV","Varun"))