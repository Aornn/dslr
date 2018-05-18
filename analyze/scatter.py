# -*- coding: utf-8 -*-
import csv
import ML_functions as mlf
import matplotlib.pyplot as plt

def prepare_data(array, name):
    name.append(array[0])
    del array[0]
    for i, elem in enumerate(array):
        if not elem:
            array[i] = 0
        else:
            array[i] = float(elem)
    return array


data = list(csv.reader(open("dataset_train.csv")))
subject = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
name = []
for row in data:
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

for array in subject:
    array = prepare_data(array, name)
    array = mlf.normalize_array(array)

res = []
for i in range(mlf.ml_len(subject)):
    for j in range(i+1, mlf.ml_len(subject)):
        r1 = mlf.std(subject[i])
        r2 = mlf.std(subject[j])
        res.append((i, j,abs(r1-r2)))

min_res = []
for elem in res:
    min_res.append(elem[2])
min_res = mlf.ml_min(min_res)

for elem in res:
    if elem[2] == min_res:
        i = elem[0]
        j = elem[1]
        break

print("The best values are for",name[i],"and" ,name[j])
plt.title("Scatter plot")
plt.scatter(subject[i], subject[j], color=['red', 'blue'])
plt.xlabel(name[i])
plt.ylabel(name[j])
plt.show()