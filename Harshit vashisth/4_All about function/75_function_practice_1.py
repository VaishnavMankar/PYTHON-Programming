#function practice
def last_char(name):
    return name[-1]

print(last_char("Vaishnav"))

# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     else:
#         return "odd"
    

def odd_even(num):
    if num%2 == 0:
        return "even"
    return "odd"

print(odd_even(10))

def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(9))


def inShort_even(number):
    return number%2 == 0

print(inShort_even(7))

def songs():
    return "The last time we met"

print(songs())