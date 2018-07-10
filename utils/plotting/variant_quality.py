#! /usr/bin/env python3

def variant_metric_hist(metric, ax, yax_scale=1e6, bins=30, title="", xlabel="", ylabel=""):
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.hist(metric, bins, alpha=0.5)
    locs = ax.get_yticks()
    labels = [str(round(x/yax_scale, 2)) for x in locs]
    ax.set_yticklabels(labels)

    return ax

def plot_windowed_variant_density(pos, window_size, ax, title=None):
    
    # setup windows
    bins = np.arange(0, pos.max(), window_size)
    
    # use window midpoints as x coordinate
    x = (bins[1:] + bins[:-1])/2
    
    # compute variant density in each window
    h, _ = np.histogram(pos, bins=bins)
    y = h / window_size
    
    # plot
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(x, y)
    ax.set_xlabel('Chromosome position (bp)')
    ax.set_ylabel('Variant density (bp$^{-1}$)')
    if title:
        ax.set_title(title)
    return y.mean()

