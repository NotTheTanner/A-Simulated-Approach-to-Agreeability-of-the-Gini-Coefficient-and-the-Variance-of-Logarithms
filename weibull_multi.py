# -*- coding: utf-8 -*-


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

def generate_gapped(sets, entries, k):
    dists = create_sets_weibull(sets, entries, k)
    gini, log_var = generate_multi(dists)
    sorted_gini, sorted_var = bubble_sort_a(gini, log_var)
    gapped_gini, gapped_var = calculate_gaps(sorted_gini, sorted_var)
    
    return gapped_gini, gapped_var


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

def avg_gap_percentile_abs(p, gini, log_var):
    bucket_size = int(len(gini)*p)
    bucket_quant = int(1/p)
    gini_gaps = []
    log_gaps = []
    section = 0
    for x in range(bucket_quant):
        gini_sum = 0
        log_sum = 0
        for y in range(bucket_size):
            gini_sum += abs(gini[y+section][2])
            log_sum += abs(log_var[y+section][2])
        gini_sum = gini_sum/bucket_size
        log_sum = log_sum/bucket_size
        gini_gaps.append(gini_sum)
        log_gaps.append(log_sum)
        section += bucket_size
        
    return gini_gaps, log_gaps

def expected_gap_random(sets):
    gap_average = []
    for x in range(sets):
        gap_x = 0
        for y in range(sets):
            gap_x += y-x
        
        gap_x = gap_x/sets
        gap_average.append(gap_x)
        
    return gap_average

def expected_gap_percentile(p, sets):
    gaps_exp = expected_gap_random(sets)
    exp_gaps = []
    section = 0
    bucket_quant = int(1/p)
    for x in range(bucket_quant):
        x_sum = 0
        for y in range((int(sets*p))):
            x_sum += gaps_exp[y+section]
        x_sum = x_sum/(sets*p)
        exp_gaps.append(x_sum)
        section += int(sets*p)
        
    return exp_gaps

def gap_percentile_iterate(p, sets, iterations, k):
    gaps = []
    var_gaps_gini = []
    var_gaps_gini_grouped = []
    var_gaps_var = []
    var_gaps_var_grouped = []
    tot_gaps_gini = []
    tot_gaps_var = []
    bucket_quant_2 = int(1/p)
    for x in range(bucket_quant_2):
        tot_gaps_gini.append(0)
        tot_gaps_var.append(0)
        
    for x in range(iterations):
        gaps_x = []
        g_gini, g_var = generate_gapped(sets, 50 , k)
        gini_gaps_x, var_gaps_x = avg_gap_percentile_abs(p, g_gini, g_var)
        gaps_x.append(gini_gaps_x)
        gaps_x.append(var_gaps_x)
        gaps.append(gaps_x)
        for y in range(bucket_quant_2):
            tot_gaps_gini[y] += gini_gaps_x[y]
            tot_gaps_var[y] += var_gaps_x[y]
            
        everything_should_be_deepcopy = copy.deepcopy(gini_gaps_x)
        var_gaps_gini.append(everything_should_be_deepcopy)
        
        everything_should_be_deepcopy_2 = copy.deepcopy(var_gaps_x)
        var_gaps_var.append(everything_should_be_deepcopy_2)
        print(x)
        
    for x in range(bucket_quant_2):
        reorder = []
        reorder_2 = []
        for y in range(iterations):
            reorder.append(var_gaps_gini[y][x])
            reorder_2.append(var_gaps_var[y][x])
        var_gaps_gini_grouped.append(reorder)  
        var_gaps_var_grouped.append(reorder_2)  
        
    for x in range(bucket_quant_2): 
        tot_gaps_gini[x] = tot_gaps_gini[x]/iterations
        tot_gaps_var[x] = tot_gaps_var[x]/iterations
        var_gaps_gini_grouped[x] = np.var(var_gaps_gini_grouped[x])
        var_gaps_var_grouped[x] = np.var(var_gaps_var_grouped[x])
        
    return tot_gaps_gini, tot_gaps_var, #var_gaps_gini_grouped, var_gaps_var_grouped

def gap_absolute_iterate(sets, iterations, k):
    tot_gaps_gini = []
    tot_gaps_var = []
    for x in range(sets):
        tot_gaps_gini.append(0)
        tot_gaps_var.append(0)
    for x in range(iterations):
        g_gini, g_var = generate_gapped(sets, 50 , k)
        for y in range(sets):
            tot_gaps_gini[y] += abs(g_gini[y][2])
            tot_gaps_var[y] += abs(g_var[y][2])
    
    for y in range(sets):
        tot_gaps_gini[y] = tot_gaps_gini[y]/iterations
        tot_gaps_var[y] = tot_gaps_var[y]/iterations
    
    return tot_gaps_gini, tot_gaps_var

def summary_stats():
    blank = []
    ginis = []
    variances = []
    for x in range(100):
        everything_should_be_deepcopy = copy.deepcopy(blank)
        everything_should_be_deepcopy_2 = copy.deepcopy(blank)
        ginis.append(everything_should_be_deepcopy)
        variances.append(everything_should_be_deepcopy_2)
    for x in range(100000): 
        g,v = generate_gapped(100, 50, 3)
        for y in range(100):
            ginis[y].append(g[y][2])
            variances[y].append(v[y][2])
        print(x)    
            
            
    return ginis, variances