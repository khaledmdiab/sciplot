import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

import utils
from . import AXIS_FONT_SIZE, TICK_FONT_SIZE, ALTERNATIVE_PALETTE

__author__ = 'Khaled Diab (kdiab@sfu.ca)'


def plot_line(xs,
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
              x_lim=None,
              legend_top=True,
              ls_cycle=False,
              marker_size=0,
              x_grid=True, y_grid=True,
              fig_size=None,
              name=None, draw_arrow=False):
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
    ls_cycler = utils.get_line_styles_cycler(ls_cycle)
    ms_cycler = utils.get_marker_styles_cycler(marker_size > 0)
    if multiple_x:
        for x, y, line_label in zip(xs, ys, line_labels):
            ax.plot(x, y, label=line_label, ls=next(ls_cycler), marker=next(ms_cycler), markersize=marker_size)
    else:
        ax.plot(xs, ys, label=line_labels)
    if xticks and isinstance(xticks, list):
        x = xs[0] if multiple_x else xs
        plt.xticks(x, xticks)

    if y_lim and isinstance(y_lim, list) and len(y_lim) > 0:
        if len(y_lim) == 1:
            plt.ylim(ymin=y_lim[0])
        else:
            plt.ylim(ymin=y_lim[0])
            plt.ylim(ymax=y_lim[1])

    if x_lim and isinstance(x_lim, list) and len(x_lim) > 0:
        if len(x_lim) == 1:
            plt.xlim(xmin=x_lim[0])
        else:
            plt.xlim(xmin=x_lim[0])
            plt.xlim(xmax=x_lim[1])

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

    utils.finalize(ax, x_grid=x_grid, y_grid=y_grid)
    utils.save_fig(name)