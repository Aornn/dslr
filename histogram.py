# -*- coding: utf-8 -*-
import csv
import ML_functions as mlf
import matplotlib.pyplot as plt

data = list(csv.reader(open("dataset_train.csv")))
subject_all = []
subject_ravenclaw = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
subject_slytherin = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
subject_gryffindor = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
subject_hufflepuf = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
house_name = ['Gryffindor','Hufflepuf','Ravenclaw','Slytherin']
name = []

def prepare_data(array):
    for i, elem in enumerate(array):
        if not elem:
            array[i] = 0
        else:
            array[i] = float(elem)
    return array

i = 6
while i != 19:
    name.append(data[0][i])
    i = i + 1

for row in data:
    i = 6
    j = 0
    if (mlf.analyze_row(row)) :
        if row[1] == 'Ravenclaw':
            while i != 19:
                subject_ravenclaw[j].append(row[i])
                j = j + 1
                i = i + 1
        elif row[1] == 'Slytherin':
            while i != 19:
                subject_slytherin[j].append(row[i])
                j = j + 1
                i = i + 1
        elif row[1] == 'Gryffindor':
            while i != 19:
                subject_gryffindor[j].append(row[i])
                j = j + 1
                i = i + 1
        elif row[1] == 'Hufflepuff':
            while i != 19:
                subject_hufflepuf[j].append(row[i])
                j = j + 1
                i = i + 1

subject_all = [subject_gryffindor, subject_hufflepuf, subject_ravenclaw, subject_slytherin]

for elem in subject_all:
    for array in elem:
        array = prepare_data(array)
        array = mlf.normalize_array(array)

std = []
for index in range(13):
    avg_std = []
    for i, array in enumerate(subject_all):
        avg_std.append(mlf.std(array[index]))
    std.append(mlf.std(avg_std))

index = 0
for i, elem in enumerate(std):
    if elem == mlf.ml_min(std):
        index = i

plt.title(str(name[index]), loc='center')
plt.hist(subject_gryffindor[index],histtype='bar', alpha=0.3,ec='black',label="Gryffindor")
plt.hist(subject_hufflepuf[index],histtype='bar', alpha=0.3,ec='black',label="Hufflepuf")
plt.hist(subject_ravenclaw[index],histtype='bar', alpha=0.3,ec='black',label="Ravenclaw")
plt.hist(subject_slytherin[index],histtype='bar', alpha=0.3,ec='black',label="Slytherin")
mean_tot = mlf.mean(subject_gryffindor[index] + subject_hufflepuf[index] + subject_ravenclaw[index] + subject_ravenclaw[index])
print (mean_tot)
plt.axvline(mean_tot)
plt.legend(loc='upper left', prop={'size': 6})
plt.show()