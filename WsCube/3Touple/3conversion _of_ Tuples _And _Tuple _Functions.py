a = ("OnePlus","Nokia","Redmi")
print(a.count("Redmi"))
print("The index of nokia is ",a.index("Nokia"))
print("Before conversion",type(a))

a = list(a)
print("after conversion",type(a))

a.append("Vivo")
print(a)

a = tuple(a)
print(type(a))
print(a)