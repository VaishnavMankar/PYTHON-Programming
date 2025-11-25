#define generator function
#take one number as argument
#generate a sequence of even numbers from 1 to that number
# 5 -> 2,4
# 7 -> 2,4,6

def even_generator(n):
    for num in range(1,n+1):
        if num % 2 == 0:
            yield(num)

# def even_generator(n):
#     for num in range(2,n+1,2):
#         yield(num)

# for num in even_generator(20):
#     print(num)                  # you can run this multiple times

even_nums = even_generator(20)
for num in even_nums:
    print(num)

# for num in even_nums:      #as soon as you assign a generator to a variable   
#     print(num)             #you cannot run it multiple timesk