#iteration in dictionaries
Student={"name":"John","class":"6th","roll_no":23}
# print(Student["name"])

# #print all the key names one by one
# for x in Student:
#     print(x)
    
# #print all the value names one by one
# for x in Student:
#     print(Student[x])
    
#using value function
# for x in Student.values():
#     print(x)
    
#using item funnction
for x,y in Student.items():
    print(x,y)