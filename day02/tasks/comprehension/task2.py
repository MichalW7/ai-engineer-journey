#Zad 1
nums = [-3, -2, -1, 0, 1, 2, 3, 4]
res=sorted([x**2 for x in nums if x>0])
print(res)
#
#Zad 2
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
d={x:words.count(x) for x in set(words)}
print(d)
#
#Zad 3
classes = ["cat", "dog", "bird"]
d={x:i for i,x in enumerate(classes)}
print(d)
#
