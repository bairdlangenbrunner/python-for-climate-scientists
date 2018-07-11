---
permalink: /where-to-start/
layout: page
title: where to start
order: 4
---

# Where to start

If you find yourself at the beginning of your Python experience, and you're not totally sure where to begin, you've come to the right place!  I'm writing this to hopefully get you started.

And I have to say, if this *is* your first foray into Python, I'm very excited for you.  It's easier now than ever before to manage a happily running Python installation on any operating system.  For you, that means less time banging your head against a keyboard, and more time learning :clap: that :clap: language.

In this case of these recommendations, most of my tips are based on a Mac OS, but if you're a Windows or LINUX user, you can follow approximately the same steps below.

## Step 1.  Install conda or miniconda on your machine.

I would recommend using either Anaconda or miniconda for this.  They each have their advantages an disadvantages; if you're going for a lightweight installation, miniconda is what you want.  Anaconda is a bit bulky but comes with lots of bells and whistles.  Personally, I use both depending on the machine I'm using.  Anaconda can take up to 10-20 GB of space after all is said and done, so if that could be an issue, avoid it.

* If you're on a Mac, installing is as simple as downloading the binary file and opening it.

* If you're on a LINUX machine, I would download the tarball and do it from the command line:

* If you're on a Windows, I'm very sorry to hear that.  You can also just download the binary directly.

### What's the difference between conda and Anaconda?

Good question!  I had to look this one up myself (multiple times).  ```conda``` is an open source package manager that was built to manage all the packages you need to run Python succesfully.  Technically, it's language agnostic, so if you find yourself using other open source languages like R or Julia often, ```conda``` is a great way to get those robustly onto your computer. 

### What about ```pip```?  I know someone who uses that.  Maybe I can just use it for Python?

Sure, ```pip``` is totally fine!  But I'll let you in on a little secret:  it comes *with* ```conda```, so you may as well go with that instead.

### Hmm... ok, and what about Canopy?  One of my labmates uses that.

I mean, go ahead and try it if you want, but I honestly think of it as a little outdated.  That could be a controversial statement, but here are my reasons for using ```conda```:

1.  With ```conda```, you can install multiple parallel "environments" of Python (or whatever *other* languages you prefer).  That means you can have a new Python you use most of the time and an older one that works with some random chunk of code you inherited from someone who graduated years ago never to be heard from again.
2.  Building off this first point, you can actually install non-python-related things in these environments, like NCO (NetCDF Operators), CDO (climate data operators), 

## Step 2.  Mess around with the conda installation and make sure everything looks alright.

If you're following along, I'd recommend looking at the official [getting started with ```conda```](https://conda.io/docs/user-guide/getting-started.html) documentation.

The first thing to do is open up a terminal shell (Terminal on Mac, or my preference:  iTerm2), type ```python```, and hit enter.

```
baird$ python

Python 3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 11:07:29)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

From the lines above, you can see that I'm running Python 3.6.6 via Anaconda.  If you downloaded Anaconda or miniconda and you don't see it above, you may have to mess around with your bash profile.  See [this]() from Stack Overflow.
