# 3. Write a program to check if a string is palindrome.

a = input("Enter anything here")
rev = a[::-1]

if a == rev:
    print("it is palindrome")
else: 
    print("it is not palindrome")
    