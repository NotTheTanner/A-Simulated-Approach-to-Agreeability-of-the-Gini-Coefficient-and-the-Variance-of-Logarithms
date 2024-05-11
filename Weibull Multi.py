# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:45:36 2024

@author: Jack
"""

import numpy as np

import copy

def create_sets_weibull(sets,entries,k):
    mainarray_exp = []
    for x in range(sets):
        mainarray_exp.append(np.random.weibull(k,size=entries))
        
    return mainarray_exp

#----------------------------------------------------------------------

#Calculating relevant variables from an array of distributions

def log_var(distributions):

    
    log_varx = np.var(np.log(distributions))

        
    return(log_varx)    
        
def gini_discrete_multi(distributions):
    
    ginix = 0
    for y in range(len(distributions)):
        for z in range(len(distributions)):
            giniz = abs(distributions[y]-distributions[z])
            ginix += giniz
                
    ginix = ginix/(2*len(distributions)**2*np.mean(distributions))
    
        
        
    return(ginix)

#-----------------------------------------------------------------------

def generate_multi(distributions):
    ginis = []
    log_vars = []   
    for x in range(len(distributions)):
        g = []
        ginix = gini_discrete_multi(distributions[x])
        g.append(ginix)
        g.append(x)
        ginis.append(g)
        
        l = []
        log_varx = log_var(distributions[x])
        l.append(log_varx)
        l.append(x)
        log_vars.append(l)
        
    return ginis, log_vars

def bubble_sort_a(gini, log_var):
    for x in range(len(gini)-1):
        counter = 0
        for y in range(len(gini)-1):
            if gini[y][0] < gini[y+1][0]:
                save = gini[y]
                gini[y] = gini[y+1]
                gini[y+1] = save
                counter += 1
            if log_var[y][0] < log_var[y+1][0]:
                save = log_var[y]
                log_var[y] = log_var[y+1]
                log_var[y+1] = save
                counter += 1
        if counter == 0:
            break
            print("I must break you")
           
    return gini, log_var    


def gap_sort(distribution):
    dist = copy.deepcopy(distribution)
    for x in range(len(dist)-1):
        counter = 0
        for y in range(len(dist)-1):
            if dist[y][2] < dist[y+1][2]:
                save = dist[y]
                dist[y] = dist[y+1]
                dist[y+1] = save
                counter += 1
                
        if counter == 0:
            break
            print("I must break you")
            
    return dist

def calculate_gaps(gini, log_var):
    
    gini_local = copy.deepcopy(gini)
    log_var_local = copy.deepcopy(log_var)
    
    for x in range(len(gini_local)):
        dist_number = gini_local[x][1]
        for y in range(len(log_var_local)):
            if dist_number == log_var_local[y][1]:
                gap = y-x
                gini_local[x].append(gap)
                log_var_local[y].append(-gap)
                break
            else:
                pass
        
    return gini_local, log_var_local


def avg_gap_percentile(p, gini, log_var):
    bucket_size = int(len(gini)*p)
    bucket_quant = int(1/p)
    gini_gaps = []
    log_gaps = []
    section = 0
    for x in range(bucket_quant):
        gini_sum = 0
        log_sum = 0
        for y in range(bucket_size):
            gini_sum += gini[y+section][2]
            log_sum += log_var[y+section][2]
        gini_sum = gini_sum/bucket_size
        log_sum = log_sum/bucket_size
        gini_gaps.append(gini_sum)
        log_gaps.append(log_sum)
        section += bucket_size
        
    return gini_gaps, log_gaps

def main_multi():
    dists = create_sets_weibull(1000, 50, 5)
    gini, log_var = generate_multi(dists)
    sorted_gini, sorted_var = bubble_sort_a(gini, log_var)
    gapped_gini, gapped_var = calculate_gaps(sorted_gini, sorted_var)
    
    return gapped_gini, gapped_var

