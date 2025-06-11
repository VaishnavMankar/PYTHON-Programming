fruits = ['orange','apple','peach','banana','kiwi','apple','banana']
#count
print(fruits.count('apple'))

#sort method
fruits.sort() #you cannot write sort methiod in print statement
print(fruits)

numbers = [5,7,6,3,4,2,9,8]
print(numbers.sort()) #it will return None
numbers.sort()
print(numbers)

#sorted function
print(sorted(numbers))
print(numbers)
print(sorted(fruits))

#reverse

#clear
# numbers.clear()
# print(numbers)


#copy
numbers_copy = numbers.copy()
print(numbers_copy)