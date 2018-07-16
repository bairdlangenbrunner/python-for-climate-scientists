---
title: Troubleshooting import issues with conda
date: 2018-07-15
order: 3
---

I tend to be an early adopter of new libraries and updated packages, but this often leads to package compatibility issues or the accidental wiping of an important library file buried somewhere in my Anaconda/Miniconda installation.  Most frequently, I seem to have trouble with "dylib" files in curl, c++, libpng, and other libraries that conda has installed for various packages.

If you're getting an ```ImportError``` with a ```Reason:  image not found``` related to some sort of dylib file, you're not alone.  I encounter this about once a week.

![power rangers gif](https://media.giphy.com/media/ERMGXqtKTDKHC/giphy.gif)

These are the steps I take to remedy it.  Unfortunately, I haven't really found a one-size-fits-all solution, so I typically bounce back and forth between some of the steps below till things work again.

**My advice here is to be persistent and keep a log of what you've done.**  I keep a text file in my main Dropbox directory titled "useful_conda_notes.txt", and any time I encounter an issue like that, I log the successes/failures there.

---

**1. Try updating the library.** A dylib error happened recently for me when executing ```import gdal``` in Python.  The error message told me this was failing because of a missing ```curl``` library file with an error message referencing a missing file with the name of something similar to ```libcurl.4.dylib```.  My first assumption is that ```gdal``` is simply a little outdated, and the first step is to try upgrading it.
```
conda upgrade gdal
```

Test if this worked by closing Python, reopening it, and running the problematic command.

---

**2. Use the conda-forge channel, instead.**  If it doesn't work, try using the conda-forge channel to update the library, instead.  In this case, you don't use the ```upgrade``` syntax, but rather issue a new install command:
```
conda install -c conda-forge gdal
```

Again, check if it works by restarting Python and trying the import command.

Still no dice?  This tells you that the issue is lurking deeper in the libraries that ```gdal``` *depends on*.  Based on the error message, you can usually get a good sense of which library is causing it.  In my case, the clue was the **libcurl.4.dylib** syntax; looks like ```curl``` is the real culprit, so I'll try and fix that.

---

**3. Find the offending libraries.**  List the libraries in the current environment and see if any look like they're related to the error message.  Do this by typing ```conda list```.

  * In this case, I found *both* the main ```curl``` library *and* ```libcurl``` installed.  This secondary library is probably where the problem actually resides, but updating ```curl``` will typically take care of it.

---

**4. Update those libraries.**  Try upgrading those specific libraries using the default channel.  The second line may not be necessary always, since a ```curl``` update should take care of ```libcurl```:
```
conda upgrade curl
conda upgrade libcurl
```

Again, close/reopen your Python shell and try out the import statement.

---

**5. Try conda-forge again.**  If the issue is still there, I try to install a conda-forge version of the packages/libraries, since it's possible that another person has already encountered this issue and has posted an update on that channel.
```
conda install -c conda-forge curl
conda install -c conda-forge libcurl
```

---

**6. Move library to a new environment or revert to old conda revision.**  If it **STILL** doesn't work, you may have to move the specific library/package you want to a new environment and use it from there (this has been true in the past for cartopy and basemap, for example).  You can also roll your conda installation back to an older version, if you had it working before, though this will downgrade any updates you've added since then.  You can do this by picking out the revision you want:
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
Pick the revision number you want (say I want to revert back to #16 above) and install it:
```
conda install --revision 16
```

---

**7. Remove and re-install the library.**  If it *still* doesn't work, you may have to remove the library entirely and reinstall it.  This can be an involved process, but it's typically where I end up if nothing else works.  Depending on my level of frustration, sometimes I just take a "scorched Earth approach" get rid of all the things that seem wrong.
```
conda remove gdal curl
```

Then reinstall them, hopefully in a working manner:
```
conda install gdal curl
```

---

Good luck!  You've got this.
