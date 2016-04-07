from . import LINE_STYLES
import os
from itertools import cycle
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import seaborn as sns

__author__ = 'Khaled Diab (kdiab@sfu.ca)'


def is_list_of_list(ls):
    return all(is_list(elem) for elem in ls)


def is_list(ls):
    return isinstance(ls, list) or isinstance(ls, np.ndarray)


def set_sci_axis(ax, x_sci, y_sci):
    if x_sci and isinstance(ax.xaxis.get_major_formatter(), ScalarFormatter):
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    if y_sci and isinstance(ax.yaxis.get_major_formatter(), ScalarFormatter):
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))


def set_axis_labels(ax, x_label, y_label):
    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)


def set_legend(top=True, ncol=1):
    if top:
        plt.legend(fontsize=28, frameon=False,
                   bbox_to_anchor=(0., .95, 1., .10),
                   loc=3, ncol=ncol, mode="expand",
                   borderaxespad=0.)
    else:
        plt.legend(fontsize=28, fancybox=True, frameon=True)


def finalize(ax, tight=True, despine_left=False, despine_bottom=False, despine_right=True, despine_top=True,
             x_grid=True, y_grid=True):

    sns.despine(top=despine_top, right=despine_right, left=despine_left, bottom=despine_bottom)

    if x_grid:
        ax.xaxis.grid()

    if y_grid:
        ax.yaxis.grid()

    if tight:
        plt.tight_layout()


def get_ls(ls_cycle):
    if LINE_STYLES and is_list(LINE_STYLES) and len(LINE_STYLES) > 0:
        return LINE_STYLES if ls_cycle else LINE_STYLES[0]
    else:
        return ['-']


def get_marker_style(cycle):
    MARKERSTYLES = ['o', 'v', '^', '<', '>']
    if MARKERSTYLES and is_list(MARKERSTYLES) and len(MARKERSTYLES) > 0:
        return MARKERSTYLES if cycle else MARKERSTYLES[0]
    else:
        return ['1']


def get_line_styles_cycler(ls_cycle):
    return cycle(get_ls(ls_cycle))


def get_marker_styles_cycler(ls_cycle):
    return cycle(get_marker_style(ls_cycle))


def save_fig(full_path):
    if full_path:
        filename, file_extension = os.path.splitext(full_path)
        if '.' in file_extension:
            file_extension = file_extension[1:]
        plt.savefig(full_path, format=file_extension)