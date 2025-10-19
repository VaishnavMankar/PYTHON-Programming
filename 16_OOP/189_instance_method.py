#instance method
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def above_18(self):
        return self.age > 18
        
p1 = Person("Varun", "Sharma", 89)
print(p1.full_name())
print(p1.above_18())
