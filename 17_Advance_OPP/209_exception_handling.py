# Exception handling
# try excption else finallly

while True:
    try:
        age = int(input('Enter your age: '))
        break
    except ValueError:
        print('Maybe you entered string insted of nuber, try again')
    except:
        print("Unexpected error ...")


if age < 18:
    print('you can\'t play this game.')
else:
    print('You can play this game')

