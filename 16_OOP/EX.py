class Laptop:
    discount_percent = 10  # class variable
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = price
        
    def apply_discount(self):
        off_price = (self.discount_percent/100) * self.price
        #we use self so that we can change the value of class variable for specific object
        #otherwise if we want the class variable value to be same we use class name like Laptop.discount_percent
        return self.price - off_price
     
#You can change the class variable value like this 
#Laptop.discount_percent = 0

laptop1 = Laptop('HP','au114tx', 63000)
print(laptop1.apply_discount())


#This will help you to see all the instance variables of an object
print(laptop1.__dict__)

laptop2 = Laptop('Dell','inspiron', 75000)
print(laptop2.apply_discount())   
