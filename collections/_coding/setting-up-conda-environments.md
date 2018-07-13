---
title: Conda environments for NCO, NCL, and CDO
date: 2018-07-10
order: 1
---

> *Disclaimer:  This assumes knowledge of a conda-based Python installation (e.g., [Anaconda or Miniconda](https://conda.io/docs/index.html)).  I'll add more info on what these are in another post.*

Environments in conda are incredibly useful:  they allow you to install parallel versions of Python and its packages, or even other languages and software, that mind their own business and never affect one another.

In my own research, I actively use several different conda environments to keep everything in its place.  To see what environments you currently have, type ```conda env list```.  You'll have at least one, called the base environment, and the asterisk means it's the current/active environment:

```
conda env list

# conda environments:
#
base                  *  /Users/baird/miniconda3

vcv076219:python-for-climate-scientists baird$
```

Installing an environment is also a great way to make the switch to a new Python library or package without breaking your installation for all your current scripts.  For example, if you use [basemap][basemap-link] for plotting maps, you may have heard it's [being retired][basemap-sunset] in the next couple years (see also [this discussion][basemap-sunset-forum]).  Its replacement is officially [cartopy][cartopy-link], but when you try to install them both, their packages conflict (or at least they did in the past).  **The solution:  Install a separate cartopy environment to get used to it, and once you feel confident, change your base environment to cartopy and create a ```basemap_stable``` environment for basemap-specific tasks.**

I typically keep at least four separate environments (in addition to the default), described below.  You could get away with putting things like NCO and NCL into your base environment, but I've run into compatibility issues in the past, and I keep them separate to be safe.

|conda environment  |use for      |install commands
|---                |---          |---
|**base**           |most things  |---
|**nco_stable**     |NCO (NetCDF Operators) | conda install -c conda-forge nco
|**ncl_stable**     |NCL (NCAR Command Language) | conda install -c conda-forge ncl
|**cdo_stable**     |CDO (Climate Data Operators) | conda install -c conda-forge cdo
|**basemap_stable** |basmap (assuming you have cartopy in your base environment)  | conda install basemap

To create these environments yourself (base is the default), type the following (choose ```y``` after each).  I like to use the ```_stable``` suffix because it helps me mentally separate an *environment* related to NCO from the language itself.  You can name them anything you like, though.

```
conda create --name nco_stable
```

Once the environment is created, activate it by typing:

```
source activate nco_stable
```

And from here, you can install the package you want within it.  For NCO, that will simply be:
```
conda install -c conda-forge nco
```

Note the ```-c``` in ```-c conda-forge``` means "channel."  What this does is tells conda to look in the "conda-forge" channel (which hosts a broader range of user-created packages).  To see what channels were used to install your conda packages, type ```conda list```.  This conveniently lists the packages installed in the current environment, their version and build information, and the channel used to install them.  For packages with nothing under the "Channel" column, they were installed using the defaults channel.  For NCO and other fairly specific software packages, conda will typically need the conda-forge channel.

```
baird$ conda list
# packages in environment at /Users/baird/miniconda3/envs/nco_stable:
#
# Name                    Version                   Build  Channel
ca-certificates           2018.4.16                     0    conda-forge
curl                      7.60.0               h93b3f91_0    conda-forge
esmf                      7.1.0r                        1    conda-forge
expat                     2.2.5                hfc679d8_1    conda-forge
gsl                       2.2.1                h002c638_3
hdf4                      4.2.13                        0    conda-forge
hdf5                      1.10.1                        2    conda-forge
jpeg                      9c                   h470a237_0    conda-forge
krb5                      1.14.6                        0    conda-forge
libgcc                    4.8.5               hdbeacc1_10
libgfortran               3.0.1                h93005f0_2
libnetcdf                 4.6.1                         2    conda-forge
libssh2                   1.8.0                h5b517e9_2    conda-forge
mpi                       1.0                       mpich    conda-forge
mpich                     3.2.1                h26a2512_4    conda-forge
nco                       4.7.5                         1    conda-forge
netcdf-fortran            4.4.4                         7    conda-forge
openblas                  0.2.20                        8    conda-forge
openssl                   1.0.2o                        0    conda-forge
udunits2                  2.2.26                        1    conda-forge
zlib                      1.2.11               h470a237_3    conda-forge
```

More about Anaconda/Miniconda channels [here](https://conda.io/docs/user-guide/tasks/manage-channels.html).

* To activate an environment: ```source activate env_name```
* To get back to your default conda:  ```source deactivate```
* The active environment will have an asterisk next to it in ```conda env list```

[basemap-link]: https://matplotlib.org/basemap/
[basemap-sunset]: https://matplotlib.org/basemap/users/intro.html
[basemap-sunset-forum]: https://github.com/SciTools/cartopy/issues/920
[cartopy-link]: https://scitools.org.uk/cartopy/
