program main



use parameters
implicit none


lambda = 0.0_dp
call run()
lambda = 1.0_dp
call run()

end program main





subroutine run()

use parameters
use constants
use IC
use rungekutta

implicit none

real(kind=dp) :: E,L, Q !Energy, AngMom, Carter
real(kind=dp), dimension(4) :: SVector, PVector !spin and momentum vectors for IC. Contravariant
real(kind=dp), dimension(entries) :: Y_init !the array of initial conditions to pass to the rk solver


h = 1.0d-1
!Setup sma, periapsis etc.
call setup()

!Calculate the initial E,L,Q from the Keplerian orbital parameters

if (circular .EQ. 1) then
r_init = r_set
call calculate_EQL_circular(E,Q,L)

else
r_init = rp
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



call rk(Y_init)

print *, 'Code completed'

end subroutine run


!end program main
