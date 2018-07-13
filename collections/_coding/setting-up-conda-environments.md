---
title: conda environments for NCO, NCL, and CDO
date: 2018-07-10
---

Environments in conda are incredibly useful:  they allow you to install parallel versions of Python and its packages, or even other languages and software, that mind their own business and never affect one another.

In my own research, I actively use several different conda environments to keep everything in its place.  To see what environments you currently have, type ```conda list env```.  You'll have at least one, called the base environment, and the asterisk means it's the current/active environment:

```
conda env list

# conda environments:
#
base                  *  /Users/baird/miniconda3

vcv076219:python-for-climate-scientists baird$
```

Installing an environment is also a great way to make the switch to a new Python library or package without breaking your installation for all your current scripts.  For example, if you use [basemap][basemap-link] for plotting maps, you may have heard it's [being retired][basemap-sunset] in the next couple years (see also [this discussion][basemap-sunset-forum]).  Its replacement is officially [cartopy][cartopy-link], but when you try to install them both, their packages conflict (or at least they did in the past).  **The solution:  Install a separate cartopy environment to get used to it, and later switch your base environment over to cartopy.**

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
conda create --name ncl_stable
conda create --name cdo_stable
```

* To activate an environment: ```source activate env_name```
* To get back to your default conda:  ```source deactivate```
* The active environment will have an asterisk next to it in ```conda env list```

> More to come...

[basemap-link]: https://matplotlib.org/basemap/
[basemap-sunset]: https://matplotlib.org/basemap/users/intro.html
[basemap-sunset-forum]: https://github.com/SciTools/cartopy/issues/920
[cartopy-link]: https://scitools.org.uk/cartopy/
