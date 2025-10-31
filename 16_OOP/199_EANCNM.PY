#In this video we will talk about
#Encapsulation
#Abstraction
#Sone special naming convention
#Name Mangling, __name (not a convention)

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        #self._price = price
        self.__price = price

    def make_a_call(self, phone_name):
        print(f"calling {phone_name} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def send_mesaage(self):
        pass #twilio

phone1 = Phone('nokia','1100',1000)
# print(phone1.__price) #this will not get print
print(phone1._Phone__price)
phone1._Phone__price = -1000
print(phone1._Phone__price)

print(phone1.__dict__)

# phone1._price = -1000
# print(phone1._price)
    
# _name : This means we are trying to tell that is a private datatype
# __name__ : We call this as dunder/magic method