#num = 1234
#calculate sum of digit ---> 1 + 2 + 3 + 4

total = 0
num = input("Enter the number: ")
for i in range(0,len(num)):
    total += int(num[i])
    
print(total)
