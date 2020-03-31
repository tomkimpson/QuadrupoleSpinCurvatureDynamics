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

left, bottom, width, height = [0.15, 0.45, 0.15, 0.15]
ax4 = fig.add_axes([left, bottom, width, height])





root = os.environ['QuadDir']
path = 'V2/Spin_and_Aberration/beamwidth/'



#beam opening angle
gamma = 10 * np.pi/180
psi = np.pi/12


def cot(x):

    return np.cos(x) / np.sin(x)


def csc(x):
    return 1/np.sin(x)


def beamwidth(stheta,gamma,psi):

    out = np.arccos(-13.928203230275507 + 14.928203230275507*np.cos(gamma))

    out = np.arccos(-3.7320508075688776*cot(psi) + 3.8637033051562737*np.cos(gamma)*csc(psi))


    out = np.arccos((-np.cos(stheta)*cot(psi) + 1.4142135623730951*np.cos(gamma)*csc(psi) - cot(psi)*np.sin(stheta))/(np.cos(stheta) - np.sin(stheta)))


    return 2*out



def get_data(f):

    data = np.loadtxt(f)
    
    tau = data[:,6]
    phi = data[:,1]
    stheta = data[:,2]

 #   stheta = np.ones((len(tau))) * np.pi/6


    w = beamwidth(stheta,gamma,psi)
    w = w/w[0] #as a fractional difference


    return tau, w

def crop(A,B,L):
    return A[0:L], B[0:L]

def compare(f1,f2,ID):
    x1,y1 = get_data(f1)
    x2,y2 = get_data(f2)




    if ID == 'AB':
        ax3.plot(x1,abs(y2-y1)*1e5)
        ax1.plot(x1,y1)

    if ID == 'AC':
        ax2.plot(x1,abs(y2-y1)*1e4)
        ax4.plot(x1,abs(y2-y1))



eStrings = ['e09/', 'e08/', 'e07/', 'e06/']
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
plt.setp(ax2.get_xticklabels(),visible=False)
plt.setp(ax4.get_xticklabels(),visible=False)
plt.setp(ax4.get_yticklabels(),visible=False)


ax4.set_xlim(3.10,3.20)
#ax4.set_ylim(-0.00008,0.00017)
ax4.set_ylim(0,0.00017)

ax3.set_xlabel(r'$ \tau / P $',fontsize=fs)

ax1.set_ylabel(r'$ w / w_0 $',fontsize=fs)
ax2.set_ylabel(r'$ |\delta_{\epsilon } w / w_0| \times 10^4$',fontsize=fs)
ax3.set_ylabel(r'$ |\delta_{\lambda } w / w_0| \times 10^5$',fontsize=fs)


#configure inset plot

savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'



plt.savefig(savepath+'beam_width.png', dpi = 300,bbox='tight')
plt.show()

