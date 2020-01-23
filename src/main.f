program main



use parameters
use constants
implicit none
integer(kind=dp) :: NumRuns, i, j, k
real(kind=dp) :: roemer_difference
real(kind=dp), dimension(:,:), allocatable :: output_array
real(kind=dp) :: maxP, minP
real(kind=dp), dimension(3) :: e_array, a_array
real(kind=dp), dimension(:), allocatable :: EinsteinDifference



!Set the observer
ObsTheta = PI/4.0_dp
ObsPhi = 0.0_dp
ObsX = sin(ObsTheta)*cos(ObsPhi)
ObsY = sin(ObsTheta)*sin(ObsPhi)
ObsZ = cos(ObsTheta)



!Configure the eccentricity and spin
!eccentricity = 0.50_dp
a = 0.50_dp

!Set the stepsize - hoepfully wont need to vary this
h = 100.00_dp !stepsize






maxP = 0.10_dp
minP = 0.10_dp
NumRuns = 10
allocate(output_array(NumRuns+1, 2))


KeplerianPeriod = 0.10_dp
do i=0,NumRuns
print *, 'i = ', i
eccentricity = 0.10_dp + real(i,kind=dp) * (0.90_dp-0.10_dp)/real(NumRuns,kind=dp)
!a = 0.10_dp + real(i,kind=dp) * (0.90_dp-0.10_dp)/real(NumRuns,kind=dp)

!KeplerianPeriod = minP + real(i,kind=dp) * (maxP-minP)/real(NumRuns,kind=dp)





!h = 10.0_dp + real(i,kind=dp) !change the stepsize as the orbital period increases.
!h = 100



!Some parameters you might want to vary
!KeplerianPeriod = 0.010_dp


!Some setup calculations based on those parameters
KeplerianPeriodSeconds = KeplerianPeriod*365.0_dp*24.0_dp*3600.0_dp
SM3 =(mu*KeplerianPeriodSeconds**2.0_dp)/(4.0_dp * PI**2.0_dp)
nsteps = int(N_orbit*KeplerianPeriodSeconds*convert_s/h)

allocate(EinsteinDifference(nsteps))


call spincurvature(roemer_difference,EinsteinDifference)
print *, 'Run successful'
print *, 'Period is = ', KeplerianPeriod, i
print *, 'Periapsis passage was rp = ', rp



    open(unit=20,file=RoemerData,status='replace',form='formatted')
    do j = 1,nsteps
    write(20,*) 0.0_dp+h*real(j-1,kind=dp),EinsteinDifference(j)
    enddo
    close(20)


deallocate(EinsteinDifference)

!Save the data to array - this is for roemer delay - really need to clean all this up at some point!
!output_array(i+1,1) = KeplerianPeriod
!output_array(i+1,2) = roemer_difference


enddo


!Save to file
 !   open(unit=20,file=RoemerData,status='replace',form='formatted')
 !   do i = 0,NumRuns


 !   write(20,*) output_array(i+1,1), output_array(i+1,2)

 !   enddo
 !   close(20)



end program main


subroutine spincurvature(difference,EinsteinDifference)

use parameters
use constants

real(kind=dp), dimension(nsteps) :: roemer0, roemer1, EinsteinDifference
real(kind=dp) :: difference
integer(kind=dp) :: imax



lambda = 0.0_dp



epsQ = 0.0_dp
call run(roemer0)

epsQ = 0.10_dp
call run(roemer1)

EinsteinDifference = roemer1-roemer0


print *, 'MAX ED =', maxval(EinsteinDifference)


!--Turn this on when you want to compare with lambda =1 case

!lambda = 1.0_dp
!call run(roemer1)
!difference =  maxval(roemer0-roemer1) * 1e6
!imax = maxloc(roemer0-roemer1,1)
!print *, 'RESULTS = ',difference, roemer0(imax), roemer1(imax)

end subroutine spincurvature



subroutine run(roemer_array)

use parameters
use constants
use IC
use rungekutta

implicit none

real(kind=dp) :: E,L, Q !Energy, AngMom, Carter
real(kind=dp), dimension(4) :: SVector, PVector !spin and momentum vectors for IC. Contravariant
real(kind=dp), dimension(entries) :: Y_init !the array of initial conditions to pass to the rk solver
real(kind=dp), dimension(nsteps) :: roemer_array





!Setup sma, periapsis etc.
call setup()

!Calculate the initial E,L,Q from the Keplerian orbital parameters

if (circular .EQ. 1) then
r_init = r_set
call calculate_EQL_circular(E,Q,L)

else
r_init = (rp+ra)/2.0_dp
!r_init = ra !r_init/2.0_dp
!1.10_dp*rp !Changed this to examine close to periapsis
call calculate_EQL(E,Q,L)
endif






!print *, E,Q,L
!stop


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


!print *, Y_init(1:4)
!print *, Y_init(5:8)
!print *, Y_init(9:12)






call rk(Y_init,roemer_array)


end subroutine run


!end program main
