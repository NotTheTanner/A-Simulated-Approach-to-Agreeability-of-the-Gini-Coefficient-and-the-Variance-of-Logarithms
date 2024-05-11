# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:47:36 2024

@author: Jack
"""

import scipy.stats as tests
import math

def ttest(x, avg_g, var_g, avg_v, var_v):
    result = tests.ttest_ind_from_stats(avg_g[x], math.sqrt(var_g[x]), 100000, avg_v[x], math.sqrt(var_v[x]), 100000, equal_var=False)
    
    return result