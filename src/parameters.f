module parameters
implicit none


!Define float precision
integer, parameter :: dp = selected_real_kind(32,4931)


!System Parameters - these can be changed to model different sorts of orbits



!The semi-major axis of the orbit can be defined either directly, or related to the period via Keplers 3rd
real(kind=dp), parameter :: KeplerianPeriod = 0.10_dp !years
real(kind=dp), parameter :: r_set = 100.0_dp !Set the sma. Only used if KepPer eq 0

real(kind=dp), parameter :: circular = 0 !Turn on/off a precessing circular orbit. If on subsequent parameters are ignored

real(kind=dp), parameter :: eccentricity = 0.90_dp !Orbital eccentricity
real(kind=dp), parameter :: iota = 20.0_dp !Inclination w.r.t equatorial plane in degrees
real(kind=dp), parameter :: MBH = 4.310d6 !BH mass in solar masses
real(kind=dp), parameter :: MPSR = 1.40_dp !pulsar mass in solar masses
real(kind=dp), parameter :: RPSR = 10.0_dp !pulsar radius in km
real(kind=dp), parameter :: p0 = 1.0d-3 !pulsar spin period in seconds
real(kind=dp), parameter :: N_orbit = 3.0_dp !Number of orbits to integrate
!real(kind=dp), parameter :: theta_obs = PI/4.0_dp, phi_obs = 0.0_dp




!System conditions
integer(kind=dp) :: adaptive = 1 !turn on/off adaptive stepsize. On by default
integer(kind=dp), parameter :: plot = 1 !Turn on/off saving a formatted file for plotting with e.g. python
integer(kind=dp), parameter :: periastron = 0 !Turn on/off calculations for the argument of periapsis





!Effective variables
real(kind=dp) :: a !BH spin parameter
real(kind=dp) :: epsQ !Quadrupole parameter 
real(kind=dp) :: lambda  !Turn on/off spin-curvature coupling (1 = on)

end module parameters
