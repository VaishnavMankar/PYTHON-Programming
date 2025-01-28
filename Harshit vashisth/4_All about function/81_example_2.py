# Define is_palindrome function that takes one word in string as input
# and returns True if it is palindrome else returns False

# palindrome - word that reads same backwards as forwards

# example
# is_palindrome("madam") ------> True
# is_palindrome("naman") ------> True
# is_palindrome("horse") ------> False

# logic (algorithm)
# step 1 -> reverse the string
# step 2 -> compare reversed string with original string
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
#return word == word[::-1]
    
print(is_palindrome("naman"))
print(is_palindrome("horse"))
        