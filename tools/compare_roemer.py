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
ax1 = plt.subplot2grid((1,1), (0,0))


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



def load(f):
    data= np.loadtxt(f)
    xaxis = data[:,ind]

    x = data[:,1]
    y = data[:,2]
    z = data[:,3]
    convert_s = data[0,10]
    dr = nx*x + ny*y + nz*z

    dr = dr - dr[0]
    dr = dr / convert_s
    
    return xaxis/convert_s, dr




def plot(f1,f2):

    x1,dr1 = load(f1)
    x2,dr2 = load(f2)


    finterp = interpolate.interp1d(x2,dr2,fill_value = 'extrapolate')
    
    dr2_new = finterp(x1)

    R = dr2_new - dr1
    R = R * 1e6 # mu s

    if ind == 0:
        x1 = (x1) / (356*24*3600) #years




    ax1.plot(x1,R)

#plot(FileA,FileB)
#plot(FileA,FileC)
plot(FileA,FileB)



fs = 20
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


ax1.set_xlabel('t [years]', fontsize=fs)
ax1.set_ylabel(r'$\delta$ R [$\mu$s]',fontsize=fs)


ax1.locator_params(axis='both', nbins=5)

ax1.tick_params(axis='both', which='major', labelsize=16)




plt.savefig(path+'RoemerAB.png', dpi=300)


plt.show()
