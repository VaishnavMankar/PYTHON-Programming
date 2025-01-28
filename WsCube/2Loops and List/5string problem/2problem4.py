#    *
#   **
#  ***
# ****
#Write a program to display this pattern.

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end = " ")
    for k in range(i):
        print("*", end = " ")
    print ()    
    