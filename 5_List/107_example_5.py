# common elements finder function
# define a function which takes 2 lists as input and returns a list
# which contains common elements of both lists

# example
# input ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

def common_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_finder([1,2,5,8], [1,2,7,6]))