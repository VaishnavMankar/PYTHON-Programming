# 3. Write a program to find a palindrome of integers.

num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    dig = num%10
    rev = rev*10 + dig 
    num = num // 10

if rev == temp:
    print("It is a palindrome")
else : 
    print("It is not a palindrom")