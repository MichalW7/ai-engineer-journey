import numpy as np

x = np.array([10, 20, 30, 40, 50])
#Zad 1
print(np.mean(x))
print(np.std(x))
print(np.min(x))
print(np.max(x))
#
#Zad 2
min=np.min(x)
max=np.max(x)
xMinMaxNorm=(x-min)/(max-min)
print(xMinMaxNorm)
#
#Zad 3
ave=np.mean(x)
std=np.std(x)
xZscore=(x-ave)/std
print(xZscore)
#
#Zad 4
def normalize_pipeline(x):
    min=np.min(x)
    max=np.max(x)
    xMinMaxNorm=(x-min)/(max-min)
    ave=np.mean(x)
    std=np.std(x)
    xZscore=(x-ave)/std
    return xMinMaxNorm,xZscore

print(normalize_pipeline(x))
#


