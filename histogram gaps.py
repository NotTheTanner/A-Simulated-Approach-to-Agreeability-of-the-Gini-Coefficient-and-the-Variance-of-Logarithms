# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

from weibull_multi import generate_gapped

def store_gaps(iterations):
    var10 = []
    gin10 = []
    for x in range(iterations):
        gin, var = generate_gapped(1000, 50, 5)
        for x in range(20):
            var10.append(var[x][2])
            gin10.append(gin[x][2])
    
    return var10, gin10

def plot_gini(a):
    plt.rcParams['figure.dpi'] = 300
    
    
    plt.hist(a, color="blue", edgecolor = "black")
    
    plt.title("Gap for top 20 distributions (Gini)")
    plt.xlabel("Gap")
    plt.ylabel("Quantity")
    
    
def plot_var(a):
    plt.rcParams['figure.dpi'] = 300
    
    
    plt.hist(a, color="red", edgecolor = "black")
    
    plt.title("Gap for top 20 distributions (Variance of Logs)")
    plt.xlabel("Gap")
    plt.ylabel("Quantity")
    
def plot_dual(a,b):
    plt.rcParams['figure.dpi'] = 300
    
    
    plt.hist([a,b], color=["red", "blue"], label=["Variance of Logs", "Gini"], edgecolor = "black", bins = 15, log=False)
    
    plt.title("Gap for top 20 distributions")
    plt.xlabel("Gap")
    plt.ylabel("Quantity")
    plt.legend(loc=1, fontsize='5')