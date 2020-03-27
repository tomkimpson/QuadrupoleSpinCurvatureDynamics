from __future__ import division 
from numpy import sin as Sin 
from numpy import cos as Cos 
from numpy import arccos as ArcCos 
from numpy import sqrt as Sqrt 
#This expression was evaluated using PSI =  Pi/4.  
                                                  
#Additionally, the observer is taken to be at =  List(1/Sqrt(2),0,1/Sqrt(2))  
                                                                             
def CalculateChi(stheta, sphi): 
    output =  ArcCos((Cos(sphi)*Cos(stheta) - Sin(stheta))/Sqrt(Cos(sphi)**2*Cos(stheta)**2 + Sin(sphi)**2 - 2*Cos(sphi)*Cos(stheta)*Sin(stheta) + Sin(stheta)**2))
    return output