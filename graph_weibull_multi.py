import matplotlib.pyplot as plt

from weibull_multi import gap_percentile_iterate, expected_gap_percentile

import math

def graph_gap_vs_expected_gini(p, sets, iterations, k):
    gap_expected = expected_gap_percentile(p, sets)
    gap_simulated, blank = gap_percentile_iterate(p, sets, iterations, k)
    
    plt.rcParams['figure.dpi'] = 300
    
    ax = plt.gca()
    ax.set_ylim([-sets/2,sets/2])
    ax.set_xlim([0,1])
    
    plt.minorticks_on()
    
    #plt.xticks(ticks = list(range(0,1,p)))
    plt.tick_params(axis='both', labelsize = 8)
    
    plt.grid()
    
    p_cummulative = p/2
    for x in range(len(gap_simulated)):
        plt.scatter(p_cummulative, gap_expected[x], s=20, c="blue")
        plt.scatter(p_cummulative, gap_simulated[x], s=20, c="red")
        p_cummulative += p
        print(p_cummulative)
    
    plt.title("Expected vs Simulated Gap")
    plt.xlabel("Percentile")
    plt.ylabel("Gap")
    
    plt.legend(loc=4, fontsize='5')
    
    
    
    plt.show
    
    return


def graph_gap_var_vs_gini(p, sets, iterations, k, avg_gini, avg_variance):
    #avg_gini, avg_variance, var_gini, var_variance = gap_percentile_iterate(p, sets, iterations, k)
    
    plt.rcParams['figure.dpi'] = 300
    
    ax = plt.gca()
    ax.set_ylim([0,150])
    ax.set_xlim([0,51])
    
    plt.minorticks_on()
    
    #plt.xticks(ticks = list(range(0,1,p)))
    plt.tick_params(axis='both', labelsize = 8)
    
    plt.grid()
    

    for x in range(len(avg_gini)-1):
        plt.scatter(x+1, avg_gini[x], s=20, c="blue")
        plt.scatter(x+1, avg_variance[x], s=20, c="red")
        #plt.plot([x+1,x+1], [avg_gini[x]-3.3*math.sqrt(var_gini[x]/10000),avg_gini[x]+3.3*math.sqrt(var_gini[x]/10000)], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_gini[x]+3.3*math.sqrt(var_gini[x]/10000),avg_gini[x]+3.3*math.sqrt(var_gini[x]/100000)], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_gini[x]-3.3*math.sqrt(var_gini[x]/10000),avg_gini[x]-3.3*math.sqrt(var_gini[x]/100000)], color="grey")
        #plt.plot([x+1,x+1], [avg_variance[x]-3.3*math.sqrt(var_variance[x]/10000),avg_variance[x]-3.3*math.sqrt(var_variance[x]/100000),], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_variance[x]-3.3*math.sqrt(var_variance[x]/10000),avg_variance[x]-3.3*math.sqrt(var_variance[x]/10000)], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_variance[x]+3.3*math.sqrt(var_variance[x]/10000),avg_variance[x]+3.3*math.sqrt(var_variance[x]/10000)], color="grey")
        print(x)
    
    plt.scatter(len(avg_gini), avg_gini[x+1], s=20, c="blue", label = "Gini")
    plt.scatter(len(avg_gini), avg_variance[x+1], s=20, c="red", label = "Log Variance")
    
    
    plt.title("Gini and Log Variance Gap")
    plt.xlabel("Rank")
    plt.ylabel("Gap")
    
    plt.legend(loc=4, fontsize='5')
    
    
    
    plt.show
    
    return 

def graph_gap_var_vs_gini_2(avg_gini, avg_variance):
    #avg_gini, avg_variance, var_gini, var_variance = gap_percentile_iterate(p, sets, iterations, k)
    
    plt.rcParams['figure.dpi'] = 300
    
    ax = plt.gca()
    ax.set_ylim([0,200])
    ax.set_xlim([0,51])
    
    plt.minorticks_on()
    
    #plt.xticks(ticks = list(range(0,1,p)))
    plt.tick_params(axis='both', labelsize = 8)
    
    plt.grid()
    

    for x in range(len(avg_gini)-1):
        plt.scatter(x+1, avg_gini[x], s=20, c="blue")
        plt.scatter(x+1, avg_variance[x], s=20, c="red")
        #plt.plot([x+1,x+1], [avg_gini[x]-3.3*math.sqrt(var_gini[x]/10000),avg_gini[x]+3.3*math.sqrt(var_gini[x]/10000)], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_gini[x]+3.3*math.sqrt(var_gini[x]/10000),avg_gini[x]+3.3*math.sqrt(var_gini[x]/100000)], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_gini[x]-3.3*math.sqrt(var_gini[x]/10000),avg_gini[x]-3.3*math.sqrt(var_gini[x]/100000)], color="grey")
        #plt.plot([x+1,x+1], [avg_variance[x]-3.3*math.sqrt(var_variance[x]/10000),avg_variance[x]-3.3*math.sqrt(var_variance[x]/100000),], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_variance[x]-3.3*math.sqrt(var_variance[x]/10000),avg_variance[x]-3.3*math.sqrt(var_variance[x]/10000)], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_variance[x]+3.3*math.sqrt(var_variance[x]/10000),avg_variance[x]+3.3*math.sqrt(var_variance[x]/10000)], color="grey")
        print(x)
    
    plt.scatter(len(avg_gini), avg_gini[x+1], s=20, c="blue", label = "Gini")
    plt.scatter(len(avg_gini), avg_variance[x+1], s=20, c="red", label = "Log Variance")
    
    
    plt.title("Gini and Log Variance Gap")
    plt.xlabel("Rank")
    plt.ylabel("Gap")
    
    plt.legend(loc=4, fontsize='5')
    
    
    
    plt.show
    
    return 

