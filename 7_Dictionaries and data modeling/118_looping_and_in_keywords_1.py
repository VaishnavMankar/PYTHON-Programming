#in keywords and iteration in dictionary

user_info = {
    'name' : "Vaishnav",
    'age' : 22,
    'fav_movies': ['coco','your name'],
    'fav_song': ['counting star','let her go']
}

#check if key exist in dictionary
if 'name' in user_info:
    print("present")
else:
    print("not present")

#check if value exist in dictionary
if 'Vaishnav' in user_info.values():
    print("Exist")
else:
    print("Not Exist")

#if you want to search a list the you will have to enter the complete list
if ['coco','your name'] in user_info.values():
    print("Exist")
else:
    print("Not Exist")
    
#loops in dictionaries
for i in user_info:
    print(i)     # this will only print the keys
    
#to print value add the .values function
for i in user_info.values():
    print(i)

user_info_values = user_info.values()
print("üser values: ",user_info_values)
print(type(user_info_values))

user_info_values2 = user_info.keys()
print("user keys: ",user_info_values2)
print(type(user_info_values2))

#printing values using for loop
for i in user_info:
    print(user_info[i])

#items method
user_item = user_info.items()
print(user_item)
print(type(user_item))

#[('name' , "Vaishnav"),('age' : 22),('fav_movies': ['coco','your name']),('fav_song': ['counting star','let her go'])

for keys, value in user_info.items():
    print(f"key is {keys} and values is {value}")
    print(keys)
    print(value)
#you can declare any variable name in the for loop like i and j not just keys and values
   