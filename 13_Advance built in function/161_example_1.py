# THIS IS CHALLENGE

# define a function take any no of lists containing number
# [1,2,3], [4,5,6], [7,8,9]
# return average
# (1+4+7)/3, (2,5,8)/3, (3,6,9)/3

# try to make this anonymous function in one line using lambda 😃😃

def average_finder(l1,l2):
    average = []
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average
    
print(average_finder([1,2,3],[4,5,6]))

def average_finder2(*args):
    average2 = []
    for pair in zip(*args):
        average2.append(sum(pair)/len(pair))
    return average2
    
print(average_finder2([1,2,3],[4,5,6],[7,8,9]))

average_finder3 = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder3([1,2,3],[4,5,6],[7,8,9]))

trying = (list(zip([1,2,3],[4,5,6],[7,8,9])))
print(trying)