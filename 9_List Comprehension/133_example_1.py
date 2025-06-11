
# define a function that takes a list of strings
# and returns a list containing the reverse of every string

# NOTE - USE LIST COMPREHENSION because we already did this exercise
# using the normal method

# example
# l = ['abc', 'tuv', 'xyz']
# reverse_string(l) ----> ['cba', 'vut', 'zyx']

#using list comprehension
def reverse_strings(l):
    return [name[::-1] for name in l]

name = ['Harshit','Vaishnav','Darshan']
print(reverse_strings(name))

print(reverse_strings(['abc','def','ijk']))

#using treditional method
def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list
    
print(reverse_str(name))
