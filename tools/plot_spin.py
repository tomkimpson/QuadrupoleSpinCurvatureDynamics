from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os







fig = plt.figure(figsize=(10,10))
ax1 = plt.subplot2grid((1,1), (0,0))



#Load data
path = os.environ['QuadDir'] 
alldata = glob.glob(path+'*.txt')
data = np.loadtxt(alldata[0])


t = data[:,0]
x = data[:,1]
y = data[:,2]
z = data[:,3]

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
phiSL = np.arctan(Sy/Sx)

#ax1.plot(Sx, Sy)
ax1.plot(phi, thetaSL)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fs = 20

plt.show()
