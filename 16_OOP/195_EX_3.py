#Write a python code in which declare a class instance variable that keep the track of number of time the constructor is called.
class Person:
    count_instance = 0  # class variable to keep track of number of instances
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1  # increment the count whenever a new instance is created
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
       
p1 = Person('John', 'Doe', 30)
p2 = Person('Jane', 'Smith', 25)
print("Number of Person instances created:", Person.count_instance)