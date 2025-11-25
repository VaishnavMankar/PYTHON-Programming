#will discuss three problems in existing
#then will solve them using getting, setter decorator

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0
        self._price = max(price, 0)
        #self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def complete_specification(self):
            return f"{self.brand} {self.model_name} and price is {self._price}"


    # getter(), setter()
    @property  #This is our Getter
    def price(self):
        return self._price
    #If you dont want user the changet the value of any data menber then we use getter and setter
    @price.setter # This is our setter
    def price(self, new_price):
        self._price = max(new_price, 0)
    

    def make_a_call(self, phone_name):
            print(f"calling {phone_name} ...")

    def full_name(self):
            return f"{self.brand} {self.model_name}"
        

phone1 = Phone('nokia','1100',1000)
print(phone1.brand)
print(phone1.model_name)
phone1._price = 500
print(phone1._price)

#print(phone1.complete_specification())
print(phone1.complete_specification)