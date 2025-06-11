#some more method to add data in list

#insert method
fruits1 = ['mango','orange']
fruits1.insert(1,'grapes')
print(fruits1)

#how to join(concatenate) two list
fruits2 = ['apple','banaba']
fruits = fruits1 + fruits2
print(fruits)

#extend method
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)

#difference between append and extend method
fruits1.append(fruits2)
print(fruits1)
print(fruits2)

