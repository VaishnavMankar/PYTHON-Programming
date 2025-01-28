#Recursion 
# def hello():
#     print("hello")
#     return hello()

# print(hello())

def fact(n):
    if n == 1:
        return 1
    else:
        return(n*fact(n-1))
    
print(fact(999))