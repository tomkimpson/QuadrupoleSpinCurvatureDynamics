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
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10,10))






#Set path to files

root = os.environ['QuadDir']
path = 'V2/TimeEvolution/'





#differences due to spin
spin = 'due_to_spinM3/'
files02 = glob.glob(root+path+spin+'e02/*.txt')
files04 = glob.glob(root+path+spin+'e04/*.txt')
files06 = glob.glob(root+path+spin+'e06/*.txt')
all_files1 = [files06,files04, files02]# , files05,files09]

#differences due to Q
spin = 'due_to_QM3/'
files02a = glob.glob(root+path+spin+'e02/*.txt')
files04a = glob.glob(root+path+spin+'e04/*.txt')
files06a = glob.glob(root+path+spin+'e06/*.txt')
all_files2 = [files06a,files04a, files02a]# , files05,files09]

def get_vector(f):

    data = np.loadtxt(f)
    
    tau = data[:,0]
    t = data[:,1]
    u0 = data[:,2]
    phi = data[:,3]

    return tau,t,u0,phi



def crop(A,B,C,D,L):
    return A[0:L], B[0:L], C[0:L], D[0:L]



def process(f1,f2,c,ax,ls):


    tau1,t1,u1,phi1 = get_vector(f1)
    tau2,t2,u2,phi2 = get_vector(f2)


    if (len(tau1) != len(tau2)):
        print ('lengths are not the same')
        minL = min(len(tau1), len(tau2))


        tau1,t1,u1,phi1 = crop(tau1,t1,u1,phi1,minL)
        tau2,t2,u2,phi2 = crop(tau2,t2,u2,phi2,minL)



    plotX = phi1 / np.pi

    if ax==ax2:
        ax1.plot(plotX,u1,c=c)
        ax1.plot(plotX,u2,c=c)
        du = (u2-u1) * 1e4
    else:
        du = (u2-u1) * 1e6



    ax.plot(plotX,du,c=c,linestyle=ls)





#due to spin
counter = 0
line='dashed'
for f in all_files1:
    C = 'C'+str(counter)
    f1 = f[0]
    f2 = f[1]
    process(f1,f2,C,ax3,line)
    counter = counter + 1



#due to Q
counter = 0
line = 'dashdot'
for f in all_files2:
    C = 'C'+str(counter)
    f1 = f[0]
    f2 = f[1]
    process(f1,f2,C,ax2,line)
    counter = counter + 1




#uncomment to get spin = 0.99, but minimal difference
#for f in all_files2:
 #   C = 'C'+str(counter)
  #  f1 = f[0]
  #  f2 = f[1]
  #  process(f1,f2,C)
  #  counter = counter + 1

#Format
#plt.style.use('science')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


fs = 20









#Number of xticks


ax1.locator_params(axis='both', nbins=5)
ax1.tick_params(axis='both', which='major', labelsize=fs-4)
ax2.locator_params(axis='both', nbins=5)
ax2.tick_params(axis='both', which='major', labelsize=fs-4)
ax3.locator_params(axis='both', nbins=5)
ax3.tick_params(axis='both', which='major', labelsize=fs-4)


plt.subplots_adjust(hspace = 0.01)
plt.setp(ax1.get_xticklabels(),visible=False)
plt.setp(ax2.get_xticklabels(),visible=False)

ax1.set_ylabel(r'$u^0$',fontsize=fs)
ax2.set_ylabel(r'$\delta_{\epsilon} \, u^0 \times 10^4$',fontsize=fs)
ax3.set_ylabel(r'$\delta_{\lambda} \, u^0 \times 10^6$',fontsize=fs)
ax3.set_xlabel(r'$ \phi / \pi$',fontsize=fs)

savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
plt.savefig(savepath+'TimeQuadrupole.png', dpi = 300,bbox='tight')


plt.show()
