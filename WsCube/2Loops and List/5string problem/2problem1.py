# 1
# 1 2
# 1 2 3
# 1 2 3 4
# write a program to display this pattern.

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = " ")
        #print("*",end = " ")
    print()