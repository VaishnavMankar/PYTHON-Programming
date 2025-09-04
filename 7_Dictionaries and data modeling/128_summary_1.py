#summary dictionary
#what is dictionary
#unordered collection of data

d = {'name' : 'harshit','age': 24}

#or
d1 = dict(name = "vaishnav",  age = 24)

#or
d2 = {
    'name' : 'harshit',
    'age' : 24,
    'fav_movie' : []
}

#how to acess data from your dictionary
#you cannot do like d[0] 
#because there id no ordered inside dictionary

#syntax
#print(dictname[keyname])
print(d['name'])

# add data insight empty dict
empty_dict = {}
empty_dict['key1'] = "value1"
empty_dict['key2'] = "value2"
print(empty_dict)

#check existance of values inside dict
#use in keywords to check for keys
if 'name' in d:
    print("present")

#how to iterate over dictionary 
#most common method 
for key, value in d.items():
    print(f"key is {key} and value is {value}")
    
    
#to print all key
for i in d:
    print(i)
    
#to print values
for i in d.values():
    print(i)
    
#get method
#to acess a key and check it existance
print(d.get('name'))

#Q - why we use get
#A - to get ride of error
# example
print(d['name'])
print(d.get('names'))

#to delete item 
#pop ----> take one argument which is keyname

popped = d.pop('name')
print(popped)
print(d)

#popitem 
popped = empty_dict.popitem()
print(popped)