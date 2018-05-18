# -*- coding: utf-8 -*-
import csv
from compute_grad import *
import ML_functions as mlf
import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Process
import seaborn as sns
import pandas as pd

def visualise_datatest(name_dataset):
    houses = list(csv.reader(open("houses.csv")))
    data = list(csv.reader(open(name_dataset)))
    subject = []
    note_tmp=[]
    houses_name = ["Herbology","Ancient Runes","Houses"]
    for i, row in enumerate(data):
        if(row[8] != "" and row[12] != ""):
            note_tmp.append([row[8],row[12]])
    del note_tmp[0]
    del houses[0]
    for i, elem in enumerate(note_tmp):
        subject.append([float(elem[0]),float(elem[1]),houses[i][1]])
    df = pd.DataFrame(subject, columns=houses_name)
    sns_plot = sns.pairplot(df,hue="Houses")
    sns_plot.savefig("resultat_test.png")