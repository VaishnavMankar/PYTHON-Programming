def fibonacci_seq(n):
    a = 0#first number
    b = 1#second number
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b # c = 1
            a = b # a = 1
            b = c # b = 1
            print(b, end = " ")
             
             
print(fibonacci_seq(10))