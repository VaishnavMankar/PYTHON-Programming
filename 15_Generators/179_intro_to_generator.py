#generators
#generators are iterators

#iterators, iterable

l = [1,2,3,4] #iterable

for i in l:
    print(i)

i = iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for num in map(lambda a:a**2, l):       #iterator
    print(num)