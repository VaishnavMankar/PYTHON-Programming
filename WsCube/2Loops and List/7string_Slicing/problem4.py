# 4. Write a program to create an area calculator.

print("************AREA CALCULATER***************")
while True: 
 print("""Press 1 to get the area of square
      Press 2 to get area of rectangle
      Press 3 to get area off circle
      press 4 to get area of triangle""")

 choice = int (input("Enter a number between 1-4: "))

 if choice == 1:
     while True:
      side = float(input("Enter the length of one side "))
      area = side**2
      print("The area of square is ",area)
      repeat = input("do you want to try again with square")
      if repeat == "no":
       break

 elif choice == 2:
     while True:
      length = int(input("Enter the length of the rectangle: "))
      Width = int(input("Enter the width of the rectangle: "))
      area = length*Width
      print("The area of rectangle is: ",area)
      repeat = input("do you want to try again with rectangle")
      if repeat == "no":
        break
 elif choice == 3 :
     while True: 
      radius = float(input("enter the radius of the circle"))
      area = ((22/7)*(radius**2))
      print("the area of the circle is ",area)
      repeat = input("do you want to try again with circle")
      if repeat == "no":
        break
    
 elif choice == 4:
     while True: 
      base = float(input("enter the base of the triangle: "))
      hight = float(input("enter the hight of the triangle: "))
      area = 0.5*base*hight
      print("The area of the triangle is ",area)
      repeat = input("do you want to try again with triangle")
      if repeat == "no":
        break
 else:
    print("invalid umber")
    
 repeat1 = input("do you want to repeat the menu again? ")
 if repeat1 == "no":
     break