# can we derive more than one class from base class ?
# Multilevel inheritance
# method resolution order
# method overriding
# isinstance(), issubclass()

class Phone: # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"
        
    def make_a_call(self, number):
        return f"calling {number}...."
    
class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        #two ways
        #Phone.__init__(self, brand, model_name, price) #uncoman Way
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

class FlagshipPhone(SmartPhone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera
    
    
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} adn fromt_camara = {self.front_camera}"

phone = Phone('nokia','1100', 1000)
smartphone = SmartPhone('onePlus','5',30000,'6 GB', '64 GB', '20 MP')
print(phone.full_name())
print(smartphone.full_name())

onePlus = FlagshipPhone('onePlus','5',30000,'6 GB', '64 GB', '20 MP','16 MP')
print(onePlus.full_name())

# print(help(smartphone)) # helps you to tell which child class is inherited from which parent class

print(isinstance(onePlus,FlagshipPhone)) # isinstance tell out that wether the object belongs to the class or not
print(isinstance(onePlus,Phone))

print(issubclass(FlagshipPhone,Phone)) # issubclass tells ous that wether the class is a chind class of the perticular perent class or not

