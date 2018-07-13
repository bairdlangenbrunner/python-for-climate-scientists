---
title: Helvetica in Python
order: 2
---

> *Disclaimer: The info below has worked for me, but getting nonstandard fonts to work in Python seems to be quite finicky.  I pulled information from [Olga Botvinnik's blog entry on the subject][olga-blog-entry], which is worth reading in its entirety, and have also found a [group lab website][chang-lab-helvetica] that has done similar things.*

I don't have a lot of complaints about Python and Matplotlib, but something that has always irked me is the default font.  It's currently DejaVu Sans, which looks a little too squat for me when comparing it to other sans serif fonts like Helvetica and Arial.

Here's an example of the current default font (with very large font sizes for emphasis):

<div style="width:60%">![](/figures/fonts/dejavu_sans_example.png)</div>

I know these are small fish I'm frying, but I find this font pretty fugly--especially the numbers on the axes (and the -1 subscript).  They're just... annoyingly wide.

Here's what it looks like with Helvetica.  Much better, right?

<div style="width:60%">![](/figures/fonts/helvetica_example.png)</div>

<div style="width:60%">![](/figures/fonts/helvetica_example_fixed_mathtext.png)</div>

, and every time I install Matplotlib anew on a machine, I make sure I get Helvetica working properly and by default with it.  It's a fairly simple process, originally described in [Olga Botvinnik back in 2012][olga-blog-entry], and I always refer back to it when I need to.

---

### Other font options

* [**Seaborn**][seaborn-website] comes with Arial installed by default.  If you don't really have a preference for which font you're using, but you just *really don't like DejaVu Sans* (understandable!).  (Note if you're using LINUX, you may have still have to install it yourself; see [here][font-seaborn-stackoverflow].)

* Jupyter versus .py for fonts, particularly Latex rendering

[olga-blog-entry]: https://github.com/olgabot/sciencemeetproductivity.tumblr.com/blob/master/posts/2012/11/how-to-set-helvetica-as-the-default-sans-serif-font-in.md

[chang-lab-helvetica]: http://www.claridgechang.net/blog/how-to-use-custom-fonts-in-matplotlib

[seaborn-wesite]: https://seaborn.pydata.org/

[font-seaborn-stackoverflow]: https://stackoverflow.com/questions/20753782/default-fonts-in-seaborn-statistical-data-visualization-in-ipython

[dejavu-sans-example]:
