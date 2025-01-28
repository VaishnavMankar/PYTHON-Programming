# take two comma separated inputs from user
# 1.) user's name
# 2.) a single character

# output - 2 print lines
# 1.) user's name length
# 2.) count the character that user inputed (bonus : case insensitive count )
name,char = input("enter comma seperated name and character: ").split(",")
print(f"length of your name is {len(name)}")
#1. Harshit -> harshit
#2. H -> h
#3. "  Harshit  " -> "Harshit"-> "harshit"
#4. "  H   " -> "H" -> "h"
# name.strip().lower().count(char.strip().lower)
# char.strip().lower
print(f"character cout: {name.strip().lower().count(char.strip().lower())}")
