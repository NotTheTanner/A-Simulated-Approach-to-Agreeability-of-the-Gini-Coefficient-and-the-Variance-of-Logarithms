# -*- coding: utf-8 -*-
"""
@author: Jack
"""

import matplotlib.pyplot as plt

from pairwise import simulate_pairwise_weibull

entries_values = list(range(10,100,10))

ks=[.5,1,3,5,10]

colors = ['red', 'orange', 'yellow', 'green', 'blue']

def weibull_on_entries(k):
    agreement_rates_weib = []
    for x in entries_values:
        rate_exp = simulate_pairwise_weibull(2, x, 100000, k)
        print(x)
        agreement_rates_weib.append(rate_exp)
        
    return agreement_rates_weib

def graph_weib():
    
    plt.rcParams['figure.dpi'] = 300
    
    ax = plt.gca()
    ax.set_ylim([.5,1])
    ax.set_xlim([0,100])
    
    plt.minorticks_on()
    
    plt.xticks(ticks = list(range(0,101,5)))
    plt.tick_params(axis='both', labelsize = 8)
    
    plt.grid()
    
    for x in range(len(ks)):
        print(x)
        w = weibull_on_entries(ks[x])
        plt.scatter(entries_values, w, s=20, c=colors[x], label="Weibull with k="+str(ks[x]))    
    
    
    plt.title("Agreement Rate by Distribution")
    plt.xlabel("Number of Entries")
    plt.ylabel("Agreement Rate")
    
    plt.legend(loc=4, fontsize='5')
    
    
    
    plt.show
    
    return