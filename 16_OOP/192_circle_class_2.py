class Laptop:
    discount_percent = 10  # class variable
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = price
        
    def apply_discount(self):
        off_price = (Laptop.discount_percent/100) * self.price
        return self.price - off_price

laptop1 = Laptop('HP','au114tx', 63000)
print(laptop1.apply_discount())

laptop2 = Laptop('Dell','inspiron', 75000)
print(laptop2.apply_discount())   