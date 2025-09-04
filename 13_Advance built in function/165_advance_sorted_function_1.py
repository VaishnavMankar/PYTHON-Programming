#sort function ....on list
fruits = ['grapes','mango','apple']
fruits.sort()
print(fruits)

#you cannot use sort in tuples
fruits2 = ('grapes','mango','apple')
# fruits2.sort()
print(fruits2)
#you can use sorted function but remember tuple are imutable
print(sorted(fruits2))

#sort on sets (you aslo cannot sort on dictionary)
fruits3 = {'grapes','mango','apple'}
print(sorted(fruits3))

guitars = [
    {'model': 'yamaha f310', 'price': 8400},
    {'model': 'faith naptune', 'price': 50000},
    {'model': 'faith apollo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 450000}
]

print(sorted(guitars, key= lambda d:d['price']))  #assending 
print(sorted(guitars, key= lambda d:d['price'], reverse=True)) #decending 

#you can also store this in a variable 
sorted_list = sorted(guitars, key= lambda d:d['price'])
print(sorted_list)