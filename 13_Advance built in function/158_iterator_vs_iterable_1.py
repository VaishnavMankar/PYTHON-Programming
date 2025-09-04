#iterator vs iterables

numbers = [1,2,3,4,5] #iterables
square = map(lambda a:a**2,numbers)#iterator
print(square)

for i in numbers:
    print(i)
    