# readfile
# open function 
# read methods
# seek method
# tell method
# readline method
# readlines method
# close method

f = open('file.txt')
# print(f'coursor position - {f.tell()}')

# print(f.read())
# print(f'coursor position - {f.tell()}')
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f'coursor position - {f.tell()}')
# print(f.read())

# print(f.readline(), end="")
# print(f.readline())
# print(f.readline())

# lines = f.readlines()
# #print(lines)
# for i in lines:
#     print(i,end="")

print(f.name)
print(f.closed)

# for j in f:         #you can also iterate ove the file directly
#     print(j,end='')

for j in f.readlines()[:1]:         #you can also iterate ove the file directly
    print(j,end='')

f.close()