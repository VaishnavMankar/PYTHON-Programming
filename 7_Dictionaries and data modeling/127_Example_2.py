#Take input from the user an print in dictunary format 
# user = {
#        'name' : 'Harshit',
#        'age' : 22,
#        'fav_movie' : ['coco','your name'],
#        'fav_song' : ['song1','song2']

user = {}

name = input('What is your name: ')
age = input('Enter your age: ')
fav_movies = input('your fav movie seperated by , ').split(',')
fav_songs = input('your fav songs seperated by , ').split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song'] = fav_songs

print(user)

for key, value in user.items():
    print(f"{key} : {value}")