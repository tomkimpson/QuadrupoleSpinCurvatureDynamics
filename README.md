# Spin Curvature Dynamics of a Pulsar in Kerr Spacetime with an arbitrary mass quadrupole

This code calculates the orbital motion of an astrophysical body, such as a pulsar, on a background Kerr spacetime with an arbitrary mass quadrupole. It is based on the [SpinCurvatureDynamics Code](https://github.com/tomkimpson/SpinCurvatureDynamics) for a Kerr spacetime, and the quasi-Kerr metric of [Glampedakis & Babak](https://arxiv.org/abs/gr-qc/0510057). Going beyond the point particle approximation, we instead model an extended spinning body via the Mathisson-Papertrou-Dixon equations.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

This code is written in FORTRAN with a [gfortran](https://gcc.gnu.org/wiki/GFortran) compiler. **Other compilers have not been tested.** The gfortran installation binaries can be found [here](https://gcc.gnu.org/wiki/GFortranBinariels), although typically gfortran comes pre-installed on most Linux/Unix systems. If you have [Homebew](https://brew.sh/) installed on OSX, you can simply run 


```
brew install gcc
```



### Starting steps

After [cloning the repo](https://help.github.com/en/articles/cloning-a-repository), the first thing to do is to set the path to the output files that the code will produce.
This can be done by setting the environment variable as

```
echo 'export QuadDir="/Users/tomkimpson/Data/Quadrupole/"' >> ~/.bash_profile
source ~/.bash_profile
```

Just change the path `Users/tomkimpson/Data/Quadrupole/` to some appropriate local path. 

You can check the environemnt variable has been added to `bash_profile` by either `env` or `vim ~/.bashprofile`


The code should then run as is, out of the box. Try

```
run.py
```

to compile and run the code. Once you have checked that everything is running OK, you can then start playing. The code structure (mdoules, subroutines etc.) is outlined below.


If making edits to the code, try to keep to the [FORTRAN Style Guide](https://www.fortran90.org/src/best-practices.html)

### Structure

* `Mathematica/` contains the code used for constructing the Christoffel/Riemann tensors for the metric



**WORK TO THIS REPO IS ONGOING AND SHOULD NOT CURRENTLY BE USED FOR PURPOSE**


