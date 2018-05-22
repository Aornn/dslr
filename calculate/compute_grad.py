import numpy as np
import ML_functions as mlf


def update_weights(X, y, weights):
    m = len(X)

    z = np.dot(X, weights)
    predictions = mlf.sigmoid(z)

    gradient = np.dot(X.T,  predictions - y) / m
    gradient *= 0.1
    weights = weights - gradient

    return weights

def training(X,y):
    tmp = []
    for i in range(len(X[0])):
        tmp.append(0)
    weights = np.transpose(tmp)
    for i in range(642435):
        weights = update_weights(X, y, weights)
    return weights