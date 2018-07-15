---
permalink: /where-to-start/
layout: page
title: where to start
order: 2
---

> This page is a work in progress.

If you're at the beginning of your Python experience, and you're not totally sure where to begin, I'm writing this for you.

And I have to say, if this *is* your first foray into Python, I'm very excited for you!  It's easier now than ever before to manage Python on an operating system.  For you, that means less time banging your head against a keyboard trying to get your libraries to cooperate with one another, and more time :clap: learning :clap: that :clap: language.

Are you excited yet?!

![doge](https://media.giphy.com/media/9gn4lhW6wiQ6c/giphy.gif)

> *One note before I go further:  Most of the tips here are based on my experience with Mac OS, but if you're a Windows or LINUX user, use this resource with other documentation specific to your OS.*

---

### 1. To get Python going, use Anaconda or Miniconda.

I recommend using either **[Anaconda or Miniconda][conda.io]** to install and maintain Python on your machine(s).

> * ```Anaconda``` and ```Miniconda``` are software packages that install the Python language, some other useful packages, and most importantly, ```conda```.
>
>
> * ```conda``` itself is an open source package manager that was built in Python and helps keep all of its libraries compatible.  (Well, it was originally built for Python, but it's technically language-agnostic. so if you find yourself using other open-source languages like R or Julia often, conda is a great way to maintain them.)

If you're brand new to Python, Anaconda will probably be a safer bet.  It's a little bulky and will take a little longer to install, but it will also give you the most options while learning the language.  Miniconda is a stripped down version of Anaconda, so if you don't have much disk space, go with that.  Personally, I like Miniconda, since it's more lightweight for laptops, shared computers, or login nodes where disk space is limited.

#### Why conda?
> 1.  This is getting a little ahead of myself, but with conda, you can install multiple parallel "environments" of Python (or whatever *other* languages you prefer).  That means you can have a Python installation you use most of the time *and* an older one that works with some random chunk of code you inherited from a student in your lab who graduated years ago.
>
>
> 2.  Another powerful aspect of conda is that you can use it to install non-Python-related software.  For example, you can set up a single or different environments for [NCO (NetCDF Operators)][nco-link], [CDO (Climate Data Operators)][cdo-link], and the [NCL (NCAR Command Language)][ncl-link].  This, in my opinion, is what makes it so valuable.
>
>
> 3. Anaconda/Miniconda are free (their developer, Continuum, offers proprietary add-ons, but there's no reason you'll ever need those).

#### Alternatives to Anaconda/Miniconda
> **"So what about pip for installing Python?  I know someone who seems to prefer that."**
> Sure, pip is totally fine!  But I'll let you in on a little secret:  it comes *with* Anaconda and Miniconda, so you may as well go with one of those instead.
>
>
> **"Hmm... ok, and what about Canopy?  I think I met a ghost once who uses it!"**
> Canopy seems like it could be great, but it's not free to use the full distribution, and the Python community really seems to be gathering around conda these days.

### 2. Mess around with conda and get the hang of it.

I can do this as much justics as the half-hour [getting started with conda][conda-tutorial-link] documentation.  That will get you where you need to be.

### 3. Install the libraries you'll need most.

If you just installed Anaconda, some of these will already be on your system.  If you installed Miniconda, you'll likely need to grab a few extra things.  The most useful libraries for any Python installation are below.  Getting these is a good first step.

| library           | main use
|---                |---
| numpy, scipy      | core Python tools
| matplotlib        | plotting
| jupyter   | Jupyter Notebook and related tools |

My favorite libraries **more specific to Earth science data analysis include**:

| library           | main use
|---                |---
| cartopy           | plotting maps
| pandas            | loading/saving .csv, .txt, and other spreadsheet files; general panel data statistics package
| xarray   | pandas for 3+ dimensions; NetCDF and HDF input/output; quick plotting
| netcdf4   | NetCDF data analysis; great as secondary option to xarray |
| gdal       | library and packages for the Geospatial Data Abstraction Library; useful for reading in HDF and geotiff files (remote sensing data sets)
| wrf-python        | wrapper for Fortran functions that analyze WRF output
| seaborn | more plotting options; has a nice color bar builder and interfaces with [ColorBrewer][colorbrewer-link]
| cmocean | really great colorblind-friendly colormaps  |

You can install these one at a time:
```
conda install matplotlib
```
Or you can install a bunch at once, e.g.:
```
conda install numpy scipy matplotlib pandas xarray jupyter
```

If you install cartopy, I'd recommend going for the conda-forge channel option:
```
conda install -c conda-forge cartopy
```

This will get you a slightly more stable version, since the folks over at SciTools seem to [recommend this one for conda-based installation][cartopy-install].

### 4. Go forth and code

Make sure you install the four packages in the first table above (```numpy```, ```scipy```, ```matplotlib```, and ```jupyter```).  This will get you the main ingredients you need to get familiar with Python.

Probably the easiest way to learn the language is using Jupyter Notebook, which takes Python and puts it into a browser window and lets you add notes, images, and even Latex to document your workflow.

To start up a notebook, you want to navigate to a directory where you'd like to save it on your computer, then type:
```
jupyter notebook
```

If all works smoothly, your default web browser will pop up with a window, and you're good go to.

I recommend skimming the [Jupyter Notebook documentation][jupyter-notebook-doc] and going deeper on some tutorials from here.  YouTube has plenty of good videos, and here are some website options:
* Dataquest's [Jupyter Notebook for Beginners](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
* An unofficial (but seemingly legitimate) [Quick Start Guide](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/)
* This [Getting Started](https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46) tutorial on Medium

<!--
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

Others that I don't use quite as much but still think are nice to know about:

| extra libraries               | main use |
| --- | --- |
| deap   |   |
| scikit-learn   |   |
| [stefan's favorites?]   |   |

### 4. Open Python from the terminal shell.

### 5. Open a Jupyter Notebook and use this to run Python.

Here's a Jupyter Notebook you can download and open.  To do this download the notebook into a new folder, use the terminal to ```cd``` into that directory, and from that folder invoke notebook by typing ```jupyter notebook``` and hitting return.
-->

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
[cartopy-install]: https://scitools.org.uk/cartopy/docs/latest/installing.html#installing
[colorbrewer-link]: http://colorbrewer2.org/
[jupyter-notebook-doc]: http://jupyter.readthedocs.io/en/latest/index.html
