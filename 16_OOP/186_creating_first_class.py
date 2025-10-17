# OBJECTIVE
# WHAT IS CLASS
# HOW TO CREATE A CLASS
# WHAT IS INIT METHOD
# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES
# HOW TO CREATE OUR OUR OBJECT

class Person:
    def __init__(self, first_name, last_neme, age):
        # instance variables 
        print("init method // constructor gets called automatically when object is created")
        self.first_name = first_name
        self.last_name = last_neme
        self.age = age

p1 = Person("Varun", "Sharma", 34)
p2 = Person("Aditya", "Gupta", 23)
            
print(p1.first_name)
print(p2.first_name)