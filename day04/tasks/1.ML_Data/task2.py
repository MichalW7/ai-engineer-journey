import numpy as np

X = np.array([
    [1.2, 3.4],
    [2.1, 0.9],
    [0.8, 1.5],
    [3.0, 2.2],
    [1.5, 2.7]
])

y = np.array([0, 1, 0, 1, 0])

sizeTrain=int(len(X)*0.8)
X_train=X[:sizeTrain]
X_test=X[sizeTrain:]
y_train=y[:sizeTrain]
y_test=y[sizeTrain:]

mu=np.mean(X_train,axis=0)
sigma=np.std(X_train,axis=0)
X_train_norm=(X_train-mu)/sigma
X_test_norm=(X_test-mu)/sigma
print(mu)
print(sigma)
print(X_train_norm)
print(X_test_norm)
