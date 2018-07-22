---
title: Helvetica in Python
order: 2
---

> *Disclaimer: The info below has worked for me, but Python seems to be quite finicky with fonts.  I pulled information from [Olga Botvinnik's blog entry on the subject][olga-blog-entry], which is worth reading in its entirety, and I've also found a [group lab website][chang-lab-helvetica] that has done similar things.  The steps below are a bit more simplified, thanks to those who have already reported on this.*

I don't have a lot of complaints about Matplotlib, but something that has always irked me is the default font.  It's currently DejaVu Sans; here it is, with the code to reproduce it, in all its squat glory:

```python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

xvals = np.linspace(-5,5,1000)
yvals = np.cos(xvals)
```

```python
fontsize = 24

fig, ax = plt.subplots()
fig.set_size_inches(4.5,3.75)

ax.plot(xvals,yvals,c='0.1',lw=2,label=r'$\phi(t)$')

ax.tick_params(labelsize=fontsize)
ax.set_xlim(-np.pi, np.pi)
ax.set_title('title', fontsize=fontsize)
ax.set_xlabel(r'$\alpha \beta \gamma$ units$^{\,-1}$', fontsize=fontsize)
ax.set_ylabel('y label', fontsize=fontsize)
ax.legend(fontsize=fontsize, loc=0, facecolor='None')

fig.tight_layout()
```

<div style="width:60%">![](/figures/fonts/dejavu_sans_example.png)</div>

<br>

I know this is a small fish to fry, but I'm not a fan of this font--especially the numbers on the axes (and the -1 subscript).  They're just... distractingly wide. >_<

Note you can add Latex-style formatting in Matplotlib by using two dollar signs with a prefix "r" around the string's quotatio marks:```r'$\alpha$'```.  In Jupyter Notebook, you can usually drop the "r" and just use ```$\alpha$```.

---

Here's what it looks like with Helvetica (after making adjustments to the default, which you can read about below):

```python
fontsize = 24

fig, ax = plt.subplots()
fig.set_size_inches(4.5,3.75)

ax.plot(xvals,yvals,c='0.1',lw=2,label='$\phi(t)$')

ax.tick_params(labelsize=fontsize)
ax.set_xlim(-np.pi, np.pi)
ax.set_title('title', fontsize=fontsize)
ax.set_xlabel(r'$\alpha \beta \gamma$ units$^{\,-1}$', fontsize=fontsize)
ax.set_ylabel('y label', fontsize=fontsize)
ax.legend(fontsize=fontsize, loc=0, facecolor='None')

fig.tight_layout()
```

<div style="width:60%">![](/figures/fonts/helvetica_example.png)</div>

<br>
Check out that dreamy text!  Woof.

One thing that is **still** off, however, is the font of the the -1 superscript on the units label.  And if you compare the two figures closely, you'll also notice the Greek letters on the x-axis label haven't changed (but... they *should*, right?  Helvetica and DejaVu Sans should have different math-styled fonts.)

The final solution comes from telling the "rcParams" (run command parameters) to use the regular font (now Helvetica) as the formatting for math.

```python
plt.rcParams.update({'mathtext.default': 'regular'})

fontsize = 24

fig, ax = plt.subplots()
fig.set_size_inches(4.5,3.75)

ax.plot(xvals,yvals,c='0.1',lw=2,label='$\phi(t)$')

ax.tick_params(labelsize=fontsize)
ax.set_xlim(-np.pi, np.pi)
ax.set_title('title', fontsize=fontsize)
ax.set_xlabel(r'$\alpha \beta \gamma$ units$^{\,-1}$', fontsize=fontsize)
ax.set_ylabel('y label', fontsize=fontsize)
ax.legend(fontsize=fontsize, loc=0, facecolor='None')

fig.tight_layout()
```

<br>

<div style="width:60%">![](/figures/fonts/helvetica_example_fixed_mathtext.png)</div>

<br>

Ok, we're in business.

---

### Setting this up on your machine

Every time I install Matplotlib anew on a machine, I make sure I get Helvetica working properly and by default with it.  It's a fairly straightforward process, but you have to be patient.  I always refer back to this [blog entry][olga-blog-entry].

#### 1. Obtain Helvetica in ```.ttf``` format.
The blog linked above gives instructions to do this on a Mac (by converting the ```.dfont``` files already available into ```.ttf```).  I keep them [here][helvetica-ttf-location] for quicker personal access, though.  You should have about 6 files (that cover all the weights/styles).

#### 2. Place those ```.ttf``` files wherever Matplotlib keeps its fonts.
If you have Anaconda/Miniconda, it will be somewhere like this:

```
~/miniconda3/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf
```

You can search for this location by typing 

---

for LINUX:
~/.cache/matplotlib/fontList.json
~/.config/matplotlib/matplotlibrc

### Other font options

* [**Seaborn**][seaborn-website] comes with Arial installed by default.  If you don't really have a preference for which font you're using, but you just *really don't like DejaVu Sans* (understandable!).  (Note if you're using LINUX, you may have still have to install it yourself; see [here][font-seaborn-stackoverflow].)

* Jupyter versus .py for fonts, particularly Latex rendering

[olga-blog-entry]: https://github.com/olgabot/sciencemeetproductivity.tumblr.com/blob/master/posts/2012/11/how-to-set-helvetica-as-the-default-sans-serif-font-in.md

[chang-lab-helvetica]: http://www.claridgechang.net/blog/how-to-use-custom-fonts-in-matplotlib

[seaborn-wesite]: https://seaborn.pydata.org/

[font-seaborn-stackoverflow]: https://stackoverflow.com/questions/20753782/default-fonts-in-seaborn-statistical-data-visualization-in-ipython

[helvetica-ttf-location]: https://github.com/bairdlangenbrunner/bairdlangenbrunner.github.io/tree/master/helvetica_ttf_files
