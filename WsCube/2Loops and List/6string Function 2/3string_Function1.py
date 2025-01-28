#endswith() - Returns true if the string ends with the specific value
a = "Harry Potter"
print(a.endswith("r"))
print(a.endswith("t",6,7))

#startswith() - Return true if the string starts with special value
b = "Harry potter"
print(b.startswith("h"))
print(b.startswith("p",6,9))

#strip() - Return a trimmed version of the sstring
c = "      Harry potter"
print(c.strip())
d = "  ******Harry potter............"
print(d.strip(" ,*,."))

#split() - Split the string at the spicified separator, and return a list
e = "#FDFD#DDG#OMG#GOODFOOD"
print(e.split("#"))
f = "hello. my name is Jon. i am 22 year old"
print(f.split("."))

#ljust - Returns a left justified version of the string
g = "Harry potter"
x = a.ljust(20)
y = a.ljust(20,"-")
print(x, "Is my favorite movie")
print(y, "Is my favorite movie")

#rjust - returns a right justified version of the string
h = "Harry potter"
x = h.rjust(20)
y = h.rjust(20,"~")
print(x, "Is my favorit movie")
print(y, "Is my favorit movie")

#replace - returns s string where a specified value is replaced with a 
#specific value
i = "my name is john"
print(i.replace("john","lisa"))

#rindex() - search the string for a specific value and return
# the last position of theree it was found
j = "Harry Potter and the Prisoner of Azkaban"
print(j.rindex("Prisoner"))

#rfind() - search the string for a specifid value and returns the last position of where it was found
k = "Harry Potter and the Prisoner of Azkaban"
print(k.rfind("Potter"))
l = "bibidy bobidy boo"
print(l.rfind("dy",6,14))