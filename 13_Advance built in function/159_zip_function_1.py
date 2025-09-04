#zip function
user_id = ['user1','user2','user3']
names = ['harshit','mohit','rohit']
print(list(zip(user_id,names)))
last_name = ['sharma','patil','rathod']
print(list(zip(user_id,names,last_name)))  
#you can convert the list which contain two pair of tuples into dectionary
example = [('a',1),('b',2)]
print(dict(example))