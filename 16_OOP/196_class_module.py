# class methods
# difference between class method and instance method

class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @classmethod
    def count_instances(cls):
        # return f"You have created {cls.count_instance} instances of person class"
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def above_18(self):
        return self.age > 18
        
p1 = Person("Varun", "Sharma", 89) # instances 1
p2 = Person("John", "Doe", 25) # instances 2
print(p1.full_name())
print(p1.above_18())

print(Person.count_instances())