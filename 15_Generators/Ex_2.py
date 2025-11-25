#Generator that yields squares of numbers from 1 to N.
def square_root(n):
    for i in range(1,n):
        yield i**2

for i in square_root(10):
    print(i)

square = (i**2 for i in range(1,11))
for i in square:
    print(i , end = " ")