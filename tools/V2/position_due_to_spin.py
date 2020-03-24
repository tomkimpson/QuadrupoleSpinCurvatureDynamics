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





#Setup plotting environment

plt.style.use('science')
fig, ax1 = plt.subplots(1, 1, figsize=(10,10))


#What BH mass do you want?
M = 6 #M=3







MBH=1.00e3*Msolar




if M == 6:
    MBH = 4.31e6 * Msolar
    dir = 'M6/'
if M == 3:
    MBH == 1.00e3 * Msolar
    dir = 'M3/'



convert_m = c**2/(G*MBH)
convert_s = convert_m * c
convert_year = 365*24*3600
convert_m = convert_m * 1e3

#Set path to files

root = os.environ['QuadDir']
path = 'V2/SpatialLambda/'+dir


files02 = glob.glob(root+path+'e02/*.txt')
files04 = glob.glob(root+path+'e04/*.txt')
files06 = glob.glob(root+path+'e06/*.txt')


all_files = [files06,files04, files02]# , files05,files09]





def get_vector(f):

    data = np.loadtxt(f)
    tau = data[:,12]

    x = data[:,1]
    y = data[:,2]
    z = data[:,3]

    phi = data[:,6]

    return tau,x,y,z,phi



def crop(A,B,C,D,E,L):
    return A[0:L], B[0:L], C[0:L], D[0:L], E[0:L]



def process(f1,f2,c):


    tau1,x1,y1,z1,phi1 = get_vector(f1)
    tau2,x2,y2,z2,phi2 = get_vector(f2)


    if (len(tau1) != len(tau2)):
        print ('lengths are not the same')
        minL = min(len(tau1), len(tau2))


        tau1,x1,y1,z1,phi1 = crop(tau1,x1,y1,z1,phi1,minL)
        tau2,x2,y2,z2,phi2 = crop(tau2,x2,y2,z2,phi2,minL)



    dx = x2-x1
    dy = y2-y1
    dz = z2-z1




    #Convert to m 

    dx = dx / convert_m
    dy = dy / convert_m
    dz = dz / convert_m

    plotX = phi1 / np.pi


    ds2 =  dz**2 + dy**2 + dx**2



    ax1.plot(plotX,dx,linestyle='solid',c=c)
    ax1.plot(plotX,dy,linestyle='dotted',c=c)
    ax1.plot(plotX,dz,linestyle='dashed',c=c)

 #   ax1.plot(plotX,np.sqrt(ds2))
 #   ax3.plot(plotX,dz)

counter = 0
for f in all_files:
    C = 'C'+str(counter)
    f1 = f[0]
    f2 = f[1]
    process(f1,f2,C)

    counter = counter + 1

#Format
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fs = 20



#Number of xticks
ax1.locator_params(axis='both', nbins=5)
ax1.tick_params(axis='both', which='major', labelsize=fs-4)


ax1.set_ylabel(r'$\delta_{\lambda}$ [km]',fontsize=fs)
ax1.set_xlabel(r'$\phi / \pi$',fontsize=fs)


savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
plt.savefig(savepath+'OrbitalSpin'+str(M)+'.png', dpi = 300,bbox='tight')

plt.show()
