from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy.signal import argrelextrema
from numpy import cos as Cos
from numpy import sin as Sin
from numpy import sqrt as Sqrt


#Setup plotting environment
plt.style.use('science')
fig, ax1 =plt.subplots(1, 1, sharex=True, figsize=(10,10))


#Observer location
ObsTheta = np.pi/4.0
ObsPhi = 0.0
ObsX = np.sin(ObsTheta)*np.cos(ObsPhi)
ObsY = np.sin(ObsTheta)*np.sin(ObsPhi)
ObsZ = np.cos(ObsTheta)




stheta = 0.0
sphi = 0.0
psi = np.pi/4
chi = np.linspace(-2*np.pi,2*np.pi,100)
omega = np.arccos((Cos(stheta) + Cos(sphi)*Cos(stheta)*Cos(chi) + Cos(sphi)*Sin(stheta) - Cos(chi)*Sin(stheta) - Sin(sphi)*Sin(chi))/2.)



#ax1.plot(chi,omega)
#plt.show()
#sys.exit()


#define the critical angle function
def CriticalPhase(Ox,Oy,Oz,stheta,sphi):

    bottom = Cos(sphi)**2 * Cos(stheta)**2 + Sin(sphi)**2 -2*Cos(sphi)*Cos(stheta)*Sin(stheta) + Sin(stheta)**2

    top = Cos(sphi)*Cos(stheta) + Sin(stheta)

    return np.arccos(top/bottom)















root = os.environ['QuadDir']
path = 'V2/SpinEvolution/'
#path = 'V2/SpinEvolution/M6/'
spin = 'a+06/'
def get_data(f):

    data = np.loadtxt(f)
    
    tau = data[:,0]
    phi = data[:,1]
    stheta = data[:,2]
    sphi = data[:,3]

    stheta = stheta * 0.0
    sphi = sphi * 0.0


    Xc = CriticalPhase(ObsX,ObsY,ObsZ,stheta,sphi)
 
    print (Xc[0], np.pi/4, 1/np.sqrt(2))
    sys.exit()

   
    delta_Xc = Xc-Xc[0]
    Ps = 1 #milliseconds
    delta_t = Ps *delta_Xc / (2*np.pi)


    ax1.plot(tau,Xc)





def crop(A,B,L):
    return A[0:L], B[0:L]

def ToPlot(f1):

    get_data(f1)



#e02
eStrings = ['e06/', 'e04/', 'e02/']
for e in eStrings:
    FileA = root+path+spin+e+'A.txt'
    FileB = root+path+spin+e+'B.txt'
    FileC = root+path+spin+e+'C.txt'
    
    ToPlot(FileA)
    ToPlot(FileB)
    ToPlot(FileC)

#Format
fs = 20



all_axes = plt.gcf().get_axes()
for ax in all_axes:
    ax.locator_params(axis='both', nbins=5) #set number of xticks
    ax.tick_params(axis='both', which='major', labelsize=fs-4) #set size of numbers
    


savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
#plt.savefig(savepath+'Spin'+str(idx)+'.png', dpi = 300,bbox='tight')
plt.show()

