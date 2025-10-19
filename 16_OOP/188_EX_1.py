# Create a laptop class with attributes like brand name, model name, price
# Create two objects/instances of the laptop class

class Laptop:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = price

laptop1 = Laptop("hp", "lazer", 50000 )
print(laptop1.brand)
