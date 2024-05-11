import matplotlib.pyplot as plt

from pairwise import simulate_pairwise_normal

x1 = 6
x2 = 100

centers = list(range(x1,x2,2))

def norm_robust_on_center(entries, iterations):
    agreements=[]
    for x in centers:
        print(x)
        result = simulate_pairwise_normal(2, entries, iterations, x)
        agreements.append(result)
    
    return agreements

def graph_normal_robustness():
    
    plt.rcParams['figure.dpi'] = 300
    
    n = norm_robust_on_center(20, 100000)
    
    plt.scatter(centers, n, s=15, c="blue")
    
    plt.title('Robustness of Normal Distribution')
    plt.xlabel("Mean of Normal Distribution")
    plt.ylabel("Agreement Rate")
    
    ax = plt.gca()
    ax.set_ylim([.75,1])
    ax.set_xlim([0,100])
    
    plt.minorticks_on()
    
    plt.xticks(ticks = list(range(25,101,25)))
    plt.tick_params(axis='both', labelsize = 8)
    
    plt.grid()
    
    plt.show
    
    return

