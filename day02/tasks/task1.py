#Zad 1
nums = [1, 2, 3, 4, 5, 6]
suma=[x*x for x in nums if x % 2 == 0]
print(suma)
#
#Zad 2
labels = ["cat", "dog", "cat", "bird", "dog"]
d={x:labels.count(x) for x in set(labels)}
print(d)
#
#Zad 3
names = ["a", "b", "c"]
values = [10, 20, 30]
d2=dict(zip(names,values))
print(d2)
