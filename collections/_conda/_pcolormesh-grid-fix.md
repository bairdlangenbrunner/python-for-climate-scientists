---
title: Fixing pcolormesh offsets in cartopy
order: 2
---

As I've said elsewhere, I have only a few complaints about the default behavior of Matplotlib.

One of the biggest ones (but admittedly in the weeds) is how the ```pcolormesh``` and ```pcolor``` functions work.  I tend to use ```pcolormesh``` more, since they are practically the same function but the former is much faster to render.

You may be familiar with how they work.  

The caveat for both of them can be found in the [pcolor documentation][pcolor-site], and it has to do with



[pcolor-site]: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolor.html
[pcolormesh-site]: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolormesh.html
[cartopy-site]: https://scitools.org.uk/cartopy/docs/latest/
