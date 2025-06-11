#generate list with range function
#something more about pop method

#pass list to a function

number = list(range(1,11))
print(number)
popped_item = number.pop()
print(popped_item)
print(number)
 
#index method
num = [1,2,3,4,5,6,7,8,9,1]
print(num.index(1)) # it will return the index at which 1 is store
print(num.index(1,3)) # 3 means the searching of 1 eill get start from the index 3
print(num.index(7,4,8))# here you haved define the range from index 4 to 8
print(num.count(1))


def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(num))
