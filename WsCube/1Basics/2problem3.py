# 3 Write a program to create area calculator.

print("************AREA CALCULATER***************")
print("""Press 1 to get the area of square
      Press 2 to get area of rectangle
      Press 3 to get area off circle
      press 4 to get area of triangle""")

choice = int (input("Enter a number between 1-4: "))

if choice == 1:
    side = float(input("Enter the length of one side"))
    area = side**2
    print("The area of square is ",area)

elif choice == 2:
    length = int(input("Enter the length of the rectangle: "))
    Width = int(input("Enter the width of the rectangle: "))
    area = length*Width
    print("The area of rectangle is: ",area)
    
elif choice == 3 : 
    radius = float(input("enter the radius of the circle"))
    area = ((22/7)*(radius**2))
    print("the area of the circle is ",area)
    
elif choice == 4:
    base = float(input("enter the base of the triangle: "))
    hight = float(input("enter the hight of the triangle: "))
    area = 0.5*base*hight
    print("The area of the triangle is ",area)
    
else:
    print("invalid umber")