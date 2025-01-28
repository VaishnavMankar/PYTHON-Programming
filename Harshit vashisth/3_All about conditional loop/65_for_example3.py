#ask a user for name
#Example = harshit vashisth
#print count of each word
#output:
#  H : 1
#  a : 2
#  r : 1
#  s : 3
#  h : 3
#  i : 2
#  t : 2
#    : 1
#  v : 1

name = input("Enter your name")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]
        