"""
Helper functions, snippets and parameters to make my plotting life a bit less
boilerplate-y.

References:
        https://github.com/juanshishido/tufte/blob/master/tufte.py
        https://joseph-long.com/writing/colorbars/
"""
from mpl_toolkits.axes_grid1 import make_axes_locatable
# import SCM5 as cmap

# colors
lgrey = "#efefef"
mgrey = "#5e5e5e"
dgrey = "#383838"


def plot_style(ax, plot_type:str, colors="black"):
    """Style some plots

    Args:
        ax (obj): matplotlib axes object
        plot_type (str): Options: line, scatter

    Returns:
        -
    """
    # remove ticks
    ax.tick_params(axis='both', top=False, bottom=False, left=False,
                   right=False, colors=colors, pad=5)
    if plot_type.lower() in ("line", "scatter"):
        # remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # reduce line width of spines
        ax.spines['left'].set_linewidth(0.75)
        ax.spines['bottom'].set_linewidth(0.75)


def colorbar(mappable, size="5%", pad=0.05, loc="right", kwargs={}):
    """Provides a properly sized and located colorbar to given mappable.

    Modified from: https://joseph-long.com/writing/colorbars/

    Args:
        mappable:

    Returns:
        fig.colorbar object fixed to given mappable
    """
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(loc, size=size, pad=pad)

    if loc in ["right", "left"]:
        orientation = "vertical"
    elif loc in ["top", "bottom"]:
        orientation = "horizontal"

    return fig.colorbar(mappable, cax=cax, orientation=orientation, **kwargs)



params = {
    'axes.labelsize': 6,
    'font.size': 6,
    'legend.fontsize': 10,
    'xtick.labelsize': 6,
    'ytick.labelsize': 6,
    'text.usetex': False,
    "axes.linewidth": 0.75,
    'xtick.major.size': 2,
    'xtick.major.width': 0.75,
    'ytick.major.size': 2,
    'ytick.major.width': 0.75,
}


def get_rcparams(fontsize, usetex=False, axescolor="black"):
    params = {
        'font.size': fontsize,
        'axes.labelsize': fontsize,
        'xtick.labelsize': fontsize,
        'ytick.labelsize': fontsize,


        "axes.edgecolor": axescolor,
        "xtick.color": axescolor,
        "ytick.color": axescolor,

        'text.usetex': usetex,
        "figure.subplot.bottom": 0.2,
        #"figure.autolayout": True,
    }

    return params


def get_figsize(scale:float, textwidth:int=522, ratio:float=0.62):
    """Generate appropriate figure size for LaTeX documents.

    Get textwidth via LaTeX command: \the\textwidth

    Source: http://bkanuka.com/posts/native-latex-plots/

    Args:
        scale: Percentage of textwidth to occupy (e.g. 0.5 for 50% of tw).
        textwidth: Textwidth of your document in pt's (default: 522).
            Latex command: \the\textwidth
        ratio: Aesthetic ratio of width/height (default: 0.62).

    Returns:
        (tuple) Figsize.
    """
    inches_per_pt = 1.0 / 72.27 # Convert pt to inch
    fig_width = textwidth * inches_per_pt * scale  # width in inches
    fig_height = fig_width * ratio  # height in inches
    fig_size = [fig_width, fig_height]
    return fig_size


def inch_to_mm(inch):
    return inch * 25.4


def mm_to_inch(mm):
    return mm * 0.0393701
