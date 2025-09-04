#lambde Expression practice
def is_even(a):
    return a % 2 == 0

print(is_even(5))


#using lambda expression
is_even2 = lambda a : a%2 == 0
print(is_even2(6))

def last_char(s):
    return s[-1]

print(last_char("Vaishnav"))

last_char2 = lambda n : n[-1]
print(last_char2('Harshit'))

#lambda function with and without using if else statement
def func(stri):
    # if len(num) >5:
    #     return True
    # return False
    return len(stri) > 5

func = lambda strin : True if len(strin) > 5 else False
print(func("abcdef"))
    