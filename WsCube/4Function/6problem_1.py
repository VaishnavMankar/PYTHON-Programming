# Write a function to find the maximum of three numbers in Python.
def maximum_num(val1,val2,val3):
    if val1 > val2 and val1 > val3:
        print(val1,"Is the greatest number")
    elif val2 > val1 and val2 > val3:
        print(val2,"Is the greatest number")
    else :
        print(val3,"Is the greatest number")
maximum_num(12,5,9)

# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30.
def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)
        
    return l
print(create_list())

# Write a Python function that takes a number as a parameter and checks if the number is prime or not.
def check_prime(num):
    if num == 1:
        print("It is not a prime number")
    elif num == 2:
        print("It is a prime number")
    else:
        for i in range(2,num):
            if num % i == 0:
                print("It is not a prime number")
                break
            
        else:
            print("It is a prime number")
check_prime(10)    

# Write a Python function to sum all the numbers in a list. 
def addition(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return (total)
print("Sum of all the number in the list is",addition([1,2,3,4,5]))

#solution 2 using recursion 
def add(num):
    if len(num)==1:
        return num[0] 
    else:
        return num[0] + add(num[1:])

print(add([1,2,3,4,5]))

# Write a Python program to solve the Fibonacci Sequence using Recursion.
def fs(num):
    if num == 1:
        return (0)
    elif num == 2:
        return (1)
    else:
        return (fs(num-1)+fs(num-2))
    
print(fs(8))