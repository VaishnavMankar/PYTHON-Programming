#Dictionary comprehension
#square = {1:1,2:4,3:9}
square = {nums:nums*2 for nums in range(1,11)}
print(square)

square2 = {f"Square of {nums} is":nums*2 for nums in range(1,11)}
#print(square2)
for k,v in square2.items():
    print(f"{k}:{v}")


name = "Vaishnav"
word_count = {char:name.count(char) for char in name}
print(word_count)