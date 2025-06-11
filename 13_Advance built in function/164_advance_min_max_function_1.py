#advance min() and max()

numbers = [1,2,3,4,5,6]
print(min(numbers))

names = ['Harshit','mohit','ab']
#write a code which can find the name with largest length
def func(item):
    return len(item)

print(max(names, key = func))
print(min(names, key = func))

student1 = [
    {'name' :'harshit' , 'score': 90 , 'age':24},
    {'name' :'mohit' , 'score': 70 , 'age':19},
    {'name' :'rohit' , 'score': 60 , 'age':23}
]

print(max(student1,key= lambda item:item.get('score')))
print(max(student1,key= lambda item:item.get('score'))['name']) 

student2 = {
    'harshit':{'score':90,'age':24},
    'mohti':{'score':75,'age':19},
    'rohit':{'score':76,'age':23}
}

print(max(student2,key = lambda item: student2[item]['score']))