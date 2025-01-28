# 5. Write a program to check if a number is a single digit nur, 2-digit number and so on.., up to 5 digits.
num = int(input("Enter a number you wan"))

if num >= 0 and num <= 9:
    print("it is a single digit umber")
    
elif num >= 10 and num <= 99:
    print("it is a double digit umber")
    
elif num >= 100 and num <= 999:
    print("it is a triple digit umber")
    
elif num >= 1000 and num <= 9999:
    print("it is a four digit umber")

else:
    print("at list five digit number or more")
    