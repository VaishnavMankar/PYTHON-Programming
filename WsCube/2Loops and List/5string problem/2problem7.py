# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 15

for i in range( 1,11):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()