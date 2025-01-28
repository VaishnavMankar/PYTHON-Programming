l1 = [30,40,50,60]

l2 = []
for i in l1:
    if i > 45:
     l2.append(i)
    
print(l2)
print(l1, "\n",l2)

l3 = [i for i in l1]
print(l3)
l4 = [i for i in l1 if i > 45]
print(l4)