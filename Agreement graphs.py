import matplotlib.pyplot as plt

from pairwise import simulate_pairwise_exponential, simulate_pairwise_normal, simulate_pairwise_uniform

entries_values = list(range(100,1000,100))

def exponential_on_entries():
    agreement_rates_exp = []
    for x in entries_values:
        rate_exp = simulate_pairwise_exponential(2, x, 5000)
        agreement_rates_exp.append(rate_exp)
        
    return agreement_rates_exp

def uniform_on_entries():
    agreement_rates_unif = []
    for x in entries_values:
        rate_unif = simulate_pairwise_uniform(2, x, 5000)
        agreement_rates_unif.append(rate_unif)
        
    return agreement_rates_unif

def normal_on_entries():
    agreement_rates_norm = []
    for x in entries_values:
        rate_norm = simulate_pairwise_normal(2, x, 5000, 25)
        agreement_rates_norm.append(rate_norm)
        
    return agreement_rates_norm

def graph():
    
    plt.rcParams['figure.dpi'] = 300
    
    e = exponential_on_entries()
    print("Done with exponentials") #Progress check, can be removed
    u = uniform_on_entries()
    print("Done with uniforms")
    n = normal_on_entries()
    print("Done with normal") 
    
    ax = plt.gca()
    ax.set_ylim([.5,1])
    ax.set_xlim([0,1000])
    
    plt.minorticks_on()
    
    plt.xticks(ticks = list(range(100,1001,100)))
    plt.tick_params(axis='both', labelsize = 8)
    
    plt.grid()
    
    plt.scatter(entries_values, e, s=20, c="red", label="Exponential")
    plt.scatter(entries_values, u, s=20, c="blue", label="Uniform")
    plt.scatter(entries_values, n, s=20, c="green", label='Normal')
    
    plt.title("Agreement Rate by Distribution")
    plt.xlabel("Number of Entries")
    plt.ylabel("Agreement Rate")
    
    plt.legend(loc=4, fontsize='5')
    
    
    
    plt.show
    
    return


#https://matplotlib.org/stable/users/project/citing.html