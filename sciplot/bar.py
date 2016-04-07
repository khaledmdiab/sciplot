import matplotlib.pyplot as plt

import utils

__author__ = 'Khaled Diab (kdiab@sfu.ca)'


def plot_bar(x, y, hue=None, hue_count=1,
             line_values=None, line_label=None, legend=True,
             xaxis_label=None, yaxis_label=None,
             xticks=None, y_lim=None,
             x_sci=True, y_sci=True,
             fig_size=None,
             y_err=None,
             name=None):
    fig, ax = plt.subplots()
    if fig_size and isinstance(fig_size, list) and len(fig_size) > 0:
        if len(fig_size) == 1:
            fig.set_figwidth(fig_size[0])
        else:
            fig.set_figwidth(fig_size[0])
            fig.set_figheight(fig_size[1])

    bar_width = 0.2
    new_x = [x_ + bar_width for x_ in x]
    ticks_x = [x_ + 0.5*bar_width for x_ in new_x]
    if y_err:
        ax.errorbar(ticks_x, y, yerr=y_err, fmt='o', ecolor='r', capthick=1, elinewidth=1)
    plt.bar(new_x, y, width=bar_width)

    if line_values and utils.is_list(line_values):
        x_set = set(x)
        if len(line_values) == len(x_set):
            if line_label:
                ax.plot(ax.get_xticks(), line_values, label=line_label)
                hue_count += 1
            else:
                ax.plot(ax.get_xticks(), line_values)
    if xticks and isinstance(xticks, list):
        plt.xticks(ticks_x, xticks)
    if y_lim and isinstance(y_lim, list) and len(y_lim) > 0:
        if len(y_lim) == 1:
            plt.ylim(ymin=y_lim[0])
        else:
            plt.ylim(ymin=y_lim[0])
            plt.ylim(ymax=y_lim[1])
    if legend:
        utils.set_legend(ncol=hue_count)
    utils.set_sci_axis(ax, x_sci, y_sci)
    utils.set_axis_labels(ax, xaxis_label, yaxis_label)
    utils.finalize(ax, x_grid=False)
    utils.save_fig(name)


def plot_two_bars(ys, labels,
                  legend=True,
                  xaxis_label=None,
                  yaxis_label=None,
                  xticks=None, y_lim=None,
                  x_sci=True, y_sci=True,
                  fig_size=None,
                  name=None):
    fig, ax = plt.subplots()
    if fig_size and isinstance(fig_size, list) and len(fig_size) > 0:
        if len(fig_size) == 1:
            fig.set_figwidth(fig_size[0])
        else:
            fig.set_figwidth(fig_size[0])
            fig.set_figheight(fig_size[1])

    bar_width = 0.2
    x = range(len(ys))
    new_x1 = [x_ for x_ in x]
    new_x2 = [x_ + bar_width for x_ in x]
    rects1 = ax.bar(new_x1, ys[0], width=bar_width, color='b')
    rects2 = ax.bar(new_x2, ys[1], width=bar_width)

    if xticks and isinstance(xticks, list):
        plt.xticks([x_ + bar_width for x_ in new_x1], xticks)
    if y_lim and isinstance(y_lim, list) and len(y_lim) > 0:
        if len(y_lim) == 1:
            plt.ylim(ymin=y_lim[0])
        else:
            plt.ylim(ymin=y_lim[0])
            plt.ylim(ymax=y_lim[1])
    if legend:
        ax.legend((rects1[0], rects2[0]), (labels[0], labels[1]),
                  fontsize=28, frameon=False,
                  bbox_to_anchor=(0, 0.95, 1.2, .10), handlelength=0.5, handletextpad=0.2,
                  loc=3, ncol=2, mode="expand",
                  borderaxespad=0.)
    utils.set_sci_axis(ax, x_sci, y_sci)
    utils.set_axis_labels(ax, xaxis_label, yaxis_label)
    utils.finalize(ax, x_grid=False)
    utils.save_fig(name)