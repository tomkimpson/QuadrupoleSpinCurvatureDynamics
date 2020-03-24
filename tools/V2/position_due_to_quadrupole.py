from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy.signal import argrelextrema



plt.style.use('science')
#fig = plt.figure(figsize=(10,10))
#ax1 = plt.subplot2grid((3,1), (0,0))
#ax2 = plt.subplot2grid((3,1), (1,0),sharex=ax1)
#ax3 = plt.subplot2grid((3,1), (2,0),sharex=ax1)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10,10))


def PlotEinstein(fname):
    
    data = np.loadtxt(fname)


    tau = data[:,10] / (convert_s)

#Set path to files

root = os.environ['QuadDir']
path = 'V2/SpatialTrajectory/'


files02 = glob.glob(root+path+'e02/*.txt')
files04 = glob.glob(root+path+'e04/*.txt')
files06 = glob.glob(root+path+'e06/*.txt')


all_files = [files06,files04, files02]# , files05,files09]



def get_vector(f):

    data = np.loadtxt(f)
    tau = data[:,12]

    r = data[:,4]
    theta = data[:,5]
    phi = data[:,6]

    return tau,r,theta,phi





def crop(A,B,C,D,L):
    return A[0:L], B[0:L], C[0:L], D[0:L]



def process(f1,f2):


    tau1,r1,theta1,phi1 = get_vector(f1) 
    tau2,r2,theta2,phi2 = get_vector(f2) 


    if (len(tau1) != len(tau2)):
        print ('lengths are not the same')
        minL = min(len(tau1), len(tau2))

        tau1,r1,theta1,phi1 = crop(tau1,r1,theta1,phi1,minL)
        tau2,r2,theta2,phi2 = crop(tau2,r2,theta2,phi2,minL)






    dr = r2-r1
    dtheta = (theta2-theta1) * 1e9
    dphi = phi2-phi1


    plotX = phi1 / np.pi
 #   plotX = r1

    ax1.plot(plotX,dr)
    ax2.plot(plotX,dtheta)
    ax3.plot(plotX,dphi)




for f in all_files:
    f1 = f[0]
    f2 = f[1]
    process(f1,f2)

#Format
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fs = 20



#Number of xticks
ax1.locator_params(axis='both', nbins=2)

ax2.locator_params(axis='y', nbins=2)
ax2.locator_params(axis='x', nbins=5)


ax3.locator_params(axis='y', nbins=2)
ax3.locator_params(axis='x', nbins=5)



plt.setp(ax1.get_xticklabels(),visible=False)
plt.setp(ax2.get_xticklabels(),visible=False)




ax1.tick_params(axis='both', which='major', labelsize=fs-4)
ax2.tick_params(axis='both', which='major', labelsize=fs-4)
ax3.tick_params(axis='both', which='major', labelsize=fs-4)



plt.subplots_adjust(hspace = 0.01)

upper = 1.0
lower = -0.1

#ax1.set_ylim(lower,upper)
#ax2.set_ylim(lower,upper)



ax1.set_ylabel(r'$\delta_{\epsilon} r \, [r_g]$',fontsize=fs)
ax2.set_ylabel(r'$\delta_{\epsilon} \theta \times 10^9$',fontsize=fs)
ax3.set_ylabel(r'$\delta_{\epsilon} \phi $',fontsize=fs)

ax3.set_xlabel(r'$ \phi / \pi$',fontsize=fs)

ax1.tick_params(axis='both', which='major', labelsize=fs-4)



savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
plt.savefig(savepath+'Orbital1.png', dpi = 300,bbox='tight')

plt.show()
