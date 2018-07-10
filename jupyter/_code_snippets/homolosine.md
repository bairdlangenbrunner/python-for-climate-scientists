    import matplotlib.pyplot as mp
    import cartopy
	
    fig, ax = mp.subplots(1,1,subplot_kw={'projection':cartopy.crs.InterruptedGoodeHomolosine()})
	fig.set_size_inches(13,13)

    ax.coastlines(resolution='110m', lw=1.5, color='#002b36')
	ax.outline_patch.set_edgecolor('#002b36')
	ax.outline_patch.set_linewidth(1.5)

    ax.background_patch.set_visible(False)

    fig.tight_layout()
	fig.savefig('homolosine_map.svg', transparent=True, bbox_inches='tight')