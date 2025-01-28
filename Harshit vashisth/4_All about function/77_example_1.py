#find greates integer using function
def greatest(a,b):
    if a > b:
        return a
    else:
        return b
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))
bigger = greatest(num1,num2)

print(f"{bigger} is greatest")
