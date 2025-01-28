
# 1. Write a program to find a sum of all the even numbers up to 50.

sum = 0
for i in range (1,51):
    if i % 2 == 0:
        sum += i
       
print("the sum of all even number fron 1 to 50 is = ",sum)