# 4. Write a program to find number of vowels in a string.

a = input("Enter anything here: ")
vowels = 0
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
     vowels += 1
    
print("The number of vowels in the following string are ",vowels)