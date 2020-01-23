from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
import os







fig = plt.figure(figsize=(10,10))
ax1 = plt.subplot2grid((3,1), (0,0))
ax2 = plt.subplot2grid((3,1), (1,0),sharex=ax1)
ax3 = plt.subplot2grid((3,1), (2,0),sharex=ax1)



#Load data
path = os.environ['QuadDir'] 
allfiles = glob.glob(path+'*.txt')



#Observer location
ThetaObs = np.pi/4
PhiObs = 0

ObsX = np.sin(ThetaObs)*np.cos(PhiObs)
ObsY = np.sin(ThetaObs)*np.sin(PhiObs)
ObsZ = np.cos(ThetaObs)


Msolar = 1.989e30
c = 3e8
G=6.67e-11
MBH=4.31e6*Msolar
convert_m = c**2/(G*MBH)
convert_s = convert_m * c
convert_year = 365*24*3600

print (ObsX, ObsY, ObsZ)

def roemer(fname):
    
    data = np.loadtxt(fname)


    t = data[:,10] / (convert_s*convert_year)
    x = data[:,1] / convert_m
    y = data[:,2] / convert_m
    z = data[:,3] / convert_m
    phi = data[:,6]

    roemer = (ObsX*x + ObsY*y + ObsZ*z)/c

    ax1.plot(t,roemer)

    return t, roemer







#geodesic option
geodesic = path+'data_lambda=0.00_epsQ=0.00.txt'
t_geo, r_geo = roemer(geodesic)


#lambda on, eps off
geodesic1 = path+'data_lambda=1.00_epsQ=0.00.txt'
t1, r1 = roemer(geodesic1)
dr1 = r_geo - r1


#lambda off, eps on
geodesic2 = path+'data_lambda=0.00_epsQ=0.10.txt'
t2, r2 = roemer(geodesic2)
dr2 = r_geo - r2


#lambda on, eps, on
geodesic3 = path+'data_lambda=1.00_epsQ=0.10.txt'
t3, r3 = roemer(geodesic3)
dr3 = r_geo - r3



ax2.plot(t1,dr1,label ='dr1')
ax2.plot(t1,dr2,label='dr2')
ax2.plot(t1,dr3, label='dr3')



diff1 = (dr3 - dr2) * 1e6
ax3.plot(t1,diff1)

#dAC = dr3 - dr1
#dAB = dr2 - dr1
#dBC = dr2 - dr3
#ax3.plot(t1,dAC,label='dAC')
#ax3.plot(t1,dAB,label='dAB')
#ax3.plot(t1,dBC,label='dBC')


#ax1.set_xlim(6.36,6.46)
#ax2.set_ylim(-4e-8,-1e-8)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fs = 20
ax1.set_xlabel(r'$\tau$ [years]')
ax1.set_ylabel(r'$\Delta_R$ [s]')
ax2.set_ylabel(r'$R$ [s]')
ax3.set_ylabel(r'$\delta [ \mu s]$')


plt.show()
