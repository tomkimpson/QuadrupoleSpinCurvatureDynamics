from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os








#Set up plotting environment
fig = plt.figure(figsize=(20,10))
ax1 = plt.subplot2grid((1,1), (0,0))


#Load data
path = os.environ['QuadDir']
alldata = glob.glob(path+'periastron*.txt')

print (alldata)

def plotter(datafile):
    data = np.loadtxt(datafile)
    d_omega = data[:,0]
    a = data[:,1]


    ax1.plot(a,d_omega)




for f in alldata:
    plotter(f)

plt.show()


