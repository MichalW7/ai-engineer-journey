#Zad 1
def positive_squares(nums):
    return sorted([x**2 for x in nums if x>0])
print(positive_squares([-1,9,2,-2,3]))
#
#Zad 2
def count_labels(labels):
    return {x:labels.count(x) for x in set(labels)}

print(count_labels(["cat","dog","cat"]))
#
#Zad 3
def top_k(d, k):
    new_d=sorted(d.items(),key=lambda item:item[1],reverse=True)
    return new_d[:k]
    """Zwraca listę (key, value) posortowaną malejąco po value, długości k."""
print(top_k({"a":5,"b":2,"c":9},2))
#