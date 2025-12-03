def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        #print('you cannot divide a number by zero')
        print(err)
    except TypeError as err:
        print('Number must be int or floats')
    except:
        print("Unexpected error")


print(divide(2,4))
print(divide(2,0))
print(divide(2,'a'))