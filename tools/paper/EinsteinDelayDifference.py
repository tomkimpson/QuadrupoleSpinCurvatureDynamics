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
ax1 = plt.subplot2grid((1,1), (0,0))


left, bottom, width, height = [0.2, 0.65, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])




plt.rc('text', usetex=True)
plt.rc('font', family='serif')


#Load data
path = os.environ['QuadDir'] 
allfiles = glob.glob(path+'PaperData/EinsteinDelay/diffs/*.txt')

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
    x = (data[:,0] / convert_s) / convert_year
    y = data[:,1] * 1e6



    ax1.plot(x,y)
    ax2.plot(x,y)

   



for f in allfiles:
    PlotEinstein(f)




fs = 20
ax1.set_xlabel(r'$\tau$ [years]', fontsize=fs)
ax1.set_ylabel(r'$\Delta dt / d \tau \times 10^6$',fontsize=fs)
ax1.tick_params(axis='both', which='major', labelsize=fs-4)


ax2.set_xlim(0.2,0.225)
plt.setp(ax2.get_xticklabels(),visible=False)
plt.setp(ax2.get_yticklabels(),visible=False)

savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
plt.savefig(savepath+'EinsteinDelayDiff.png', dpi = 300)


plt.show()
