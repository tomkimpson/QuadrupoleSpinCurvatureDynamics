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
fig = plt.figure(figsize=(15,10))
ax1 = plt.subplot2grid((1,1), (0,0))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


#Load data
path = os.environ['QuadDir'] 
allfiles = glob.glob(path+'*.txt')

#Some constants
Msolar = 1.989e30
c = 3e8
G=6.67e-11
MBH=4.31e6*Msolar
convert_m = c**2/(G*MBH)
convert_s = convert_m * c
convert_year = 365*24*3600

def PlotEinstein(fname):
    
    data = np.loadtxt(fname)


    tau = data[:,10] / (convert_s)
    dt = data[:,12]   
    tplot = (tau/ convert_year) #days



    ax1.plot(tplot,dt)





for f in allfiles:
    PlotEinstein(f)





fs = 20
ax1.set_xlabel(r'$\tau$ [years]', fontsize=fs)
ax1.set_ylabel(r'$dt / d \tau$',fontsize=fs)
ax1.tick_params(axis='both', which='major', labelsize=fs-4)


#savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
#plt.savefig(savepath+'spin_time_delay5.png', dpi = 300)


plt.show()
