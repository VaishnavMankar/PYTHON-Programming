# special magic methods / Dunder method
# Operator overloading
# polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price, 0)

    def phone_name(self):
        return f"{self.brand} {self.model}"
    
    #str, repr
    def __repr__(self):
        return f"Phone(\'{self.brand}\',\'{self.model}\',\'{self.price}\')"
    
    def __str__(self):
        return f"{self.brand} {self.price} {self.model}"
    

    
my_phone = Phone('Nokia','1100',1100)
print(my_phone) # This doesnt print our object for this we use str and repr
print(repr(my_phone))
print(str(my_phone))
print(my_phone.__repr__())