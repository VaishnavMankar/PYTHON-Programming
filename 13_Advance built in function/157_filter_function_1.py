# filter function
def is_even(a):
    return a%2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

#the filter function will sent one by one values to is_even function the and
#will soore the vaues which is_even function returns in even variable
even = tuple(filter(is_even,numbers))
print(even)
# you can fo this without declearing other function to return the values
# you can use lambda function 

even2 = tuple(filter(lambda a: a%2 == 0, numbers))
print(even2)

#you cannot iterate on map and filter function more than once 

new_list = [ i for i in numbers if i%2 == 0]
print(new_list)