# 1 
# 2 1
# 3 2 1 
# 4 3 2 1
# write a program to display this pattern

for i in range(1,6):
    for j in range(i, 0, -1):
        print(i, end = " ")
    print()