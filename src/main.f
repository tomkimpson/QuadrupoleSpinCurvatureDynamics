program main

use parameters  
use constants

implicit none
integer(kind=dp) :: i
integer(kind=dp) :: num_a !Number of spin entries
character(len=200) :: Qstr, LAMstr, periname
num_a = 10


epsQ = 0.10_dp
lambda=1.0_dp

write(Qstr,'(F10.2)') epsQ
write(LAMstr,'(F10.2)') lambda

call get_environment_variable("QuadDir", PathOut)
periname = 'periastron_Q='//trim(adjustl(Qstr))// &
         '_L='//trim(adjustl(LAMstr))
                                          
print *, trim(adjustl(periname))
print *, trim(adjustl(PathOut))
PeriastronData = trim(adjustl(PathOut))//trim(adjustl(periname))//'.txt'
print *, PeriastronData


open(unit=30,file=PeriastronData,status='replace',form='formatted')
close(30)





do i = 1,num_a
a = real(0.1_dp*i, kind=dp)
if (a.eq.1.0_dp) then
a = 0.9980_dp !Set maximum possible spin
endif

call main_run()
enddo

print *, 'All completed OK. EXIT'


end program main




subroutine main_run()

use parameters
use constants
use IC
use rungekutta




implicit none
real(kind=dp) :: E,L, Q !Energy, AngMom, Carter
real(kind=dp), dimension(4) :: SVector, PVector !spin and momentum vectors for IC. Contravariant
real(kind=dp), dimension(entries) :: Y_init !the array of initial conditions to pass to the rk solver
character(len=20) :: Astr, Qstr, LAMstr
integer(kind=dp) :: i
real(kind=dp) :: domega, dt, x1,x2,y1,y2,z1,z2, e1,e2
!Setup sma, periapsis etc.
call setup()


!Declare savefiles
write(Astr,'(F10.2)') a
write(Qstr,'(F10.2)') epsQ
write(LAMstr,'(F10.2)') lambda

Fname = 'data_a='//trim(adjustl(Astr))// &
         '_Q='//trim(adjustl(Qstr))// &
         '_L='//trim(adjustl(LAMstr))
                                          

BinaryData = trim(adjustl(PathOut))//trim(adjustl(Fname))//'.dat'

print *, BinaryData

!Calculate the initial E,L,Q from the Keplerian orbital parameters

if (circular .EQ. 1) then
r_init = r_set
call calculate_EQL_circular(E,Q,L)

else
r_init = r_set
call calculate_EQL(E,Q,L)
endif

!Set the spatial components of the spin-vector in the coordinate basis
!This transformation is done locally - in the neighbourhood is it Minkowskian.
!See https://physics.stackexchange.com/questions/370027/non-coordinate-basis-in-gr?rq=1
SVector(2) = s0 * sin(stheta) * cos(sphi) !S1
SVector(3) = -s0 *cos(stheta)/r_init !S2 
SVector(4) = s0*sin(stheta)*sin(sphi)/(r_init*sin(theta_init)) !S3





!Calculate the remaining initial conditions

call calculate_IC(E,L,Q, SVector,PVector)



!Now do the numerical integration using a runge-kutta

Y_init(1) = t_init
Y_init(2) = r_init
Y_init(3) = theta_init
Y_init(4) = phi_init

Y_init(5:8) = PVector
Y_init(9:12) = SVector



!Calculate the vector which points towards the ascending node
!By constrution, the initial spatial position is at the point of the ascending
!node


!Periapsis setup

nx = r_init*sin(theta_init)*cos(phi_init)
ny = r_init*sin(theta_init)*sin(phi_init)
nz = r_init*cos(theta_init)
nmag = sqrt(nx**2 + ny**2 + nz**2)

omega_array = 0.0_dp
i_periapsis = 1


print *, 'Going in. N = ', nx,ny,nz

call rk(Y_init)

print *, '-----------------------'
print *, 'Completed rk solver'
print *, '-----------------------'




do i = 1,int(N_orbit)
print *, omega_array(i,:)
enddo
print *, '-----------------------'

!do i = 1,int(N_orbit-1)
!print *, omega_array(i+1,1), omega_array(i,1),(omega_array(i+1,1) - omega_array(i,1) ) / (omega_array(i+1,2) - omega_array(i,2) ) 
!enddo



x1 = omega_array(1,1)
y1 = omega_array(1,2)
z1 = omega_array(1,3)
e1 = sqrt(x1**2 + y1**2 + z1**2)

x2 = omega_array(2,1)
y2 = omega_array(2,2)
z2 = omega_array(2,3)
e2 = sqrt(x2**2 + y2**2 + z2**2)


domega = acos( (x1*x2 + y1*y2 + z1*z2)/(e1*e2))


!domega = omega_array(int(N_orbit),1) - omega_array(int(N_orbit-1),1)
!dt     = omega_array(int(N_orbit),2) - omega_array(int(N_orbit-1),2)


print *, 'OUT', a, domega



open(unit=30,file=PeriastronData,action='write', position='append',status='old',form='formatted')
write(30, *) domega, a,dt
close(30)


end subroutine main_run








