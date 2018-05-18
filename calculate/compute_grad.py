import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def update_weights(X, y, weights):
    m = len(X)

    z = np.dot(X, weights)
    predictions = sigmoid(z)

    gradient = np.dot(X.T,  predictions - y) / m
    gradient *= 0.1
    weights = weights - gradient

    return weights

def training(X,y):
    weights = np.transpose([0,0,0])
    for i in range(642435):
        weights = update_weights(X, y, weights)
    return weights