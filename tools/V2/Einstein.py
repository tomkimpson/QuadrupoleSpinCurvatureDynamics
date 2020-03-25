from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy.signal import argrelextrema
from scipy import interpolate


#Setup plotting environment
plt.style.use('science')
fig, (ax1,ax2,ax3) =plt.subplots(3, 1, sharex=True, figsize=(10,10))



#Set observer location
ObsTheta = np.pi/4
ObsPhi = 0.0
ObsX = np.sin(ObsTheta)*np.cos(ObsPhi)
ObsY = np.sin(ObsTheta)*np.sin(ObsPhi)
ObsZ = np.cos(ObsTheta)


#convert time
convert_s = 0.203393735668199405699775876374792498
convert_s = 4.71911219647794444779062358178172841E-0002 #Sgr A*
#convert_s = 203.393735668199405699775876374792498 #GlobClus


#set what you want the x-axis to be


#paths to dirs
root = os.environ['QuadDir']
path = 'V2/Einstein/'
def get_data(f):

    data = np.loadtxt(f,skiprows=1)
    
    phase = data[:,0] #tau / P
    einstein = data[:,1]
    

    return phase, einstein




    #return t/(convert_s), roemer/(convert_s) 
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
        ax1.plot(tau1,y1/3600) #hours
        ax3.plot(tau1,(y2-y1) * 1e6) #microseconds

    if ID == 'AC':
        ax2.plot(tau1,(y2-y1)) #seconds





#null plot for color cycle
for i in range(3):
    ax1.plot([], [])
    ax2.plot([], [])
    ax3.plot([], [])



#e02
eStrings = ['e06/', 'e04/', 'e02/']
pStrings = ['P01/', 'P005/', 'P001/']
eStrings = ['']
pStrings = ['']

for e in pStrings:
    FileA = root+path+e+'A.txt'
    FileB = root+path+e+'B.txt'
    FileC = root+path+e+'C.txt'
    compare(FileA, FileB,'AB') # compare a quasi Kerr ST with/without spin couplings
    compare(FileA, FileC,'AC') #compare a Kerr ST w/ quasi WITH spin couplings



#Format
fs = 20



all_axes = plt.gcf().get_axes()
for ax in all_axes:
    ax.locator_params(axis='both', nbins=5) #set number of xticks
    ax.tick_params(axis='both', which='major', labelsize=fs-4) #set size of numbers
    

#Label axes
ax3.set_xlabel(r'$ \tau / P $',fontsize=fs)

fontsize=fs

ax1.set_ylabel(r'$\Delta_{\rm E}$ [hr]',fontsize=fs)
ax2.set_ylabel(r'$ \delta_{\epsilon} \Delta_{\rm E}$ [s]',fontsize=fs)
ax3.set_ylabel(r'$\delta_{\lambda} \Delta_{\rm E} \, [\mu$s$]$', fontsize=fs)




plt.subplots_adjust(hspace = 0.01)
plt.setp(ax1.get_xticklabels(),visible=False)
plt.setp(ax2.get_xticklabels(),visible=False)


savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
plt.savefig(savepath+'Einstein.png', dpi = 300,bbox='tight')
plt.show()

