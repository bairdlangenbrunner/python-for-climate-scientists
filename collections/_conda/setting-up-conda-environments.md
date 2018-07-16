---
title: Conda environments for NCO, NCL, and CDO
date: 2018-07-10
order: 1
---

> *Disclaimer:  This assumes knowledge of a conda-based Python installation (e.g., [Anaconda or Miniconda](https://conda.io/docs/index.html)).  Read through the documentation websites or the [where to start][where-to-start-page] page to learn more about this.*

Environments in conda are incredibly useful.  They allow you to install parallel versions of Python and its packages, or even other languages and software, that mind their own business and never affect one another.

In my own research, I actively use several different conda environments to keep everything in its place.  If you're up and running with conda, then you can see what environments you currently have by typing ```conda env list``` in a terminal window.  You'll have at least one, called the base environment, and the asterisk means it's the current/active environment:

```
conda env list

# conda environments:
#
base                  *  /Users/baird/miniconda3

vcv076219:python-for-climate-scientists baird$
```

This tells me that I currently only have a base environment, and it's installed on my home directory at ```/Users/baird/miniconda3```.

Installing an environment is also a great way to make the switch to a new Python library or package without breaking your installation for all your current scripts.  For example, if you use [basemap][basemap-link] for plotting maps, you may have heard it's [being retired][basemap-sunset] in the next couple years (see also [this discussion][basemap-sunset-forum]).  Its replacement is officially [cartopy][cartopy-link], but when you try to install them both, their packages can conflict.  **The solution:  Install a *separate cartopy environment* to get used to it, and once you feel confident, change your base environment to cartopy and create a ```basemap_stable``` environment for basemap-specific tasks.**  That's at least what I did, and I was able to finish projects that I had started with basemap but start new ones in cartopy.

I typically keep at least four separate environments on a machine (in addition to the default), described below.  You could get away with combining some of them into the same one below (and I encourage you to try, because you'll learn a lot about conda when you run into issues and have to resolve them).  I've learned the setup below works best for me.

|conda environment  |use for      |install commands
|---                |---          |---
|**base**           |most things  |---
|**nco_stable**     |NCO (NetCDF Operators) | conda install -c conda-forge nco
|**ncl_stable**     |NCL (NCAR Command Language) | conda install -c conda-forge ncl
|**cdo_stable**     |CDO (Climate Data Operators) | conda install -c conda-forge cdo
|**basemap_stable** |basmap (assuming you have cartopy in your base environment)  | conda install basemap

To create these environments yourself (base is the default, so no need to make that), follow the steps below.  I like to use the ```_stable``` suffix because it helps me mentally separate an *environment* related to NCO from the language itself.  You can name them anything you like, though.

```
conda create --name nco_stable
```

Choose ```y``` when prompted.  Once the environment is created, activate it by typing:

```
source activate nco_stable
```

And from here, you can install the package you want within it.  For NCO, that will look like this:

```
conda install -c conda-forge nco
```

Note the ```-c``` in ```-c conda-forge``` means "channel."  What this does is tells conda to look in the "conda-forge" channel (which hosts a broader range of user-created packages and beta versions of official Python packages).  To see what channels were used to install your conda packages, type ```conda list```.  This conveniently lists the packages installed in the current environment, their version and build information, and the channel used to install them.  For packages with nothing under the "Channel" column, they were installed using the defaults channel.  For NCO and other fairly specific software packages, conda will typically need the conda-forge channel.

This is an example for the ```ncl_stable``` environment.  These are all the packages that conda installed to get NCO on my computer.  (Imagine having to keep all of these, and even more, working compatibly!  This is the true utility of a conda environment.)

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

---

### Keeping environments up-to-date

Every once in a while, I'll activate each of my environments and tell conda to update everything to its latest version:

```
source activate nco_stable
conda update --all
```

Then choose ```y``` to approve of the udpates.  Some packages will inevitably be downgraded, but I usually go for it anyway.

[basemap-link]: https://matplotlib.org/basemap/
[basemap-sunset]: https://matplotlib.org/basemap/users/intro.html
[basemap-sunset-forum]: https://github.com/SciTools/cartopy/issues/920
[cartopy-link]: https://scitools.org.uk/cartopy/
[where-to-start-page]: https://bairdlangenbrunner.github.io/python-for-climate-scientists/where-to-start/
