a = "hello"
b = "HELLO"
c = "123456"
d = " "
f = "Hello 123@"
g = "1.234"
h = "Harry Potter And The Goblet Of Fire"

#isalnum - Returns True if all characters in the string are alphanumeric 
print("checking if it is a #isalnum")
print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(f,f.isalnum())
print(g,g.isalnum())


#isalpha - Returns True if all characters in the string are in the alphabet 
print("checking if it is #isalpha")
print(a,a.isalpha())
print(b,b.isalpha())


#isdecimal - Returns True if all characters in the string are decimals
print("checking if it is #isdecimal or not")
print(g,g.isdecimal())
print(c,c.isdecimal())
 
#isdigit - Returns True if all characters in the string are digits 
print("checking if it s #isdigit or not")
print(g,g.isdigit())
print(c,c.isdigit())
print(b,b.isdigit())

#isnumeric - Returns True if all characters in the string are numeric 
print("checking if it is #isnumeric or not")
print(b,b.isnumeric())
print(c,c.isnumeric())
print(g,g.isnumeric())

#islower - Check if the string is lower case or  not
print("checking if it is #islower or not")
print(a,a.islower())
print(c,c.islower())

#isupper - Returns True if all characters in the string are upper case 
print("checking if it is #isupper or not") #not just one but all the characters should be capital
print(a,a.isupper())
print(b,b.isupper())
print(f,f.isupper())

#isspace - Returns True if all characters in the string are whitespaces
print("checking if it is #isspace or not")
print(d,d.isspace())
print(f,f.isspace())

#istitle - Returns True if the string follows the rules of a title
print(b,b.istitle()) 
print(f,f.istitle()) 
print(h,h.istitle())



