# -*- coding: utf-8 -*-

from pairwise import create_sets_exponential, create_sets_normal, create_sets_uniform, compairwise
#----------------------------------------------------------------------------

#Functions that sort distribution pairs into whether or not they agreed

def simulate_pairwise_uniform_sort(u_sets,u_entries,u_iterations):
    agreement = 0
    matching = []
    non_matching = []
    for x in range(u_iterations):
        sets = create_sets_uniform(2, u_entries)
        results = compairwise(sets)
        if results[0] == results[1]:
            agreement += 1
            matching.append(sets)
        else:
            non_matching.append(sets)
        
    agreement_rate = agreement/u_iterations
    
    return agreement_rate, matching, non_matching

def simulate_pairwise_normal_sort(n_sets,n_entries,n_iterations,center):
    agreement = 0
    matching = []
    non_matching = []
    for x in range(n_iterations):
        sets = create_sets_normal(2, n_entries, center)
        results = compairwise(sets)
        if results[0] == results[1]:
            agreement += 1
            matching.append(sets)
        else:
            non_matching.append(sets)
        
    agreement_rate = agreement/n_iterations
    
    return agreement_rate, matching, non_matching

def simulate_pairwise_exponential_sort(e_sets,e_entries,e_iterations):
    agreement = 0
    matching = []
    non_matching = []
    for x in range(e_iterations):
        sets = create_sets_exponential(2, e_entries)
        results = compairwise(sets)
        if results[0] == results[1]:
            agreement += 1
            matching.append(sets)
        else:
            non_matching.append(sets)
        
    agreement_rate = agreement/e_iterations
    
    return agreement_rate, matching, non_matching
        


