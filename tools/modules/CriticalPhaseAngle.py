from __future__ import division 
from numpy import sin as Sin 
from numpy import cos as Cos 
from numpy import arccos as ArcCos 
from numpy import sqrt as Sqrt 
#This expression was evaluated using PSI =  Pi/4.  
                                                  
#Additionally, the observer is taken to be at =  List(1/Sqrt(2),0,1/Sqrt(2))  
                                                                             
def CalculateChi(stheta, sphi): 
    top = (-(Cos(sphi)*Cos(stheta)) + Sin(stheta))
    bot = Sqrt(Cos(sphi)**2*Cos(stheta)**2 + Sin(sphi)**2 + Sin(stheta)**2 - Cos(sphi)*Sin(2*stheta))
    



    output = -ArcCos(-top/bot)
  #  output =  (-ArcCos((-(Cos(sphi)*Cos(stheta)) + Sin(stheta))/Sqrt(Cos(sphi)**2*Cos(stheta)**2 + Sin(sphi)**2 + Sin(stheta)**2 - Cos(sphi)*Sin(2*stheta))))
    
    return -top,bot
