# define a function which will take list as a argument and this function 
# will return a reversed list

# examples
# [1,2,3,4] ---> [4,3,2,1]
# ['word1', 'word2'] ---> ['word2', 'word1']

# Note you simply do this with reverse method or [::-1]

# but try to do this with the help of append and return method


def reverse_list(lis):
    lis.reverse()
    return lis

def reverse_list2(l):
     l[::-1]
     return l
    
num = [1,2,3,4,5]
print("method 1",reverse_list(num))

print("method 2",reverse_list2(num))

number = [4,3,2,1]
def reverse_list3(le):
    r_list = []
    for i in range(len(le)):
        popped_item = le.pop()
        r_list.append(popped_item)
    return r_list

print("method 3: ", reverse_list3(number))