from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy.signal import argrelextrema
sys.path.insert(1, '../modules/')
from CriticalPhaseAngle import CalculateChi


#Setup plotting environment
plt.style.use('science')
fig, ax1 =plt.subplots(1, 1, sharex=True, figsize=(10,10))


root = os.environ['QuadDir']
path = 'V2/Spin_and_Aberration/'



def get_data(f):

    data = np.loadtxt(f)
    
    tau = data[:,6]
    phi = data[:,1]
    stheta = data[:,2]
    sphi = data[:,3]
    Xc = data[:,5]


    #Calculate the time delay
    delta_Xc = Xc-Xc[0]

    Ps = 1e-3 #seconds
    delta_t = Ps *delta_Xc / (2*np.pi)
    
    delta_t = delta_t * 1e6 #microseconds

    ax1.plot(tau,delta_t)





eStrings = ['e06/','e07/','e08/', 'e09/']
#eStrings = ['e09/']
for e in eStrings:
    FileA = root+path+e+'C.txt'
    get_data(FileA)



#Format
fs = 20



all_axes = plt.gcf().get_axes()
for ax in all_axes:
    ax.locator_params(axis='both', nbins=5) #set number of xticks
    ax.tick_params(axis='both', which='major', labelsize=fs-4) #set size of numbers
    



ax1.set_xlabel(r'$ \tau / P $',fontsize=fs)
ax1.set_ylabel(r'$\Delta t [\mu s]$',fontsize=fs)


savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'



plt.savefig(savepath+'SpinDelays.png', dpi = 300,bbox='tight')
plt.show()

