


f= open('../src/QuadExpressions.f', 'w')

f.write('module quadrupole_expressions \n')
f.write('use parameters \n')
f.write('use constants \n')
f.write('implicit none \n')
f.write('private \n')
f.write('public ChristoffelQuad, RiemannQuad \n')
f.write('contains \n')
f.write('\n')



#Christoffel subroutine 
f.write('subroutine ChristoffelQuad(r,theta) \n')
f.write('real(kind=dp), intent(in) :: r,theta  \n')



with open('out/Christoffel.txt', 'r') as cfile:
    lines = cfile.readlines()
    for l in lines:
        f.write(l)

f.write('\n')
f.write('end subroutine ChristoffelQuad \n')



#Riemann subroutine 


f.write('subroutine RiemannQuad(r,theta) \n')
f.write('real(kind=dp), intent(in) :: r,theta  \n')


with open('out/Riemann.txt', 'r') as cfile:
    lines = cfile.readlines()
    for l in lines:
        f.write(l)

f.write('\n')

with open('out/covariantRiemann.txt', 'r') as cfile:
    lines = cfile.readlines()
    for l in lines:
        f.write(l)


f.write('\n')


#Symmetries

f.write( 'R_0201 = R_0102 \n')


f.write( 'R_0301 = R_0103 \n')


f.write( 'R_1201 = R_0112 \n')


f.write( 'R_1301 = R_0113 \n')


f.write( 'R_2301 = R_0123 \n')


f.write( 'R_0302 = R_0203 \n')


f.write( 'R_1202 = R_0212 \n')


f.write( 'R_1302 = R_0213 \n')


f.write( 'R_2302 = R_0223 \n')


f.write( 'R_1203 = R_0312 \n')


f.write( 'R_1303 = R_0313 \n')


f.write( 'R_2303 = R_0323 \n')


f.write( 'R_1312 = R_1213  \n')


f.write( 'R_2312 = R_1223 \n')


f.write( 'R_2313 = R_1323 \n')





f.write('\n')
f.write('end subroutine RiemannQuad \n')




f.write('end module quadrupole_expressions')


f.close()


