---
title: Troubleshooting import issues with conda
date: 2018-07-15
order: 3
---

I tend to be an early adopter of new libraries and updated packages, but this often leads to package compatibility issues or the accidental wiping of an important library file buried somewhere in my Anaconda/Miniconda installation.  Most frequently, I seem to have trouble with "dylib" files in curl, c++, libpng, and other libraries that conda has installed for various packages.

If you're getting an ```ImportError``` with a ```Reason:  image not found``` related to some sort of dylib file, you're not alone.  I encounter this about once a week.

<div style="width:50%">
![pr gif](https://media.giphy.com/media/ERMGXqtKTDKHC/giphy.gif)</div>
<br>

These are the steps I take to remedy it.  Unfortunately, I haven't really found a one-size-fits-all solution, so I typically bounce back and forth between some of the steps below till things work again.  My advice here is to be persistent and keep a log of what you've done.

---

1. **Try updating the library.** This happened recently for me when attempting to ```import gdal```, which itself was failing because of a missing curl library file with an error message referencing a missing file with the name of something similar to ```libcurl.4.dylib```.
 So I started by typing:
```
conda upgrade gdal
```

1. **Use the conda-forge channel, instead.**  Close Python, reopen it, and try your import statement again.  If it doesn't work, try using the conda-forge channel instead:
```
conda install -c conda-forge gdal
```

1.  **Find the offending libraries.**  Close, reopen, and re-import.  If that doesn't work, you may need to try to update the specific libraries that are giving trouble (in this case, curl).  For me, I had an idea that it was curl-related, so I went looking for curl-specific libraries.  Type ```conda list``` to see them all and find the one you want.

  * I find that I often have *both* a ```curl``` *and* a ```libcurl``` packge installed, so you may have to scroll to the ```lib*``` section of the ```conda list``` output (it's in alphabetical order) to see what related libraries you have.

1. **Update those libraries.**  Try upgrading those specific libraries with their default branch first.  This would be something like below (substituting ```curl``` and/or ```libcurl``` for whatever your issues are coming from):
```
conda upgrade curl
conda upgrade libcurl
```

1. **Try conda-forge again.**  Close and re-open Python and try importing things again.  If the issue is still there, I usually try to install a conda-forge version of the packages/libraries, since it's possible that another person has already encountered this issue and has posted an update on conda-forge.
```
conda install -c conda-forge curl
conda install -c conda-forge libcurl
```

1.  **Move failing library to a new environment or revert to old conda revision.**  If it **STILL** doesn't work, you may have to move the specific library/package you want to a new environment and use it from there (this has been true in the past for cartopy and basemap, for example).  You can also roll your conda installation back to a revision that worked before, though this will downgrade any updates you've added since then.  You can do this by picking out the revision you want:
```
conda list -r
```
and the output will list a bunch of revisions and the libraries that were updated for each.
```
2018-07-15 11:49:54  (rev 16)
     cartopy  {0.16.0 -> 0.16.0}
     gdal  {2.2.2 -> 2.3.0}
     hdf5  {1.10.1 -> 1.10.2}
     kealib  {1.4.7 -> 1.4.7}
     libgdal  {2.2.4 -> 2.3.0}
     libnetcdf  {4.4.1.1 -> 4.6.1}
     libspatialite  {4.3.0a -> 4.3.0a}
     netcdf4  {1.3.1 -> 1.4.0}
     proj4  {4.9.3 -> 5.0.1}
     pyproj  {1.9.5.1 -> 1.9.5.1}
```
Pick the revision number you want (say I want to revert back to #16 above).  Then install it:
```
conda install --revision 16
```

1. **Remove and re-install the library.**  If it *still* doesn't work, you may have to remove the library entirely and reinstall it.  This can be an involved process, and conda will typically remove a lot of dependencies and clear out anything that was initially installed with the library.  Then reinstall it.
```
conda remove curl
conda install curl
```

1. **Last resort:**  A last resort would be either to delete the environment you're working in or to uninstall Anacona/Miniconda entirely, and then set up everything again, but I tend to avoid this.
