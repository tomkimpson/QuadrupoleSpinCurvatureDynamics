from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy.signal import argrelextrema



#Setup plotting environment
plt.style.use('science')
fig, (ax1,ax2,ax3) =plt.subplots(3, 1, sharex=True, figsize=(10,10))




#Do you want to look at theta_spin or phi_spin
idx = 3 #2 = theta, 3=phi


#Normalisataion factors

if idx == 3:
    factorAB = 1e5
    factorAC = 1e3
if idx == 2:
    factorAB = 1e5
    factorAC = 1e4
#Set path to files

root = os.environ['QuadDir']
path = 'V2/SpinEvolution/'
path = 'V2/SpinEvolution/M6/'
spin = 'a+06/'
def get_data(f):

    data = np.loadtxt(f)
    
    tau = data[:,0]
    phi = data[:,1]
    y = data[:,idx]
    #y = data[:,4]

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








    if ID == 'AB':
        ax1.plot(tau1,y1)
        ax3.plot(tau1,(y2-y1)*factorAB)

    if ID == 'AC':
        ax2.plot(tau1,(y2-y1)*factorAC)




#e02
eStrings = ['e06/', 'e04/', 'e02/']
#eStrings = ['e06/']
for e in eStrings:
    FileA = root+path+spin+e+'A.txt'
    FileB = root+path+spin+e+'B.txt'
    FileC = root+path+spin+e+'C.txt'
    compare(FileA, FileB,'AB') # compare a quasi Kerr ST with/without spin couplings
    compare(FileA, FileC,'AC') #compare a Kerr ST w/ quasi WITH spin couplings



#Format
fs = 20



all_axes = plt.gcf().get_axes()
for ax in all_axes:
    ax.locator_params(axis='both', nbins=5) #set number of xticks
    ax.tick_params(axis='both', which='major', labelsize=fs-4) #set size of numbers
    

#Label axes
ax3.set_xlabel(r'$ \tau$ [s]',fontsize=fs)

fontsize=fs

if idx == 2:
    ax1.set_ylabel(r'$\theta_{\rm spin}$',fontsize=fs)
    ax2.set_ylabel(r'$ \delta_{\epsilon} \theta_{\rm spin} \times 10^4$',fontsize=fs)
    ax3.set_ylabel(r'$\delta_{\lambda} \theta_{\rm spin} \times 10^5$', fontsize=fs)

if idx == 3:
    ax1.set_ylabel(r'$\phi_{\rm spin}$', fontsize=fs)
    ax2.set_ylabel(r'$ \delta_{\epsilon} \phi_{\rm spin} \times 10^3$', fontsize=fs)
    ax3.set_ylabel(r'$\delta_{\lambda} \phi_{\rm spin} \times 10^5$', fontsize=fs)



plt.subplots_adjust(hspace = 0.01)
plt.setp(ax1.get_xticklabels(),visible=False)
plt.setp(ax2.get_xticklabels(),visible=False)


savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
#plt.savefig(savepath+'Spin'+str(idx)+'.png', dpi = 300,bbox='tight')
plt.show()

