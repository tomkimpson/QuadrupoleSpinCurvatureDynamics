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

def roemer(fname):
    
    data = np.loadtxt(fname)


    t = data[:,10] / (convert_s*convert_year)
    x = data[:,1] / convert_m
    y = data[:,2] / convert_m
    z = data[:,3] / convert_m
    phi = data[:,6]

    roemer = (ObsX*x + ObsY*y + ObsZ*z)/c
    r_hours = roemer/(60*60)


    ax1.plot(t,r_hours)

    return t, roemer







#geodesic option
geodesic = path+'data_lambda=0.00_epsQ=0.00.txt'
t_geo, r_geo = roemer(geodesic)






#More plot config
fs = 20
ax1.set_xlabel(r'$\tau$ [years]', fontsize=fs)
ax1.set_ylabel(r'$\Delta_R$ [hours]',fontsize=fs)
ax1.tick_params(axis='both', which='major', labelsize=fs-4)
savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
plt.savefig(savepath+'example_roemer.png', dpi = 300)

plt.show()
