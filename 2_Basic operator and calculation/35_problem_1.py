# take two comma separated inputs from user
# 1.) user's name
# 2.) a single character

# output - 2 print lines
# 1.) user's name length
# 2.) count the character that user inputed (bonus : case insensitive count )
name,char = input("enter comma seperated name and character: ").split(",")
print(f"length of your name is {len(name)}")
print(f"character cout: {name.lower().count(char.lower())}")

#print(f"the character count is {name.lower().count(char)}")