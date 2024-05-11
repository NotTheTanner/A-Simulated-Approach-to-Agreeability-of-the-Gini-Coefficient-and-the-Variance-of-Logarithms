# -*- coding: utf-8 -*-

from pairwisewithstoring import simulate_pairwise_exponential_sort, simulate_pairwise_normal_sort, simulate_pairwise_uniform_sort

exp_agree,exp_match,exp_nomatch = simulate_pairwise_exponential_sort(2, 30, 1000)
unif_agree,unif_match,unif_nomatch = simulate_pairwise_uniform_sort(2, 30, 1000)
norm_agree,norm_match,norm_nomatch = simulate_pairwise_normal_sort(2, 30, 1000, 10)

