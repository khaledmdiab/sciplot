import numpy as np

import matplotlib.cm as cm
import matplotlib.pyplot as plt

import utils
from . import ALTERNATIVE_PALETTE

__author__ = 'Khaled Diab (kdiab@sfu.ca)'


def plot_scatter(xs,
                 ys,
                 line_labels=None,
                 xaxis_label=None,
                 yaxis_label=None,
                 xticks=None,
                 vlines=None,
                 vlines_kwargs=None,
                 hlines=None,
                 hlines_kwargs=None,
                 x_sci=True,
                 y_sci=True,
                 y_lim=None,
                 legend_top=True,
                 fig_size=None,
                 ls_cycle=False,
                 name=None):
    multiple_x = utils.is_list_of_list(xs)
    multiple_y = utils.is_list_of_list(ys)
    multiple_line_label = utils.is_list(line_labels)
    assert multiple_x == multiple_y == multiple_line_label

    fig, ax = plt.subplots()
    if fig_size and isinstance(fig_size, list) and len(fig_size) > 0:
        if len(fig_size) == 1:
            fig.set_figwidth(fig_size[0])
        else:
            fig.set_figwidth(fig_size[0])
            fig.set_figheight(fig_size[1])
    colors = iter(cm.rainbow(np.linspace(0, 1, len(ys))))
    if multiple_x:
        for x, y, line_label in zip(xs, ys, line_labels):
            ax.scatter(x, y, label=line_label, c=next(colors))
    else:
        ax.scatter(xs, ys, label=line_labels, c=next(colors))
    if xticks and isinstance(xticks, list):
        x = xs[0] if multiple_x else xs
        plt.xticks(x, xticks)
    if y_lim and isinstance(y_lim, list) and len(y_lim) > 0:
        if len(y_lim) == 1:
            plt.ylim(ymin=y_lim[0])
        else:
            plt.ylim(ymin=y_lim[0])
            plt.ylim(ymax=y_lim[1])
    plt.xlim(xmin=0)
    ncol = len(xs) if multiple_x else 1
    utils.set_legend(legend_top, ncol)
    utils.set_sci_axis(ax, x_sci, y_sci)
    utils.set_axis_labels(ax, xaxis_label, yaxis_label)

    vlines = vlines or []
    for xvline in vlines:
        with ALTERNATIVE_PALETTE:
            plt.axvline(x=xvline, **vlines_kwargs)

    hlines = hlines or []
    for yhline in hlines:
        with ALTERNATIVE_PALETTE:
            plt.axhline(y=yhline, **hlines_kwargs)

    utils.finalize(ax)
    utils.save_fig(name)
