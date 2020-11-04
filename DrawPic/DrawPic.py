import csv
import numpy as np
from matplotlib import pyplot as plt

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
def roration(ax):
    for ticklabel in ax.xaixs.get_ticklabels():
        ticklabel.set_rotation(30)

ratio,ratioTe = readCsv('sample1.csv','result1.csv',1)
d0,d0Te = readCsv('sample2.csv','result2.csv',2)
n,nTe = readCsv('sample3.csv','result3.csv',0)
d1,d1Te = readCsv('sample4.csv','result4.csv',3)

fig,ax = plt.subplots(1,4,sharey=True)

ratioZ = fit(ratio,ratioTe,1)
d0Z = fit(d0,d0Te,1)
nZ = fit(n,nTe,3)
d1Z =fit(d1,d1Te,1)

ax[0].plot(ratio,ratioZ)
ax[0].set_title('TotaleEnergy change with ratio')
ax[1].plot(d0,d0Z)
ax[1].spines['left'].set_color('white')
ax[1].yaxis.set_ticks_position('right')
ax[1].set_title('TotaleEnergy change with d0')
ax[2].plot(n,nZ)
ax[2].spines['left'].set_color('white')
ax[2].yaxis.set_ticks_position('right')
ax[2].set_title('TotaleEnergy change with n')
ax[3].plot(d1,d1Z)
ax[3].spines['left'].set_color('white')
ax[3].yaxis.set_ticks_position('right')
ax[3].set_title('TotaleEnergy change with d1')
fig.subplots_adjust(wspace=0)
plt.show()
