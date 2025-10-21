class Laptop:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = price
        
    def apply_discount(self, num):
        off_price = (num/100) * self.price
        return self.price - off_price

laptop1 = Laptop('HP','au114tx', 63000)
print(laptop1.apply_discount(10))

laptop2 = Laptop('Dell','inspiron', 75000)
print(laptop2.apply_discount(15))