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
ax1 = plt.subplot2grid((1,1), (0,0))


#Load data
path = os.environ['QuadDir']
files = glob.glob(path+'*.txt')



def plot(f1):
    data1= np.loadtxt(f1)
    Sx = data1[:,7]
    Sy = data1[:,8]
    Sz = data1[:,9]

    Sx = Sx/Sx[0]
    Sy = Sy/Sy[0]
 

    ax1.plot(Sx,Sy)




for f in files:
    plot(f)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fs = 20

plt.show()
