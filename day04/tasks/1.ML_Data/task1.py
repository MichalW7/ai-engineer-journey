import numpy as np

X = np.array([
    [1.2, 3.4],
    [2.1, 0.9],
    [0.8, 1.5],
    [3.0, 2.2],
    [1.5, 2.7]
])

y = np.array([0, 1, 0, 1, 0])
print(X.shape)
print(y.shape)

sizeTrain=int(len(X)*0.8)
X_train=X[:sizeTrain]
X_test=X[sizeTrain:]
y_train=y[:sizeTrain]
y_test=y[sizeTrain:]
print(X_train)
print(X_test)
print(y_train)
print(y_test)