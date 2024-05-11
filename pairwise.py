# -*- coding: utf-8 -*-
"""
Jack Dickinson Thesis 2024
"""
import numpy as np

#Global values to use if no imputs are specified:

g_sets = 2
g_entries = 100
g_iterations = 1000
g_distribution_type = "e"


#-----------------------------------------------------------------------

#Two main functions that print an agreement rate. Only differ on if 
#they ask for user input in the function call or the console

def main():

    sets, entries, iterations, dist = ask_for_inputs()
    if dist == "n" and sets == 2:
        agreement_normal = simulate_pairwise_normal(sets, entries, iterations, 10)
        print(agreement_normal)
    elif dist == "u" and sets == 2:
        agreement_uniform = simulate_pairwise_uniform(sets, entries, iterations)
        print(agreement_uniform)
    elif dist == "e" and sets == 2:
        agreement_exponential = simulate_pairwise_exponential(sets, entries, iterations)
        print(agreement_exponential)

def main_no_ask(sets, entries, iterations, dist):
    if dist == "n" and sets == 2:
        agreement_normal = simulate_pairwise_normal(sets, entries, iterations)
        print(agreement_normal)
    elif dist == "u" and sets == 2:
        agreement_uniform = simulate_pairwise_uniform(sets, entries, iterations)
        print(agreement_uniform)
    elif dist == "e" and sets == 2:
        agreement_exponential = simulate_pairwise_exponential(sets, entries, iterations)
        print(agreement_exponential)
    
#----------------------------------------------------------------------

#Optional function to allow user modifications to inputs:
    
def ask_for_inputs():
    resolved = 0
    while resolved == 0:
        print("Would you like to modify the parameters of the simulation? Type Yes or No")
        response1 = input()
    
        if response1 == "yes" or response1 == "Yes":
            print("How many entries would you like each distribution to contain? (Current value = " + str(g_entries)+")")
            entries_local = int(input())
            print("How many iterations would you like to run? (Current value = " + str(g_iterations)+")")
            iterations_local = int(input())
            print("What distribution type would you like to use? n = normal, u = uniform, e = exponential")
            distribution_type_local = input()
            
            resolved = 1
        
            return(g_sets, entries_local, iterations_local, distribution_type_local)
    
        elif response1 == "No" or response1 == "no":
            
            resolved = 1
        
            return(g_sets, g_entries, g_iterations, g_distribution_type)
        else:
            print("Please enter either yes or no")

#---------------------------------------------------------------------   

#Creating sets based on certain distributions 

def create_sets_uniform(sets,entries):
    mainarray_unif = []
    for x in range(sets):
        mainarray_unif.append(np.random.uniform(size=entries))
    
    return mainarray_unif

def create_sets_normal(sets,entries,center):
    mainarray_norm = []
    for x in range(sets):
        mainarray_norm.append(np.random.normal(loc=center, scale = 1, size=entries))
    
    return mainarray_norm

def create_sets_exponential(sets,entries):
    mainarray_exp = []
    for x in range(sets):
        mainarray_exp.append(np.random.exponential(scale=1, size=entries))
        
    return mainarray_exp

def create_sets_weibull(sets,entries,k):
    mainarray_exp = []
    for x in range(sets):
        mainarray_exp.append(np.random.weibull(k,size=entries))
        
    return mainarray_exp
    

#----------------------------------------------------------------------

#Calculating relevant variables from an array of distributions

def log_var(distributions):
    log_vars = []
    for x in range(len(distributions)):
        log_varx = np.var(np.log(distributions[x]))
        log_vars.append(log_varx)
        
    return(log_vars)    
        
def gini_discrete(distributions):
    gini = []
    for x in range(len(distributions)):
        ginix = 0
        for y in range(len(distributions[x])):
            for z in range(len(distributions[x])):
                giniz = abs(distributions[x][y]-distributions[x][z])
                ginix += giniz
                
        ginix = ginix/(2*len(distributions[x])**2*np.mean(distributions[x]))
        gini.append(ginix)
        
        
    return(gini)

#-----------------------------------------------------------------------
 
#Functions for comparing two distributions  
     
def compairwise(something):
    logs = log_var(something)
    ginis = gini_discrete(something)
    winner = []
    
    if logs[0] > logs[1]:
        winner.append(0)
    elif logs[0] < logs[1]:
        winner.append(1)
    elif logs[0] == logs[1]:
        print("How did we get here?") #Should be near impossible for this to happen but including it as a failsafe
        
    if ginis[0] > ginis[1]:
        winner.append(0)
    elif ginis[0] < ginis[1]:
        winner.append(1)
    elif ginis[0] == ginis[1]:
        print("How did we get here? (Gini's version)")

    return winner

#----------------------------------------------------------------------------

#Functions for calculating agreement rate for different distribution types

def simulate_pairwise_uniform(u_sets,u_entries,u_iterations):
    agreement = 0
    for x in range(u_iterations):
        sets = create_sets_uniform(2, u_entries)
        results = compairwise(sets)
        if results[0] == results[1]:
            agreement += 1
        
    agreement_rate = agreement/u_iterations
    
    return agreement_rate

def simulate_pairwise_normal(n_sets,n_entries,n_iterations,center):
    agreement = 0
    for x in range(n_iterations):
        sets = create_sets_normal(2, n_entries, center)
        results = compairwise(sets)
        if results[0] == results[1]:
            agreement += 1
        
    agreement_rate = agreement/n_iterations
    
    return agreement_rate

def simulate_pairwise_exponential(e_sets,e_entries,e_iterations):
    agreement = 0
    for x in range(e_iterations):
        sets = create_sets_exponential(2, e_entries)
        results = compairwise(sets)
        if results[0] == results[1]:
            agreement += 1
        
    agreement_rate = agreement/e_iterations
    
    return agreement_rate

def simulate_pairwise_weibull(w_sets,w_entries,w_iterations,k):
    agreement = 0
    for x in range(w_iterations):
        sets = create_sets_weibull(2, w_entries, k)
        results = compairwise(sets)
        if results[0] == results[1]:
            agreement += 1
        
    agreement_rate = agreement/w_iterations
    
    return agreement_rate
