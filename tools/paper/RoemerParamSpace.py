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
allfiles = glob.glob(path+'/PaperData/RoemerParameterSpace/*.txt')


def roemer(fname):
    
    data = np.loadtxt(fname)


    P = data[:,0]
    dr = data[:,1]


    ax1.plot(P,dr)

    print (P)
    print (dr)



print (allfiles)


for f in allfiles:
    roemer(f)




#More plot config
fs = 20
ax1.set_xlabel(r'P [years]', fontsize=fs)
ax1.set_ylabel(r'$\delta R [\mu s]$',fontsize=fs)
ax1.tick_params(axis='both', which='major', labelsize=fs-4)
ax1.set_yscale('log')
savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
plt.savefig(savepath+'roemer_param_space.png', dpi = 300)


plt.show()
