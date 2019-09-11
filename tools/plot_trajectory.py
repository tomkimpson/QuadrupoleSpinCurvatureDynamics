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
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
elif  (d == 2):
    fig = plt.figure(figsize=(20,10))
    ax1 = plt.subplot2grid((1,2), (0,0))
    ax2 = plt.subplot2grid((1,2), (0,1))
    ax1.scatter(0,0,c='r')


#Load data

path = os.environ['QuadDir']

alldata = glob.glob(path+'*.txt')
scatterdata = glob.glob(path+'scatter*.txt')


def scatter(datafile):

    data = np.loadtxt(datafile)
    x = data[:,0]
    y = data[:,1]
    z = data[:,2]

    if (d == 3):
        ax1.scatter(x,y,z)

    if (d == 2):
        ax1.scatter(x,y, label = datafile)




def plotter(datafile):
    print (datafile)
   
    data = np.loadtxt(datafile)
    t = data[:,0]
    x = data[:,1]
    y = data[:,2]
    z = data[:,3]
    
    
    
    #Plot it
    
    
    if (d == 3):
        ax1.plot(x,y,z)  
        ax1.scatter(x[0],y[0],z[0])  
        ax1.scatter(0,0,0, c='r')  
        limit = max(max(x),max(y),max(z))
        ax1.set_xlim(-limit,+limit)
        ax1.set_ylim(-limit,+limit)
        ax1.set_zlim(-limit,+limit)

      
        
    if (d == 2):
        ax1.plot(x,y, label = datafile)
        ax1.scatter(x[0],y[0],c='g')
        ax2.plot(x,z)
    


for datafile in alldata:
    plotter(datafile)

for datafile in scatterdata:
    scatter(datafile)


ax1.legend()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fs = 20

plt.show()
