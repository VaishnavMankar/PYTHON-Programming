#split method
#convert string to list

user_info = "harshit 22".split()
print(user_info) #convert string into list

user_info_2 = "Vaishnav,23".split(',')
print(user_info_2)

name,age = input("Enter your name and age: ").split()
print(name)
print(age)

#join method 
#convert list to string
user_info_3 = ['varun','21']
print(','.join(user_info_3)) 