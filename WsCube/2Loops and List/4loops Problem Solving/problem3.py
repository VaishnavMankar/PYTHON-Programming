# 3. Write a program to find sum of first 10 odd numbers using while loop.

sum = 0
n = 0
while n <= 20:
    if n % 2 != 0:
        sum += n
    n += 1
    
print("sum of furst 10 odd numbers is: ",sum)