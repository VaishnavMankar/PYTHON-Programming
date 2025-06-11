#find the number of list insode the list
#[[1,2,3],[4,5,6],[8,9,0]] -> input
# 3 list -> output

def sublist_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

maximum = [1,2,3,[4,5]]
print(sublist_count(maximum))