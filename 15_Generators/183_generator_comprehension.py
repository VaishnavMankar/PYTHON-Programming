square = [i**2 for i in range(1,11)]
print(square)

#doint same thing with generator

square_2 = (i**2 for i in range(1,11))
print(square_2)
for num in square_2:
    print(num)

for num in square_2: # even if you run the loop two tiem it will not work
    print(num)       # the number comes only one time in the memmory 



square_3 = (i**2 for i in range(1,11))
print(next(square_3))
print(next(square_3))
print(next(square_3))
print(next(square_3))
