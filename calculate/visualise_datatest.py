# -*- coding: utf-8 -*-
import csv
import ML_functions as mlf
import matplotlib.pyplot as plt


def visualise_datatest(name_dataset):
    houses = list(csv.reader(open("houses.csv")))
    repartition = []
    for elem in houses:
        repartition.append(elem[1])
    del repartition[0]
    plt.title("Répartition des élèves")
    plt.hist(repartition)
    plt.xlabel("House")
    plt.ylabel("Frequency")
    plt.savefig("resultat_test.png")