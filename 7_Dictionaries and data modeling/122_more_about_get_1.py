#more about get, two same keys in dictionaries
user = {'name':'harshit','age': 24,'age': 35}
print(user.get('name'))
print(user.get('names'))
print(user.get('names','not found!'))
print(user.get('age'))
#there cannot be two keys with the same name when you print the keys which are present two time
#the key at the last index will be present 
#this is known as over heading 
