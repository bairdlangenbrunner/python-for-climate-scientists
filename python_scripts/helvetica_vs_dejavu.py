# set backend so it plots
import matplotlib
matplotlib.use('TkAgg')

import numpy
import matplotlib.pyplot as mp

# matplotlibrc file
matplotlib.matplotlib_fname()
# fontList.cache file
matplotlib.get_cachedir()

xvals = numpy.linspace(-5,5,1000)
yvals = numpy.cos(xvals)

# first figure
mp.rcParams['font.family'] = 'sans serif'
mp.rcParams['font.sans-serif'] = ['DejaVu Sans']
fontsize = 24
fig.tight_layout()
fig, ax = mp.subplots()
fig.set_size_inches(4.25,3)
ax.plot(xvals,yvals,c='0.1',lw=2)
ax.tick_params(labelsize=fontsize)
ax.set_title('title', fontsize=fontsize)
ax.set_xlabel('units$^{\,-1}$', fontsize=fontsize)
fig.tight_layout()
mp.show()
fig.savefig('dejavu_sans_exmaple.png', dpi=300, transparent=True, bbox_inches='tight')
