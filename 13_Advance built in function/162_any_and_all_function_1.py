#any, all function
numbers1 = [2,4,6,8,10]
numbers2 = [1,2,3,4,5,6]

#write a code for numbers1 if number is even store True delse sotre false

evens1 = []
for nums in numbers1:
    evens1.append(nums%2==0)
    
print(evens1)

print(all([True,True,True,True]))
print(all([True,True,False,True]))
print(all([num%2 == 0 for num in numbers1]))
print(any([number%2 == 0 for number in numbers2]))