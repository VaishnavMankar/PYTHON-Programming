#replace() method
#find() method

string = "he is smart and he is a good dancer"
print(string.replace(" ","_"))
print(string.replace("he","He"))
print(string.replace("he","He",1))

# find() method 
print(string.find("is",6))
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1 + 1)
print(is_pos2)