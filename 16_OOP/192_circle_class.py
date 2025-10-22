#class Variable
#circle
#area
#circle

class Circle:
    # def __init__(self, randius, pi):
    #     self.randius = randius
    #     self.pi = pi
    pi = 3.14
    def __init__(self, randius):
        self.randius = randius
    def calc_circumference(self):
        return 2 * self.pi * self.randius
    
# c1 = Circle(4,3.14)
# c2 = Circle(5,3.14)
c1 = Circle(4)
print(c1.calc_circumference())
