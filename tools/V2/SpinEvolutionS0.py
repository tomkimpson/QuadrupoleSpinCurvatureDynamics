from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy.signal import argrelextrema




#Some constants
Msolar = 1.989e30
c = 3e8
G=6.67e-11
MBH = 4.31e6 * Msolar
convert_m = c**2/(G*MBH)
convert_s = convert_m * c
convert_year = 365*24*3600
convert_m = convert_m * 1e3 



#Setup plotting environment
plt.style.use('science')
fig, (ax1,ax2) =plt.subplots(2, 1, sharex=True, figsize=(10,10))


#Set path to files
root = os.environ['QuadDir']
path = 'V2/SpinEvolution/'

def get_data(f):

    data = np.loadtxt(f)
    
    tau = data[:,0]
    phi = data[:,1]
    y = data[:,4]

    return tau, y

def crop(A,B,L):
    return A[0:L], B[0:L]

def compare(f1,f2,ID):

    tau1, y1 = get_data(f1)
    tau2, y2 = get_data(f2)

    #Check lengths are the same
    if (len(tau1) != len(tau2)):
        print ('lengths are not the same')
        minL = min(len(tau1), len(tau2))

        tau1,y1 = crop(tau1,y1,minL)
        tau2,y2 = crop(tau2, y2,minL)



    ax1.plot(tau1,y1*1e7,linestyle=ID)
    ax2.plot(tau1,(y2-y1)*1e9,linestyle=ID)



spin = 'a-06/'
eStrings = ['e06/', 'e04/', 'e02/']
for e in eStrings:
    FileA = root+path+spin+e+'A.txt'
    FileB = root+path+spin+e+'B.txt'
    FileC = root+path+spin+e+'C.txt'
    compare(FileA, FileC,'solid') #compare a Kerr ST w/ quasi WITH spin couplings

'''
spin = 'a-06/'
for e in eStrings:
    FileA = root+path+spin+e+'A.txt'
    FileB = root+path+spin+e+'B.txt'
    FileC = root+path+spin+e+'C.txt'
    compare(FileA, FileC,'--') #compare a Kerr ST w/ quasi WITH spin couplings
'''




#Format
fs = 20



all_axes = plt.gcf().get_axes()
for ax in all_axes:
    ax.locator_params(axis='both', nbins=5) #set number of xticks
    ax.tick_params(axis='both', which='major', labelsize=fs-4) #set size of numbers
    

#Label axes
ax2.set_xlabel(r'$ \tau$ [s]',fontsize=fs)

fontsize=fs

ax1.set_ylabel(r'$s^{0} \times 10^7$',fontsize=fs)
ax2.set_ylabel(r'$ \delta_{\epsilon} s^0 \times 10^9 $',fontsize=fs)




plt.subplots_adjust(hspace = 0.01)
plt.setp(ax1.get_xticklabels(),visible=False)


savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
plt.savefig(savepath+'SpinS0.png', dpi = 300,bbox='tight')
plt.show()

