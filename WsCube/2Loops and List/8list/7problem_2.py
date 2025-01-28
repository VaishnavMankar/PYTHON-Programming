# B = [13, 7, 12, 10]
# 1. Write a program to multiply all the numbers in the list. 

B = [13, 7, 12, 10]
mul = 1
for i in (B):
    mul *= i
print(mul)

# 2. Write a program to get the largest number from the list. 
# 3. Write a program to get the smallest number from the list.
B.sort()    #Arranging the list in ascending order
print(B)
print("The largest value in the given list is",B[-1])
print("The smallest value in the givn list is ",B[0])
