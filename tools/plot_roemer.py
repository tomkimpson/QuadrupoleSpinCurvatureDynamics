from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy import interpolate





fig = plt.figure(figsize=(10,10))
axA = plt.subplot2grid((1,1), (0,0))
#axB = plt.subplot2grid((2,2), (1,0))
#axC = plt.subplot2grid((2,2), (0,1))
#axD = plt.subplot2grid((2,2), (1,1))


#Load data
path = os.environ['QuadDir']



FileA = path+'A.txt'
FileB = path+'B.txt'

FileC = path+'C.txt'
FileD = path+'D.txt'







#Define what you want the x-axis to be
ind = 0 #time 4 = phi


#Define the observer location
theta_obs = np.pi/4
phi_obs = 0

nx = np.sin(theta_obs)*np.cos(phi_obs)
ny = np.sin(theta_obs)*np.sin(phi_obs)
nz = np.cos(theta_obs)

def plot(f1,ax):
    data1= np.loadtxt(f1)
    convert_s = data1[0,10]
    xaxis = data1[:,ind] 
    x = data1[:,1]
    y = data1[:,2]
    z = data1[:,3]
    dr = nx*x + ny*y + nz*z


    dr = dr- dr[0] #normalise

    if ind == 0:
        xaxis = (xaxis / convert_s) / (356*24*3600) #years


    dr = (dr/convert_s) / (3600) #hours








    ax.plot(xaxis,dr)


plot(FileA,axA)



fs = 20
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


axA.set_xlabel('t [years]', fontsize=fs)
axA.set_ylabel(r'$\Delta_{\rm R}$ [hours]',fontsize=fs)


axA.locator_params(axis='both', nbins=5)

axA.tick_params(axis='both', which='major', labelsize=16)




plt.savefig(path+'Roemer.png', dpi=300)

plt.show()
