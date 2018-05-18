# -*- coding: utf-8 -*-
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Process
import numpy as np
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    mine = list(csv.reader(open("houses.csv")))
    good = list(csv.reader(open("dataset_train.csv")))
    good_val = []
    tmp = []

    for elem in mine:
        house_name = elem[0].split(',')
        tmp.append(elem[1])

    for row in good:
        if(row[8] != "" and row[12] != ""):
            good_val.append(row[1])
    del good_val[0]
    del tmp[0]
    print("Pourcentage de précision : ",accuracy_score(good_val, tmp))