from os import system as os
import sys



print ('Starting compilation')

settings = ' -ffree-form -ffree-line-length-0 -fdefault-real-8 -O3 '


#You will obviouslyneed to compile QuadExpressions once. After that comment out for speed up


#Compile all modules
os("gfortran -J mod/ -c"+settings+"parameters.f -o mod/1.o") 
os("gfortran -J mod/ -c"+settings+"constants.f -o mod/2.o") 
#os("gfortran -J mod/ -c"+settings+"QuadExpressions.f -o mod/3.o") 
os("gfortran -J mod/ -c"+settings+"tensors.f -o mod/4.o") 
os("gfortran -J mod/ -c"+settings+"derivatives.f -o mod/5.o") 
os("gfortran -J mod/ -c"+settings+"initial_conditions.f -o mod/6.o") 
os("gfortran -J mod/ -c"+settings+"rk.f -o mod/7.o") 
os("gfortran -J mod/ -c"+settings+"main.f -o mod/8.o") 



#Link all modules
os("gfortran mod/*.o -o GO")


#Run the code
print ('Compiled. Now running the code')
os("./GO")


