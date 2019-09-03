module rungekutta

use parameters
use constants
use derivatives

implicit none

private calc_periastron


public rk

contains


subroutine rk(y0)

 
!Arguments
real(kind=dp),intent(IN),dimension(entries) :: y0 !initial conditions

!Other
real(kind=dp), dimension(size(y0)) :: y, y1,dy1
!an array to store all the data. !Should be faster than dynamically allocating
!However this does require more exploration
!see https://stackoverflow.com/questions/8384406/how-to-increase-array-size-on-the-fly-in-fortran
real(kind=dp), dimension(nrows,size(y0)) :: AllData !Big array to save all data
real(kind=dp), dimension(:,:),allocatable :: output !smaller array which will be outout
integer(kind=dp) :: i,j !index for saving to array
real(kind=dp) :: mm, xC, yC, zC !Cartesian components
real(kind=dp) :: dr, dr1,tau,tau1

character(len=200) :: ScatterName, astr

if (periastron .EQ. 1) then



write(astr,'(F10.2)') a
ScatterName = 'scatter_a_'//trim(adjustl(astr))
PeriastronScatter = trim(adjustl(PathOut))//trim(adjustl(ScatterName))//'.txt'
open(unit=30,file=PeriastronScatter,status='replace',form='formatted')
close(30)
endif 




y  = y0


!Save the first row to array
i = 1
AllData(i,:) = y
tau = 0.0_dp


!Get initial sign of rdot. This will be used for assessing when a periastron
!corssing has occured
call derivs(y,dy1)
dr = sign(1.0_dp,dy1(2))
  

!Integrate
!do while (y(1) .LT. 1.0_dp)
!Integrate for just a bit more than num orbits
do while ( abs( y(4) - y0(4)) .LT. 1.10_dp*N_orbit*2.0_dp*PI)    
    tau1 = tau + h
    call RKF(y,y1)
    !print *,  abs( y(4) - y0(4)),  N_orbit*2.0_dp*PI, y1(2)

    !Save the output
    i = i + 1
    AllData(i,:) = y1


    !print *, y1(2), h, dr

    !Check to see if it crossed periastron
    if (periastron .EQ. 1) then
    call calc_periastron(y1,y, &
                         tau1, tau, &
                         dr)
    endif





   !Update for next timestep
    y = y1
    tau = tau1


enddo






print *, 'Runge Kutta completed. Start data I/O'
!!!!!!!!!! - Save the output for analysis and plotting - !!!!!!!
!!!!!!!!!! - Save the output for analysis and plotting - !!!!!!!
!!!!!!!!!! - Save the output for analysis and plotting - !!!!!!!



!Binary format. See discussin at https://stackoverflow.com/questions/24395686/best-way-to-write-a-large-array-to-file-in-fortran-text-vs-other



!First reallocate to create a smaller array
allocate(output(i,entries))
output = AllData(1:i, :)

!Now save
open(unit=10,file=BinaryData,status='replace',form='unformatted')
write(10) output
close(10)




if (plot .EQ. 1) then
!Save formatted data for plotting
    PlotData = trim(adjustl(PathOut))//trim(adjustl(Fname))//'.txt'

    open(unit=20,file=PlotData,status='replace',form='formatted')
    do j = 1,i
    if (mod(real(j), coarse) .EQ. 0.0_dp) then
    mm = sqrt(output(j,2)**2 + a**2)
    xC = mm * sin(output(j,3)) * cos(output(j,4))
    yC = mm * sin(output(j,3)) * sin(output(j,4))
    zC = mm * cos(output(j,3)) 
    write(20, *) output(j,1), xC, yC, zC
    endif
    enddo
    close(20)



endif



!Closing messages
print *, 'Data saved to ', trim(adjustl(BinaryData))
print *, 'Estimated file size is: ', real(i)*real(entries)*real(dp)/1.0d6, ' MB'


end subroutine rk




subroutine calc_periastron(ynew,yold,&
                           tau1, tau, &
                           dr)
!Arguments
real(kind=dp),intent(IN),dimension(entries) :: ynew !initial conditions
real(kind=dp),intent(IN),dimension(entries) :: yold !initial conditions
real(kind=dp), intent(inout) :: dr
real(kind=dp), intent(inout) :: tau1
real(kind=dp), intent(inout) :: tau
!Other
real(kind=dp), dimension(size(ynew)) :: dy1, ytemp, yplay
real(kind=dp) :: dr1, xx,yy,zz,mm,omega
real(kind=dp) :: cc

!Get the sign of dr
call derivs(ynew,dy1)
dr1 = sign(1.0_dp,dy1(2))

yplay = yold

if (dr1 .NE. dr .and. dr1 .GT. 0.0_dp) then

    !Bisection method


    h = 1.0d-4
    do while (abs(dy1(2)) .GT. 1.0d-15)
    adaptive = 0
    call RKF(yplay, ytemp)
    call derivs(ytemp,dy1)

    if (dy1(2) .GT. 0) then
    h = h * 0.50_dp
    else
    yplay = ytemp
    endif

    enddo



!Export the omega crossing
xx = ytemp(2)*sin(ytemp(3))*cos(ytemp(4))
yy = ytemp(2)*sin(ytemp(3))*sin(ytemp(4))
zz = ytemp(2)*cos(ytemp(3))
mm = sqrt(xx**2 + yy**2 + zz**2)
omega = acos( (xx*nx + yy*ny + zz*nz) / (mm*nmag) ) !argument of periapsis





open(unit=30,file=PeriastronScatter,action='write', position='append',status='old',form='formatted')
write(30, *) xx,yy,zz
close(30)


print *, 'WRITING OMEGA', i_periapsis, omega


!print*, 'WRITING OMEGA:', omega, i_periapsis, ytemp(4), MODULO(ytemp(4), &
!2.0_dp*PI), 2.0_dp*PI - omega
!print *, 'WRITING OEMGA2:', xx,yy,zz
print *, '--------------------'


!omega_array(i_periapsis,1) = omega
!omega_array(i_periapsis,2) = ytemp(1)

omega_array(i_periapsis,1) = xx
omega_array(i_periapsis,2) = yy
omega_array(i_periapsis,3) = zz



i_periapsis = i_periapsis + 1
adaptive = 1
h = 1.0d-4


endif



dr = dr1


end subroutine calc_periastron









end module rungekutta
