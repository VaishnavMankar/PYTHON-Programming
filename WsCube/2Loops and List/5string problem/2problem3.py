# 1 1 1 1
# 2 2 2
# 3 3
# 4 
# write a program to display this pattern.
for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end = " ")
    print()