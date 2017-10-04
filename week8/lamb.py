def isEven(x):
    return x % 2 == 0

l = range(1, 11)
# print filter(isEven, l)
print filter(lambda x: x % 2 == 0, l)
# sum()
# reverse()
# sort()
# max([1,2,3])
# min([1,2,3])
