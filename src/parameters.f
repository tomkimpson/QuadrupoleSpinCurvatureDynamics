module parameters
implicit none


!Define float precision
integer, parameter :: dp = selected_real_kind(33,4931)



!The semi-major axis of the orbit can be defined either directly, or related to the period via Keplers 3rd


!Orbital parameters

real(kind=dp), parameter :: circular = 0 !Turn on/off a circular orbit. If on subsequent orbital parameters are ignored and the
!orbital radius is given by r_set



real(kind=dp), parameter :: KeplerianPeriod = 0.10_dp
real(kind=dp), parameter :: r_set = 20.0_dp !Set the sma. Only used if KepPer eq 0
real(kind=dp), parameter :: eccentricity = 0.90_dp !Orbital eccentricity
real(kind=dp), parameter :: iota = 00.0_dp !Inclination w.r.t equatorial plane in degrees
real(kind=dp), parameter :: N_orbit = 3.0_dp !Number of orbits to integrate


!BH intrinsic parameters
real(kind=dp), parameter :: MBH = 4.310d6 !BH mass in solar masses
real(kind=dp), parameter :: a=0.50_dp !BH spin parameter
real(kind=dp), parameter :: epsQ = 0.0_dp !BH quadrupole moment

!PSR intrinsic parameters
real(kind=dp), parameter :: MPSR = 1.40_dp !pulsar mass in solar masses
real(kind=dp), parameter :: RPSR = 10.0_dp !pulsar radius in km
real(kind=dp), parameter :: p0 = 1.0d-3 !pulsar spin period in seconds



!Format parameters
integer(kind=dp), parameter :: plot = 1 !Turn on/off saving a formatted file for plotting with e.g. python



!Globals to be set later
real(kind=dp) :: lambda !Turn on/off spin-curvature coupling (1 = on)

end module parameters
