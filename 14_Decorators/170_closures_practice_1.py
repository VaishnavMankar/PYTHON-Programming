#function returning function (closure) practice
#first class function
#square

def to_power(x): # x = 3
    def calc_power(n): # n = 3
        return n**x
    return calc_power

cube = to_power(3)
print(cube(2))
        
square = to_power(2)
print(square(4))