# "Ask user to input 3 numbers and you have to print the average of three
# numbers using string formatting.

# Bonus: try to take all three comma-separated inputs in one line."

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print(f"The average of three number are: {(num1+num2+num3) / 3}")

num4,num5,num6 = input("Enter three number ").split(",")
print(f"Teh average of 3 values are {(int (num4) + int (num5)+ int (num6))/3}") 