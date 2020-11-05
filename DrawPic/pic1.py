import csv
import numpy as np
import sys
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

def readCsv(samplename,resultname,sampleindex):
    with open(samplename) as sn:
        reader = csv.reader(sn)
        xlabel = []
        for row in reader:
            xlabel.append(float(row[sampleindex]))

    with open(resultname) as rn:
        reader=csv.reader(rn)
        totalEnergy = []
        for row in reader:
            totalEnergy.append(float(row[0]))
    currentMax = max(totalEnergy)
    tcount = totalEnergy.count(currentMax)
    for i in range(0,tcount):
        currentIndex = totalEnergy.index(currentMax)
        del xlabel[currentIndex]
        totalEnergy.remove(currentMax) 
    return xlabel,totalEnergy
    
def fit(xlabel,ylabel,n):
    poly = np.polyfit(xlabel,ylabel,deg=n)
    z = np.polyval(poly,xlabel)
    return z
def drawPic(x,y,lw=5,lineCol='tab:orange',baseLineCol='r'):
    fig,ax = plt.subplots(1,4,sharey=True)

    sxlabel=['ratio','d0','n','d1']
    ax[0].set_ylabel('total energy(Kwh/m³)', fontsize=20)
    plt.setp(ax[0].get_yticklabels(),fontsize=15)

    for a,xl,i in zip(ax,sxlabel,range(4)):
        a.plot(x[i],y[i],linewidth=lw,color=lineCol)
        a.spines['bottom'].set_linewidth(4)
        a.axhline(y=23.61, c=baseLineCol, ls='--', lw=2)
        a.grid(color='black',linestyle='-',linewidth=1)
        a.spines['left'].set_linewidth(4)
        a.spines['right'].set_linewidth(4)
        a.spines['top'].set_linewidth(4)
        a.set_xlabel(xl, fontsize=20)
        plt.setp(a.get_xticklabels(),fontsize=15)

    fig.subplots_adjust(wspace=0.25)
    ax[0].set(ylim=(23.0,25.5))
    plt.show()


ratio,ratioTe = readCsv('sample1.csv','result1.csv',1)
d0,d0Te = readCsv('sample2.csv','result2.csv',2)
n,nTe = readCsv('sample3.csv','result3.csv',0)
d1,d1Te = readCsv('sample4.csv','result4.csv',3)

ratioZ = fit(ratio,ratioTe,1)
d0Z = fit(d0,d0Te,1)
nZ = fit(n,nTe,3)
d1Z =fit(d1,d1Te,1)

x = [ratio,d0,n,d1]
y = [ratioZ,d0Z,nZ,d1Z]

drawPic(x,y)