# 2. Write a program to check if a number is prime or not.
# 3. Write a program to find a palindrome of integers.
# 4. Write a program to create an area calculator.

num = int(input("Enter a number here: "))

if num <= 1:
    print("It is not a prime numner")
else: 
    for i in range(2,num):
        if num % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number") 
            