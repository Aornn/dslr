# -*- coding: utf-8 -*-
import csv
from compute_grad import *
import ML_functions as mlf
import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Process

def prepare_data(array):
    data = list(array)
    del data[0]
    for i, elem in enumerate(data):
            data[i] = float(elem)
    return data

def writer(weights, value):
    house_name = ['Ravenclaw','Slytherin','Hufflepuff','Gryffindor']
    f = open('/tmp/'+house_name[value-1]+'.csv', 'w')
    for i in range(len(weights)):
        f.write(str(weights[i]))
        if (i != len(weights) - 1):
            f.write(',')
    f.close()

def get_weights(X, y, value):
    array = list(y)
    for i, elem in enumerate(array):
        if (elem != value):
            array[i] = 0
        else:
            array[i] = 1
    array = np.transpose(array)
    weights = training(X,array)

if __name__ == '__main__':
    data = list(csv.reader(open("dataset_train.csv")))
    subject = [[],[]]
    y = []
    for i , row in enumerate(data):
        if (mlf.analyze_row(row)):
            subject[0].append(row[8])
            subject[1].append(row[12])
            if (row[1] == 'Ravenclaw'):
                y.append(1.0)
            elif (row[1] == 'Slytherin'):
                y.append(2.0)
            elif (row[1] == 'Hufflepuff'):
                y.append(3.0)
            elif (row[1] == 'Gryffindor'):
                y.append(4.0)
            else:
                y.append(0.0)

    for i in range(2):
        subject[i] = prepare_data(subject[i])
        subject[i] = mlf.normalize_array(subject[i])

    del y[0]
    X = np.transpose(subject)
    ones = np.ones((len(X),1))
    X = np.concatenate((ones, X), axis=1)
    for i in range(1,5):
        p = Process(target=get_weights, args=(X,y,i,))
        p.start()
    p.join()
    house_name = ['Ravenclaw','Slytherin','Hufflepuff','Gryffindor']
    weights = []
    for elem in house_name:
        data = csv.reader(open('/tmp/'+elem+'.csv'))
        for row in data:
            weights.append(row)

    f = open('weights.csv', 'w')
    for array in weights:
        for i in range(len(array)):
            f.write(str(array[i]))
            if (i != len(array) - 1):
                f.write(',')
        f.write("\n")
    f.close()
