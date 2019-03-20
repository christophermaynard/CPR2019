#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

def plot2Data(x, y1, y2):

    fig, ax = plt.subplots()
    xlim=[15,500]
    ax.set_xlim(xlim[0],xlim[1])
    width1=0.1*x
    width2=0.1*x
    rects1 = ax.bar(0.95*x, y1, width1, color='firebrick',label="MPI",edgecolor='black')
    rects2 = ax.bar(1.05*x, y2, width2, color='goldenrod',label="OMP",edgecolor='black')
#    l1 = ax.plot(psx,psy,color='black',linestyle='dashed',label="perfect scaling")
    ax.legend(loc='upper right')
    ax.set_xscale('log')
#    ax.set_yscale('log')

 #   yax = [200, 400, 800, 1600, 3200]
 #   ax.set_yticks(yax)
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")

#    fstem="strong-scale"
    fstem="wc-scale"
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    fname=fstem+".eps"
    plt.savefig(fname,format="eps")    
    plt.show()


fname="perf.dat"
data=np.genfromtxt(fname, skip_header=1, usecols=range(0,7))
nodes=np.array(data[0:5,0])
print nodes
T6W=np.array(data[0:5,1])
T1W=np.array(data[5:10,1])
print T6W
print T1W


#nodes=np.array(sdata[:,0])
#mpidat=np.array(sdata[:,1])
#ompdat=np.array(sdata[:,2])

plot2Data(nodes, T1W, T6W)

