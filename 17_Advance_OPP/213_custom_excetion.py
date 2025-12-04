# python custom exceptions
# Q - why custom exception ?
# A - To incease the readability of code


# example
class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        raise NameTooShortError('name is to short')


username = input('Enter your name: ')
validate(username)
print(f'hello {username}')