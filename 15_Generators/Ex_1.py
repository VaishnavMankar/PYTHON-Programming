#fibonacci using generator
def fibonic_num(n):
    a = 0
    b = 1
    if n == 1:
        yield a
    elif n == 2:
        yield a,b 
    else:
        #yield(a,b,end=" ")
        for i in range(n-2):
          c = a + b
          a = b
          b = c
          yield b
        
for i in fibonic_num(20):
    print(i, end = " ")