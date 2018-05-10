# -*- coding: utf-8 -*-
import csv
import ML_functions as mlf
import matplotlib.pyplot as plt
import random
import seaborn as sns
import pandas as pd
from matplotlib.widgets import Slider
# def prepare_data(array, name):
#     name.append(array[0])
#     del array[0]
#     for i, elem in enumerate(array):
#         if not elem:
#             array[i] = 0
#         else:
#             array[i] = float(elem)
#     return array

# data = list(csv.reader(open("dataset_train_2.csv")))
# subject = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
# name = []
# for row in data:
#     subject[0].append(row[6])
#     subject[1].append(row[7])
#     subject[2].append(row[8])
#     subject[3].append(row[9])
#     subject[4].append(row[10])
#     subject[5].append(row[11])
#     subject[6].append(row[12])
#     subject[7].append(row[13])
#     subject[8].append(row[14])
#     subject[9].append(row[15])
#     subject[10].append(row[16])
#     subject[11].append(row[17])
#     subject[12].append(row[18])

# for i, array in enumerate(subject):
#     array = prepare_data(array, name)
#     array = mlf.normalize_array(array)
#     # array.insert(0,name[i])
# print (subject)

arr = pd.read_csv('tet.csv')
sns.set(style="ticks")
sns.pairplot(arr, hue="Arithmancy")

plt.show()