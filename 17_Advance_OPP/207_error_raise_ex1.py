# raise errrors example 1
# NotImplementedError
# abstract method

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        # return 'meao meao'
        raise NotImplementedError('Your have to define this method in subclasses')

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(seld):
        return "bhow bhow"

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed



dogg = Dog('tomy','pug')
print(dogg.sound())