# define a function that takes a list of words as an argument and
# returns a list with the reverse of every element in that list

# example
# ['abc', 'tuv', 'xyz'] ---> ['cba', 'vut', 'zyx']
def reverse_element(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

words = ['abc', 'tuv', 'xyz']
print(reverse_element(words))

