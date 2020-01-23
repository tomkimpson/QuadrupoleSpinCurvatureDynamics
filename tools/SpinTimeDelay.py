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
fig = plt.figure(figsize=(15,10))
ax1 = plt.subplot2grid((2,3), (0,0), rowspan=2,colspan=2)
ax2 = plt.subplot2grid((2,3), (0,2))
ax3 = plt.subplot2grid((2,3), (1,2))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


#Load data
path = os.environ['QuadDir'] 
allfiles = glob.glob(path+'*.txt')



#Observer location
ThetaObs = np.pi/4
PhiObs = 0

ObsX = np.sin(ThetaObs)*np.cos(PhiObs)
ObsY = np.sin(ThetaObs)*np.sin(PhiObs)
ObsZ = np.cos(ThetaObs)

#Some constants
Msolar = 1.989e30
c = 3e8
G=6.67e-11
MBH=4.31e6*Msolar
convert_m = c**2/(G*MBH)
convert_s = convert_m * c
convert_year = 365*24*3600

def GetSpinAngles(fname,counts):
    
    data = np.loadtxt(fname)


    t = data[:,10] / (convert_s)
    
    tplot = (t / convert_year) *365 #days
    x = data[:,1] #/ convert_m
    y = data[:,2] #/ convert_m
    z = data[:,3] #/ convert_m

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


    stheta = np.arctan2(np.sqrt(Sx**2 + Sy**2),Sz)
    sphi = np.arctan2(Sy,Sx)




   # stheta = np.zeros(len(stheta))
   # sphi = np.zeros(len(sphi))

    #Set beam oreintation w.r.t spin axis
    psi = np.pi/4
    P = 1e-3 #pulsar spin period
    #chi = t/P * 2*np.pi

 
    ax1.axhline(0,linestyle='--', c='0.5')



    box = -ObsX*np.cos(sphi)*np.cos(stheta)*np.sin(psi) -ObsY*np.sin(sphi)*np.cos(stheta)*np.sin(psi) - ObsZ*np.sin(stheta)*np.cos(psi)


    RHS = np.sin(psi)*(ObsX*np.sin(sphi) - ObsY*np.cos(sphi))/box

    chi = np.arctan(RHS)


    #Plot the trajectory
    if counts == 0:
        idx = np.argmin(r)
        ax2.plot(x,y,zorder=1)
        ax2.scatter(x[0], y[0], c='g',marker='.',zorder=2)
        ax2.scatter(x[-1], y[-1], c='r',marker='.',zorder=2)




        print ('Periapsis was', min(r))

        #ax1.axvline(tplot[idx],c='C1',linestyle='--')

        perix = [0,x[idx]]
        periy = [0,y[idx]]
        periz = [0,z[idx]]
        ax2.plot(perix,periy,periz,c='C1',zorder=1)


        ax2.scatter(0,0,c='k',zorder=2)

        ax2.scatter(x[idx],y[idx], c='C1',zorder=2,marker='.')


    ax3.plot(tplot,chi-chi[0],c='C2')



    frac = (chi - chi[0]) / (2*np.pi) #fraction by which pulse frequency changes
 

    frac = abs(frac*100)





#    ax1.plot(tplot,frac)


    print (fname, max(frac))


    return tplot, chi,phi



xx = []
yy = []
zz = []
counts = 0
for f in allfiles:
    x,y,z = GetSpinAngles(f,counts)


    xx.extend([x])
    yy.extend([y])
    zz.extend([z])

    counts = counts + 1


x = xx[1]
y = yy[1] - yy[0]


y = y/(2*np.pi) * 1e6



ax1.plot(x,y)
#ax3.plot(z,y)

fs = 20
ax1.set_xlabel(r'$\tau$ [days]', fontsize=fs)
ax1.set_ylabel(r'$\delta_t / P \times 10^6$',fontsize=fs)
ax1.tick_params(axis='both', which='major', labelsize=fs-4)


ax2.axis('equal')
plt.setp(ax2.get_xticklabels(),visible=False)
plt.setp(ax2.get_yticklabels(),visible=False)

ax3.locator_params(axis='both', nbins=3)
ax3.set_xlabel(r'$\tau$ [days]', fontsize=fs)


#savepath = '/Users/tomkimpson/Dropbox/MSSL/Papers/PaperNQuadrupole/figures/'
#plt.savefig(savepath+'spin_time_delay5.png', dpi = 300)


plt.show()
