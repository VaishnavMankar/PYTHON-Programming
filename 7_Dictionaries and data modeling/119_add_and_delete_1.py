#add and delete data
user_info = {
    'name' : "harshit",
    'age' : 24,
    'fav_movie': ['coco','your name'],
    'fav_tunes' : ['little kirshna', 'benten']
}
# how to add  data
user_info['fav_song'] = ['song1','song2']
print(user_info)

#how to delete elements form dictionary
#pop method
popped_item = user_info.pop('fav_movie')
print(f"popped item is {popped_item}")
print(user_info)

#how to delete random element from a dictionary
#popitem method 
popped_element = user_info.popitem()
print(user_info)
print(popped_element)