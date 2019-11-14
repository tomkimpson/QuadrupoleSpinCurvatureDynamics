from os import system as os




print ('Starting compilation')


os("gfortran -ffree-form -ffree-line-length-0 -fdefault-real-8 -O3 parameters.f constants.f tensors.f derivatives.f initial_conditions.f rk.f main.f -J mod/") 

#os("gfortran -ffree-form -ffree-line-length-0 -fdefault-real-8 -O3 parameters.f constants.f QuadExpressions.f tensors.f derivatives.f initial_conditions.f rk.f main.f -J mod/") 


print ('Code has compiled. Now run it.')

os("./a.out") 
