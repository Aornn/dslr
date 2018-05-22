# -*- coding: utf-8 -*-
import csv
import sys
import numpy as np
from compute_grad import *
import ML_functions as mlf
import matplotlib.pyplot as plt
from visualise_datatest import *
from multiprocessing import Process
import seaborn as sns

def prepare_data(array):
    data = list(array)
    del data[0]
    for i, elem in enumerate(data):
        try:
            data[i] = float(elem)
        except:
            data[i] = data[i]
    return data

def concatenate_weights(array):
    data = list(array)
    weights = []
    for i , row in enumerate(data):
        tmp = []
        for elem in row:
            tmp.append(float(elem))
        weights.append(tmp)
    return weights

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("No argument given")
        exit()
    house_name = ['Ravenclaw','Slytherin','Hufflepuff','Gryffindor']
    data = list(csv.reader(open(sys.argv[1])))
    weights_file = list(csv.reader(open("weights.csv")))
    subject = [[],[],[],[],[],[],[],[],[],[],[]]

    for i , row in enumerate(data):
        for i in range(11):
            if (row[i+8] == ""):
                subject[i].append(0)
            else:
                subject[i].append(row[i+8])
    for i in range(11):
        subject[i] = prepare_data(subject[i])
        subject[i] = mlf.normalize_array(subject[i])

    X = np.transpose(subject)
    ones = np.ones((len(X),1))
    X = np.concatenate((ones, X), axis=1)
    weights = []
    f = open("houses.csv", "w")
    f.write("Index,Hogwarts House\n")
    weights = concatenate_weights(weights_file)

    for j, student in enumerate(X):
        res = []
        house_index = 0
        for i, theta in enumerate(weights):
            res.append(mlf.sigmoid(np.dot(student, theta)))
        max_weights = mlf.ml_max(res)
        for index_note, note in enumerate(res):
            if note == max_weights:
                house_index = index_note
        f.write(str(j)+","+str(house_name[house_index])+"\n")
    f.close()
    visualise_datatest(str(sys.argv[1]))