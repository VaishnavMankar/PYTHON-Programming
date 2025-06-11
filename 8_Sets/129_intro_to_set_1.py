#set data type
#unordered collection of unique items

s = {1,2,3,4,2}
print(s)
#remove duplicate
l = [1,2,3,4,5,5,5,5,5,6,7,7,7,8]
print(l)
s2 = set(l)
print(s2)
s3 = list(set(l))
print(s3)
s.add(5)
print(s)
s.remove(2) # id the value is not present in the set it will create error 
print(s)

s.discard(7) #even if the value is not present in the set the discard method will not create an error
s.clear()
print(s)

#you cannot store dictionary or list in sets
 