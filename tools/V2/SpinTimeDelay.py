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
fig, (ax1,ax2,ax3) =plt.subplots(3, 1, sharex=True, figsize=(10,10))


root = os.environ['QuadDir']
path = 'V2/Spin_and_Aberration/'



def get_data(f):

    data = np.loadtxt(f)
    
    tau = data[:,6]
    phi = data[:,1]
    stheta = data[:,2]
    sphi = data[:,3]
    Xc = data[:,5]

    #ax1.plot(tau, Xc)

    #Calculate the time delay
    delta_Xc = Xc-Xc[0]

    Ps = 1e-3 #seconds
    delta_t = Ps *delta_Xc / (2*np.pi)
    
    delta_t = delta_t * 1e6 #microseconds

    #ax1.plot(tau,Xc)
    #ax2.plot(tau,sphi)
    #ax3.plot(tau, delta_t)

    return tau, delta_t


def crop(A,B,L):
    return A[0:L], B[0:L]

def compare(f1,f2,ID):

    x1,y1 = get_data(f1)
    x2,y2 = get_data(f2)




    if ID == 'AB':
        ax1.plot(x1,y1)
        ax3.plot(x1,(y2-y1)*1e3) #ns

    if ID == 'AC':
        ax2.plot(x1,(y2-y1)*1e3) #ns



eStrings = ['e06/','e07/','e08/', 'e09/']
for e in eStrings:
    FileA = root+path+e+'A.txt'
    FileB = root+path+e+'B.txt'
    FileC = root+path+e+'C.txt'
    

    compare(FileA, FileB, 'AB')
    compare(FileA, FileC, 'AC')

#Format
fs = 20



all_axes = plt.gcf().get_axes()
for ax in all_axes:
    ax.locator_params(axis='both', nbins=5) #set number of xticks
    ax.tick_params(axis='both', which='major', labelsize=fs-4) #set size of numbers
    


plt.subplots_adjust(hspace = 0.01)
plt.setp(ax1.get_xticklabels(),visible=False)
plt.setp(ax2.get_xticklabels(),visible=False)



ax3.set_xlabel(r'$ \tau / P $',fontsize=fs)

ax1.set_ylabel(r'$\Delta t [\mu s]$',fontsize=fs)
ax2.set_ylabel(r'$ \delta_{\epsilon} \Delta t$ [ns]',fontsize=fs)
ax3.set_ylabel(r'$ \delta_{\lambda} \Delta t$ [ns]',fontsize=fs)






savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'



plt.savefig(savepath+'SpinDelays.png', dpi = 300,bbox='tight')
plt.show()

