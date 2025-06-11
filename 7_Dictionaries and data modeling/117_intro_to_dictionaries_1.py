# dictionaries intro
# Q - why we use dictionaries?
# A - Because of limitations of lists, lists are not enough to represent real data.

# Example
user = ['Harshit', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains user name, age, fav movies, fav tunes
# you can do this but this is not a good way to do this.

# Q - what are dictionaries
# A - unordered collections of data in key : value pair.

# how to create dictionaries
user = {'name' : 'Harshit', 'age' : 24}
print(user)
print(type(user))

#second method to create dictionary
user1 = dict(name = "Harshit", age = 24)
print(user1)

#how to access data from dictionary
#NOTE - there is no indexing because of unordered collectgion of data
print(user['name'])
print(user['age']) 

#which type of data a dictionary can stor?
#anything
#number, string, list, dictionary

user_info = {
    'name' : 'Vaishnav',
    'age' : 22,
    'fav_movies' : ['your_name','spirited away'],
    'fav_tunes' : ['little krishna','kal bhrave']
} 
print(user_info)
print(type(user_info))
print(user_info['fav_movies'])

#how to add data to an empty dictionary
user_info2 = {}
user_info2['name'] = 'mohit'
user_info2['age'] = 24
print(user_info2)