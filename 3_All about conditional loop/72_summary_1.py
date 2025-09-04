#if statement
name = "harshit"
if name == "harshit" or name == "Harsshit":
    print("you are harshit")
elif name == "Mohit" or "mohit":
    print("You are mohit")
else:
    print("you are not harshit ether mohit")

#while loop
i = 0
while i < 10:
    print("hello world!")    
    i += 1
    
#for loop
for j in range(0,11,2):
    print(j)
    
    
#break keyword
for k in range(1,11):
    if k == 5:
        break
    print(k)
    
#continue keyword
for i in range(1,11):
    if i == 5:
        continue
    print(i)
    