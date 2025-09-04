#fromkeys
d = {'name':'unknown','age': 'unknown'}
print(d)

e = dict.fromkeys(['name','age','hight'],'unknown')
print(e)

f = dict.fromkeys(('name','age','hight'),'unknown')
print(f)

g = dict.fromkeys("abc",'unknown')
print(g)

h = dict.fromkeys(range(1,11),'unknown')
print(h)

i = dict.fromkeys(['name','age'],['unknown_name','unknown_age'])
print(i)

 #get method(useful)
j = {'name':'Harshit','age':'unknown'}
#print(j['names']) this will produce an error
#therefore insted of this we use get method
print(d.get('names')) #this will not create an error this will return just return a null value

#how to clear the dictionary or make it empty
j.clear()
print(j)

#how to make a copy of all the elements
d1 = d.copy()
print(d1)