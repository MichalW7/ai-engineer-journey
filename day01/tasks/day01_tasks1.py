
#Zad A
nums = [5, 1, 9, 2, 7, 3, 8]
print(nums[:3])
#
#Zad B
cfg = {"lr": 0.01, "epochs": 10}
cfg["batch_size"]=32
cfg["epochs"]+=5
for k in cfg:
    print(k,"->",cfg[k],)
#
#Zad C
bbox = (10, 20, 110, 220)
x1,x2,y1,y2=bbox
pole=abs((x1-x2)*(y1-y2))
print(pole)
#Zad D
labels = ["cat", "dog", "cat", "bird", "dog"]
s=set(labels)

for i in s:
    print(i,end=" ")
print();

if("fish" in s):
    print("Jest")
else:
    print("Nie ma ")
#Zad E
classes = ["cat", "dog", "bird"]
m=dict()
for i,val in enumerate(classes):
    m[val]=i
print(m)
