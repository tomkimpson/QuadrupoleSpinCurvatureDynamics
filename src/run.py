from os import system as os

#os("gfortran -ffree-form -ffree-line-length-0 -fdefault-real-8 -O3 *.f -J mod/") 
os("gfortran -ffree-form -ffree-line-length-0 -fdefault-real-8 -O3 parameters.f constants.f QuadExpressions.f tensors.f initial_conditions.f derivatives.f rk.f main.f -J mod/")
os ("./a.out")

#os("gfortran -ffree-form -ffree-line-length-0 -fdefault-real-8 -O3 *.f -J mod/") 
#os("./a.out") 
