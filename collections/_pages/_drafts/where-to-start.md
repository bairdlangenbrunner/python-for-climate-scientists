---
permalink: /where-to-start/
layout: page
title: where to start
order: 4
---

# Where to start

> By the end of this, you will be able to run Python from within your command line or from Jupyter Notebook.

If you find yourself at the start of your Python experience, and you're not totally sure where to begin, you've come to the right place!  I'm writing this to hopefully get you started.

And I have to say, if this *is* your first foray into Python, I'm very excited for you!  It's easier now than ever before to manage Python on an operating system.  For you, that means less time banging your head against a keyboard trying to get your libraries to cooperate with one another, and more time :clap: learning :clap: that :clap: language.

Are you excited yet?!

![doge](https://media.giphy.com/media/9gn4lhW6wiQ6c/giphy.gif)

One note before I go further:  Most of the tips here are based on my experience with Mac OS, but if you're a Windows or LINUX user, use this resource with other documentation specific to your OS.

---

### 1. To get Python going, install conda on your machine.

I recommend using either [Anaconda or Miniconda][conda.io] for this.

Which one, do you ask?  If you're brand new to Python, Anaconda will probably be a safer bet.  Miniconda is a stripped down version of Anaconda, so if you don't have much disk space, go with the mini version.  Personally, I use both, depending on the machine (e.g., on my *own* computer, I keep a giant Anaconda going, which can take up 10-20 GB of space if I'm being ambitious).  Miniconda is great for shared computers or login nodes, where your home disk space is limited.

> **So... what are conda, Anaconda, and Miniconda?**  Good question!  I had to look this one up myself (multiple times).  ```conda``` is an open source package manager that was built to manage the dependencies of a given language or set of packages.  It was built for Python, but it's technically language agnostic, so if you find yourself using other open-source languages like R or Julia often, consider using conda to maintain them.
>
> **Why conda, then?**
> 1.  With conda, you can install multiple parallel "environments" of Python (or whatever *other* languages you prefer).  That means you can have a Python installation you use most of the time *and* an older one that works with some random chunk of code you inherited from a student in your lab who graduated years ago (?) and is doing something in... maybe the tech world at this point?
> 2.  My **favorite** aspect of conda is that you can use it to install non-Python-related software.  For example, you can set up a single or different environments for [NCO][nco-link], [CDO (Climate Data Operators)][cdo-link], and the [NCAR Command Language][ncl-link].  You can even use it to install [ncview][ncview-link]!
> 3. Anaconda/Miniconda are free (their developer, Continuum, offers proprietary add-ons, but there's no reason you'll ever need those).
>
> **What about pip?  I know someone who seems to prefer that.**
> Sure, pip is totally fine!  But I'll let you in on a little secret:  it comes *with* conda, so you may as well go with that instead.
>
> **Hmm... ok, and what about Canopy?  I think I met a ghost once who uses it?**
> Canopy seems like it could be great, but it's not free to use the full distribution, and the Python community really seems to be gunning for conda these days.  I vote conda.

---

### 2. Mess around with conda and get the hang of it.

If you're following along, I'd recommend looking at the half-hour [getting started with conda][conda-tutorial-link] documentation.

#### 2.1.  

The first thing to do is open up a terminal shell (Terminal on Mac, or my preference:  iTerm2), type ```python```, and hit enter.  If your Anaconda installation was successful, it will show something like this:

```
baird$ python

Python 3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 11:07:29)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

From the lines above, you can see that I'm running **Python 3.6.6** via Anaconda, which was released in June 2018.  By typing ```python``` and hitting return, I invoked the Python shell, which is denoted by the ```>>>``` line.

> If you downloaded Anaconda or Miniconda and you don't see the output above, it means your terminal probably isn't recognizing ```conda``` as a command, and you need to tell it where the installation lives.
>
> This is likely related to whether your environment has conda in its path.  The first thing to do is open a *new* terminal shell to see if simply needs to refresh (technically by running your home directory's ```.bash_profile``` or ```.bashrc``` again).  If that doesn't work, it probably means the path to Anaconda/Miniconda wasn't added at installation time.  See [this]() from Stack Overflow.

---

### 3. Install the libraries you'll need most.

If you just installed Anaconda, some of these will already be on your system.  My most-used libraries are:

| library           | my main use
|---                |---
| numpy, scipy      | core Python tools
| pandas            | loading/saving csv, txt, and spreadsheet files; taking rolling sums and averages
| xarray, netCDF4   | messing with NetCDF and gridded data sets; acts as a >2 dimensional version of pandas
| osgeo, gdal       | for remote sensing data sets (like MODIS)
| wrf-python        | wrapper for Fortran functions that analyze WRF output
| matplotlib        | plotting
| cartopy           | plotting maps
| seaborn, cmocean  | great color maps, more plotting options

Others that I don't use quite as much but still think are nice to know about:

### 4. Open Python from the terminal shell.

### 5. Open a Jupyter Notebook and use this to run Python.

Here's a Jupyter Notebook you can download and open.  To do this download the notebook into a new folder, use the terminal to ```cd``` into that directory, and from that folder invoke notebook by typing ```jupyter notebook``` and hitting return.


<!--
### 6. Use pandas to open a .csv file.

### 7. Make a quick plot of El Niño SSTs.

Check out 1997-1998!  That one was aggressive.

### 8. Save that figure.

### 9. Go get some coffee.

Or grab some tea?  Seriously, you deserve it.  This can be frustrating.
-->

[conda-tutorial-link]: https://conda.io/docs/user-guide/getting-started.html
[conda.io]: https://conda.io/docs/user-guide/install/download.html
[ncview-link]: https://conda.io/docs/user-guide/install/download.html
[nco-link]: https://conda.io/docs/user-guide/install/download.html
[ncl-link]: https://conda.io/docs/user-guide/install/download.html
[cdo-link]: https://conda.io/docs/user-guide/install/download.html