def graph_gap_top_vs_bottom_gini(p, sets, iterations, k, avg_gini, avg_variance, var_gini, var_variance):
    #avg_gini, avg_variance, var_gini, var_variance = gap_percentile_iterate(p, sets, iterations, k)
    
    plt.rcParams['figure.dpi'] = 300
    
    ax = plt.gca()
    ax.set_ylim([-sets/20,sets/5])
    ax.set_xlim([0,len(avg_gini)/2+1])
    
    plt.minorticks_on()
    
    #conf = 1
    
    #plt.xticks(ticks = list(range(0,1,p)))
    plt.tick_params(axis='both', labelsize = 8)
    
    plt.grid()
    
    for x in range(int(len(avg_gini)/2)-1):
        
        #plt.plot([x+1,x+1], [avg_gini[x]-conf,avg_gini[x]+conf], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_gini[x]+conf,avg_gini[x]+conf], color="grey")
        #plt.plot([x+.85,x+1.15], [avg_gini[x]-conf,avg_gini[x]-conf], color="grey")
        #plt.plot([x+1,x+1], [abs(avg_gini[-x-1])-conf,abs(avg_gini[-x-1])+conf], color="grey")
        #plt.plot([x+.85,x+1.15], [abs(avg_gini[-x-1])+conf,abs(avg_gini[-x-1])+conf], color="grey")
        #plt.plot([x+.85,x+1.15], [abs(avg_gini[-x-1])-conf,abs(avg_gini[-x-1])-conf], color="grey")
        plt.scatter(x+1, abs(avg_gini[x]), s=20, c="blue")
        plt.scatter(x+1, abs(avg_gini[-x-1]), s=20, c="red")
        
        
    
    plt.scatter(len(avg_gini)/2, abs(avg_gini[x+1]), s=20, c="blue", label = "Top Half")
    plt.scatter(len(avg_gini)/2, abs(avg_gini[x+2]), s=20, c="red", label = "Bottom Half")

    print(x)
    
    plt.title("Gini Gap")
    plt.xlabel("Rank")
    plt.ylabel("Gap (Absolute Value)")
    
    plt.legend(loc=4, fontsize='5')
    
    
    
    plt.show
    
    return

def graph_gap_top_vs_bottom_variance(p, sets, iterations, k, avg_gini, avg_variance, var_gini, var_variance):
    #avg_gini, avg_variance, var_gini, var_variance = gap_percentile_iterate(p, sets, iterations, k)
    
    plt.rcParams['figure.dpi'] = 300
    
    ax = plt.gca()
    ax.set_ylim([-sets/20,sets/5])
    ax.set_xlim([0,len(avg_variance)/2+1])
    
    plt.minorticks_on()
    
    #plt.xticks(ticks = list(range(0,1,p)))
    plt.tick_params(axis='both', labelsize = 8)
    
    plt.grid()
    
    for x in range(int(len(avg_gini)/2)-1):
        plt.scatter(x+1, abs(avg_variance[x]), s=20, c="blue")
        plt.scatter(x+1, abs(avg_variance[-x-1]), s=20, c="red")
        
    
    plt.scatter(len(avg_gini)/2, abs(avg_variance[x+1]), s=20, c="blue", label = "Top Half")
    plt.scatter(len(avg_gini)/2, abs(avg_variance[x+2]), s=20, c="red", label = "Bottom Half")
    print(x)
    
    plt.title("Variance Gap")
    plt.xlabel("Rank")
    plt.ylabel("Gap (Absolute Value)")
    
    plt.legend(loc=4, fontsize='5')
    
    
    
    plt.show
    
    return