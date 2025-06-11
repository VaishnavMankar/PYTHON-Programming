#ask a user for name
#Example = harshit vashisth
# harshit
# name.count("h") , name.count(name[0]) = 2
# name.count("a") , name.count(name[1]) = 1
# name.count("r") , name.count(name[2]) = 1
# name.count("s") , name.count(name[3]) = 1
# name.count("h") , name.count(name[4]) = 2
# name.count("i") , name.count(name[5]) = 1
# name.count("t") , name.count(name[6]) = 1

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

name = input("Enter your name: ") 
temp_var = "" 
i  = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1  