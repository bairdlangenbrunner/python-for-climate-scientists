---
permalink: /where-to-start/
layout: page
title: where to start
order: 4
---

If you find yourself at the very beginning of your Python experience, and you're not totally sure where to begin, you've come to the right place!  I'm writing this to hopefully get you started.

And I have to say, if this *is* your first foray into Python, I'm very excited for you.  It's easier now than ever before to manage a happily running Python installation on any operating system.

In this case, most of this information is specific to a Mac OS, but you can follow parallel steps to get other important things.

## Step 1.  Install conda or miniconda on your machine.

I would recommend using either Anaconda or miniconda for this.  They each have their advantages an disadvantages; if you're going for a lightweight installation, miniconda is what you want.  Anaconda is a bit bulky but comes with lots of bells and whistles.  Personally, I use both depending on the machine I'm using.  Anaconda can take up to 10-20 GB of space after all is said and done, so if that could be an issue, avoid it.

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
