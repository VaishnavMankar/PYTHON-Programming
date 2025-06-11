numbers = [1,2,3,4,5]
print(numbers)
print(numbers[1])
words = ["Wordq","word2","word3",]
print(words)
print(words[:2])

mixed = [1,2,3,4,"five","six",2.3,None]
print(mixed)
print(mixed[:-1])
print(mixed[-1])
print(mixed[::-1])

mixed[1] = "Two"
print(mixed)

mixed[2:] = "Three","Four"
print(mixed)
