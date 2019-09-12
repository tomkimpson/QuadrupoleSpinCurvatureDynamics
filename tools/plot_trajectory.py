from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os





d = 2


#Set up plotting environment
if (d == 3):
    fig = plt.figure(figsize=(10,10))
    ax1 = plt.subplot2grid((1,1), (0,0),projection='3d')
elif  (d == 2):
    fig = plt.figure(figsize=(20,10))
    ax1 = plt.subplot2grid((1,2), (0,0))
    ax2 = plt.subplot2grid((1,2), (0,1))



#Load data
path = os.environ['QuadDir']
files = glob.glob(path+'*.txt')


def plot(f):
    data = np.loadtxt(f)

    t = data[:,0]
    x = data[:,1]
    y = data[:,2]
    z = data[:,3]



    #Plot it


    if (d == 3):
        ax1.plot(x,y,z)
        limit = max(max(x),max(y),max(z))
        ax1.set_xlim(-limit,+limit)
        ax1.set_ylim(-limit,+limit)
        ax1.set_zlim(-limit,+limit)

    if (d == 2):
        ax1.plot(x,y)
        ax2.plot(x,z)



for f in files:
    print (f)
    plot(f)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fs = 20

plt.show()
