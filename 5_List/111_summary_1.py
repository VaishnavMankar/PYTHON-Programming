#list chapter summary
#list is a data structure that can hold any type of data

#create a list
words = ['word1','word2']

#you can store anything inside list
mixed = [1,2,3,[4,5,6],'seven',8.00001,None]
print(mixed)

#list is ordered collection of items
print(mixed[0]) 
print(mixed[3])
print(mixed[4])

#add data to our list
#append method

mixed.append('10')
print(mixed)

mixed.append([20,30,40])
print(mixed)

mixed.extend([50,60,70])
print(mixed)

#join two list
#l = l1 + l2

#insert at perticulat index
mixed.insert(1,"at_first_position")
print(mixed)

#remove data from list
popped = mixed.pop() #remove last item
print(popped)
print(mixed)

#remove element from perticular position
print(mixed)
popped2 = mixed.pop(1)
print(mixed)
print(popped2)

#remove method is used when you dont know the position 
mixed.remove('seven')
print(mixed)

#del statement 
#is use to delete element form list
del mixed[3]
print(mixed)

#loops in list 
for i in mixed:
    print(i)