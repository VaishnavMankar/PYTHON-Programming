a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor"}

#isdisjoint       check if there is any common element or not if its there is comon element the false & if there is no common the true
print("IsDisjoint")
print(a.isdisjoint(b))
print(a.isdisjoint(c))

#issubset
print("IsSubset")
print(a.issubset(b))
print(a.issubset(c))
print(c.issubset(a))

#issuperset
print("IsSuperset")
print(a.issuperset(c))

#update
a.update(c)
print(a)

#clear
a.clear()
print(a)