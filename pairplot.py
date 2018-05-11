# -*- coding: utf-8 -*-
import csv
import ML_functions as mlf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
def prepare_data(array, name):
    name.append(array[0])
    del array[0]
    for i, elem in enumerate(array):
            array[i] = float(elem)
    return array

data = list(csv.reader(open("dataset_train.csv")))
subject = [[],[],[],[],[],[],[],[],[],[],[],[],[], []]
name = []
final_dict = {}
for i , row in enumerate(data):
    if (mlf.analyze_row(row)):
        subject[0].append(row[6])
        subject[1].append(row[7])
        subject[2].append(row[8])
        subject[3].append(row[9])
        subject[4].append(row[10])
        subject[5].append(row[11])
        subject[6].append(row[12])
        subject[7].append(row[13])
        subject[8].append(row[14])
        subject[9].append(row[15])
        subject[10].append(row[16])
        subject[11].append(row[17])
        subject[12].append(row[18])
        subject[13].append(row[1])

for i in range(13):
    subject[i] = prepare_data(subject[i], name)
    subject[i] = mlf.normalize_array(subject[i])
del subject[13][0]
name.append("House")

output = []
for i in range(len(subject[13])):
    tmp = []
    for j, _ in enumerate(subject):
        tmp.append(subject[j][i])
    output.append(tmp)

df = pd.DataFrame(output, columns=name)
sns_plot = sns.pairplot(df,hue="House")
sns_plot.savefig("output.png")
