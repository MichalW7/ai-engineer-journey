#Zad 1
def invert_dict(d):
    new_d=dict()
    for k,v in d.items():
        new_d[v]=k
    return new_d

print(invert_dict({"a": 1, "b": 2}))
#

#Zad 2
def count_labels(labels):
    d=dict()
    for i in labels:
        d[i]=d.get(i,0)+1
    return d

print(count_labels(["cat","dog","cat"]))
#

#Zad 3
def top_k(d, k):
    new_d=sorted(d.items(),key=lambda item: item[1],reverse=True)
    for i,t in enumerate(new_d):
        k1,v=t
        if i<k:
            print(k1,"->",v,end=" ")
    
top_k({"a": 5, "b": 2, "c": 9, "d":1},2)
        


