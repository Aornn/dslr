import numpy as np
import ML_functions as mlf
import matplotlib.pyplot as plt

def cost_func(features, labels, weights):
    pred = mlf.sigmoid(np.dot(features, weights))
    pt1 = labels * np.log(pred)
    pt2 = (1 - labels) * np.log( 1 - pred)
    cost = pt1 + pt2
    return np.sum(cost) / len(labels)

    # observations = len(labels)
    # predictions = mlf.sigmoid(np.dot(features, weights))
    # class1_cost = -labels*np.log(predictions)
    # class2_cost = (1-labels)*np.log(1-predictions)
    # cost = class1_cost - class2_cost
    # return np.sum(cost)/observations

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
    prev_cost = 1
    for i in range(len(X[0])):
        tmp.append(0)
    weights = np.transpose(tmp)
    for i in range(600000):
        weights = update_weights(X, y, weights)
        cost = cost_func(X,y,weights)
        if(abs(prev_cost - cost) < 0.0001):
                break
        else:
            prev_cost = cost
    return weights