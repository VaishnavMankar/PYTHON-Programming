#map function 

numbers = [1,2,3,4]

def square(a):
    return a**2

square1 = list(map(square,numbers))
print(square1)


#using lambda function 
square2 = list(map(lambda a : a**2, numbers))
print(square2)

#using listy comprehension
square3 = [i**2 for i in numbers]
print(square3)

new_list = []
for nums in numbers:
    new_list.append(square(nums))
print(new_list)

names = ['abc','abcpq','dfgh']
length = map(len,names)
for i in length:
    print(i)