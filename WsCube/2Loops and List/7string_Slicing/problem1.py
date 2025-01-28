# 1. Write a program to get Fibonacci series up to 10 numbers.

a = 0
b = 1

print(a)
print(b)
for i in range (2,11):
 c = a+b
 a = b
 b = c
 print(c)