---
title: Helvetica in Python
order: 2
---

> *Disclaimer: The info below has worked for me, but Python seems to be quite finicky with fonts.  I pulled information from [Olga Botvinnik's blog entry on the subject][olga-blog-entry], which is worth reading in its entirety, and I've also found a [group lab website][chang-lab-helvetica] that has done similar things.  The steps below are a bit more simplified.*

I don't have a lot of complaints about Matplotlib, but something that has always irked me is the default font.  It's currently DejaVu Sans; here it is, in all its squat glory:

<div style="width:60%">![](/figures/fonts/dejavu_sans_example.png)</div>

I know this is a small fish to fry, but I'm not a fan of this font--especially the numbers on the axes (and the -1 subscript).  They're just... annoyingly wide!

---

Here's what it looks like with Helvetica:

<div style="width:60%">![](/Users/baird/Dropbox/_github_repos_personal/python-for-climate-scientists/figures/fonts/helvetica_example.png)</div>

Check out those thinner letters!  Notice those sexier numbers.  I'm into it.

One thing that is still off here, however, is the -1 superscript on the units label.

<div style="width:60%">![](/figures/fonts/helvetica_example_fixed_mathtext.png)</div>

, and every time I install Matplotlib anew on a machine, I make sure I get Helvetica working properly and by default with it.  It's a fairly simple process, originally described in [Olga Botvinnik back in 2012][olga-blog-entry], and I always refer back to it when I need to.

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

[dejavu-sans-example]:
