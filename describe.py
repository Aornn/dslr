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

def get_stats(array, name):
    print (name)
    print ("Count : " + str(len(array)))
    print ("Moyenne : " + str(mlf.mean(array)))
    print ("Ecart-type : " + str(mlf.std(array)))
    print ("Min : " + str(min(array)))
    print ("Max : " + str(max(array)))
    q1, q2 = mlf.quartile(array)
    print ("15% : " + str(q1))
    print ("Mediane : " + str(mlf.mediane(array)))
    print ("75% : " + str(q2))
    print ("")
#Arithmancy,Astronomy,Herbology,Defense,Divination,Muggle,Ancients,History,Transfiguration,Potions,Care,Charms,Flying = [],[],[],[],[],[],[],[],[],[],[],[],[]
data = list(csv.reader(open("dataset_train.csv")))
subject = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
name = []
for row in data:
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

for elem in subject:
    elem = prepare_data(elem, name)
for i, elem in enumerate(subject):
    get_stats(elem, name[i])