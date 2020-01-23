module rungekutta

use parameters
use constants
use derivatives

implicit none

private


public rk

contains


subroutine rk(y0,roemer_array)

 
!Arguments
real(kind=dp),intent(IN),dimension(entries) :: y0 !initial conditions
real(kind=dp),intent(OUT),dimension(nsteps) :: roemer_array !initial conditions

!Other
real(kind=dp), dimension(size(y0)) :: y, y1,dy
!an array to store all the data. !Should be faster than dynamically allocating
!However this does require more exploration
!see https://stackoverflow.com/questions/8384406/how-to-increase-array-size-on-the-fly-in-fortran
real(kind=dp), dimension(nrows,size(y0)+2) :: AllData !Big array to save all data. 12 coordinates + tau + dt/dtau
real(kind=dp), dimension(:,:),allocatable :: output !smaller array which will be outout
integer(kind=dp) :: i,j !,nsteps !index for saving to array
real(kind=dp) :: mm, xC, yC, zC !Cartesian components
real(kind=dp), dimension(:), allocatable :: r,theta,phi,S1,S2,S3,Sx,Sy,Sz, thetaSL, phiSL
real(kind=dp) :: tau, roemer


y  = y0


!Save the first row to array
i = 1
AllData(i,1:12) = y
AllData(i,13) = tau
 

call derivs(y,dy)
AllData(i,14) = dy(1)






!Integrate
!
!do while (i .LT. 5)
!do while ( abs( y(4) - y0(4)) .LT. N_orbit*2.0_dp*PI)    
!print *, abs( y(4) - y0(4)) , N_orbit*2.0_dp*PI

do while (tau .LT. N_orbit*KeplerianPeriodSeconds*convert_s)
!do while (i .LT. nsteps)
!do while (y(2) .LT. 1.010_dp*r_init)

    call RKF(y,y1)
    y = y1
    
    !Save the output
    i = i + 1
    AllData(i,1:12) = y
    tau = tau + h
    AllData(i,13) = tau

    !And calculate some derivative info - probably not the most effective way to do this

    call derivs(y,dy)
    AllData(i,14) = dy(1)

 !   print *, y


enddo






print *, 'Runge Kutta completed. Start data I/O'
!!!!!!!!!! - Save the output for analysis and plotting - !!!!!!!
!!!!!!!!!! - Save the output for analysis and plotting - !!!!!!!
!!!!!!!!!! - Save the output for analysis and plotting - !!!!!!!



!Binary format. See discussion at https://stackoverflow.com/questions/24395686/best-way-to-write-a-large-array-to-file-in-fortran-text-vs-other



!First reallocate to create a smaller array
allocate(output(i,entries))
output = AllData(1:i, :)

!Now save
!open(unit=10,file=BinaryData,status='replace',form='unformatted')
!write(10) output
!close(10)




print *, 'Nsteps = ', i, int(N_orbit*KeplerianPeriodSeconds*convert_s/h), h





if (plot .EQ. 1) then
!Save formatted data for plotting
    open(unit=20,file=PlotData,status='replace',form='formatted')
    do j = 1,i
    if (mod(real(j), coarse) .EQ. 0.0_dp) then
    mm = sqrt(output(j,2)**2 + a**2)
    xC = mm * sin(output(j,3)) * cos(output(j,4))
    yC = mm * sin(output(j,3)) * sin(output(j,4))
    zC = mm * cos(output(j,3)) 
    

    !Calculate the Roemer delay

    !roemer = (ObsX*xC + ObsY*yC + ObsZ*zC) / convert_s   
    !roemer_array(j) = roemer

    !Repurposing roemer to be Einstein delay

    roemer_array(j) = output(j,14)




    write(20, *) output(j,1), xC, yC, zC , & !t,x,y,z
                 output(j,2), output(j,3), output(j,4), & !r,theta,phi 
                 output(j,10),output(j,11),output(j,12), & !s1,s2,s3
                 output(j,13),roemer,output(j,14) !tau, roemer,dt,dtau
    endif 
    enddo
    close(20)



endif



!Closing messages
!print *, 'Data saved to ', trim(adjustl(BinaryData))
!print *, 'Estimated file size is: ', real(i)*real(entries)*real(dp)/1.0d6, ' MB'


end subroutine rk


end module rungekutta
