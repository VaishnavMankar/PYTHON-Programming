#Datetiem
import datetime
x = datetime.datetime.now()
print(x)

y = datetime.datetime(1997,10,14)
print(y)
print(y.strftime("%a")) #day in 3 letter
print(y.strftime("%A")) #day in all letter
print(y.strftime("%B")) #month in all letter
print(y.strftime("%b")) #mon in three letterr
print(y.strftime("%m")) #month in nummber
print(y.strftime("%Y")) #year in 4 digit
print(y.strftime("%y")) #year in last 2 digitt

#random
import random 

print("Random")
y = random.randint(1,10)
print(y)

#math
import math

print("Math")
z = max(16,67,45)
print("The maximum value is",z)
a = min(25,67,9)
print("The minimum value is",a)

b = pow(2,4)
print(b)

c = math.sqrt(256)
print(c)

d = abs(-12.346)
print(d)

k = math.ceil(2.4)
print(k)
m = math.floor(2.4)
print(m)