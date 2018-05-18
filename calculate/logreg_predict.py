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

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def prepare_data(array):
    data = list(array)
    del data[0]
    for i, elem in enumerate(data):
        try:
            data[i] = float(elem)
        except:
            data[i] = 0.0
    return data

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("No argument given")
        exit()
    house_name = ['Ravenclaw','Slytherin','Hufflepuff','Gryffindor']
    data = list(csv.reader(open(sys.argv[1])))
    subject = [[],[]]
    for i , row in enumerate(data):
        if(row[8] != "" and row[12] != ""):
            subject[0].append(row[8])
            subject[1].append(row[12])

    for i in range(2):
        subject[i] = prepare_data(subject[i])
        subject[i] = mlf.normalize_array(subject[i])

    X = np.transpose(subject)
    ones = np.ones((len(X),1))
    X = np.concatenate((ones, X), axis=1)
    data = list(csv.reader(open("weights.csv")))
    weights = []
    f = open("houses.csv", "w")
    f.write("Index,Hogwarts House\n")

    for i , row in enumerate(data):
        tmp = []
        for elem in row:
            tmp.append(float(elem))
        weights.append(tmp)
    
    for j, student in enumerate(X):
        house = {}
        for i, theta in enumerate(weights):
            z = np.dot(student, theta)
            house.update({sigmoid(z):i})
        res = []
        for key in house.keys():
            res.append(key)
        max_res = mlf.ml_max(res)
        house_definitive = house[max_res]
        f.write(str(j)+","+str(house_name[house_definitive])+"\n")
    f.close()
    visualise_datatest(sys.argv[1])