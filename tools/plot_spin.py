from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy import interpolate





fig = plt.figure(figsize=(20,10))
ax1 = plt.subplot2grid((1,2), (0,0))
ax2 = plt.subplot2grid((1,2), (0,1))


#Load data
path = os.environ['QuadDir']



FileA = path+'A.txt'
FileB = path+'B.txt'

FileC = path+'C.txt'
FileD = path+'D.txt'


#Define what you want the x-axis to be
ind = 0 #time 4 = phi



def compare(f1,f2,lab):
    data1= np.loadtxt(f1)
    xx = data1[:,ind]
    stheta = data1[:,5]
    sphi = data1[:,6]


    data2= np.loadtxt(f2)
    xx2 = data2[:,ind]
    stheta1 = data2[:,5]
    sphi1 = data2[:,6]


   
    ftheta = interpolate.interp1d(xx2,stheta1,fill_value = 'extrapolate')
    fphi = interpolate.interp1d(xx2,sphi1,fill_value = 'extrapolate')
    
    stheta_new = ftheta(xx)
    sphi_new = fphi(xx)

    dstheta = stheta_new-stheta
    dsphi = sphi_new-sphi

    ax1.plot(xx,stheta,label=lab)
    ax2.plot(xx,sphi,label=lab)


compare(FileA, FileB,'geo')
#compare(FileC, FileD, 'quad')




ax2.legend()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fs = 20

plt.show()
