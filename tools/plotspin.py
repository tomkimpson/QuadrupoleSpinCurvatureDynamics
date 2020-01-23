from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
import os






#Plotting set up
fig = plt.figure(figsize=(10,10))
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


#Load data
path = os.environ['QuadDir'] 
allfiles = glob.glob(path+'*.txt')



#Observer location
ThetaObs = np.pi/4
PhiObs = 0

ObsX = np.sin(ThetaObs)*np.cos(PhiObs)
ObsY = np.sin(ThetaObs)*np.sin(PhiObs)
ObsZ = np.cos(ThetaObs)

#Some constants
Msolar = 1.989e30
c = 3e8
G=6.67e-11
MBH=4.31e6*Msolar
convert_m = c**2/(G*MBH)
convert_s = convert_m * c
convert_year = 365*24*3600

def spin(fname):
    
    data = np.loadtxt(fname)


    t = data[:,10] / (convert_s*convert_year)
    x = data[:,1] / convert_m
    y = data[:,2] / convert_m
    z = data[:,3] / convert_m

    r = data[:,4]
    theta = data[:,5]
    phi = data[:,6]

    s1 = data[:,7]
    s2 = data[:,8]
    s3 = data[:,9]


    #Calculate spin
    Sx = s1*np.sin(theta)*np.cos(phi) + s2*r*np.cos(theta)*np.cos(phi) - s3*r*np.sin(theta)*np.sin(phi)
    Sy = s1*np.sin(theta)*np.sin(phi) + s2*r*np.cos(theta)*np.sin(phi) + s3*r*np.sin(theta)*np.cos(phi)
    Sz = s1*np.cos(theta) - s2*r*np.sin(theta)


    thetaSL = np.arctan2(np.sqrt(Sx**2 + Sy**2),Sz)
    phiSL = np.arctan2(Sy,Sx)

    print (thetaSL[0], np.pi/4)
    


    dangle = (thetaSL - thetaSL[0]) * 180/np.pi
    dangle1 = (phiSL - phiSL[0]) * 180/np.pi

    ax2.plot(t,dangle1)
    ax1.plot(t, dangle)

    return t, thetaSL, phiSL




for f in allfiles:
    spin(f)





#More plot config
fs = 20

#AX1
ax1.locator_params(axis='both', nbins=5)
ax1.tick_params(axis='both', which='major', labelsize=fs-4)
plt.setp(ax1.get_xticklabels(),visible=False)
ax1.set_ylabel(r'$S_{\theta} [\deg]$',fontsize=fs)
#AX2



ax2.locator_params(axis='both', nbins=5)
ax2.tick_params(axis='both', which='major', labelsize=fs-4)
ax2.set_xlabel(r'$\tau$ [years]', fontsize=fs)
ax2.set_ylabel(r'$S_{\phi} [\deg]$',fontsize=fs)

plt.subplots_adjust(hspace=0.05)


savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
#plt.savefig(savepath+'spin_evolution.png', dpi = 300)

plt.show()
