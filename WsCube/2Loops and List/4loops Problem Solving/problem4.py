# 4. Write a program to check if a number is divisible by 8 and 12,up to 100 numbers

for i in range(1,101):
    if i % 8 == 0 and i % 12 == 0:
        print(i)