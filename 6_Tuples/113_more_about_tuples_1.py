#looping in tuples
#tuple with one element
#tuple without parenthesis
#tuple unpecking
#list inside tuple
#some function that you can use with tuple

mixed = (1,2,3,4,5,6)

#For loop and tuple
for i in mixed:
    print(i)
#NOTE - you can use while loop to 

#tuple with one element
nums = (1)
num2 = (1,)  # to create a tuples of single element you need to add , after the element otherwise it will not be the tuple
print(type(num2))
words = ('word1')
print(type(nums))
print(type(words))
print(type(mixed))

#Tuple without parenthesis
guitars = 'yello', 'baton rouge', 'taylor'
print(type(guitars))
#you can create tuple without using round bracket

#Tuple unpacking
guitarist = ('Maneli Jamal','Eddie van Der Meer','Andrew Foy')
guitarist1,guitarist2,guitarist3 = (guitarist)
print(guitarist1)

#list inside tuples
favorites = ('southern magnolie',['Tokyo ghoul them','landscape'])
favorites[1].pop()
favorites[1].append("We made it")
print(favorites)

#min, max, sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))