#common method to delete data from list

fruits = ['orange','apple','peach','banana','kiwi']
#pop method
print(fruits)
fruits.pop(1) #it will delete the element at position at index 1     
print(fruits)

#delete method
del fruits[2]
print(fruits)

#remove
fruits.remove('kiwi')
print(fruits)
