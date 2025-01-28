# 2.Write a program to swap two variables.
#method 1
x = 12
y = 13

temp = x
print("temp = ",temp)
x = y 
print("x = ",x)
y = temp
print("y = ",y)

print(x , y)

#method2
a = 30
b = 40
print("a = ",a)
print("b = ",b)

#left,right = right,left
a,b = b,a

print(a,b);

