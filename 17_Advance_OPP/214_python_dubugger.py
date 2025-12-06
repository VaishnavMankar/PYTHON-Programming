import pdb

# module - python file contains usefull classes and functions wrote
# by developer.

# According to wikipedia - Debugging is the process of finding and resolving
# defects or problems within a computer program that prevent correct operation
# of computer software or a system.

# why debugging
# 1.) our program is not running and causing unexpected errors.
# 2.) our program is working fine but not working the same way we want.

# step for debugging 
# 1.) set trace
# 2.) execution code line by line

pdb.set_trace()
name = input('Please type your numbr : ')
age = input('Please type your age: ')
print(f"Hello {name} your age is {age}")
age2 = int(age) + 5
print(f'{name} your will be {age2} in next five year')

