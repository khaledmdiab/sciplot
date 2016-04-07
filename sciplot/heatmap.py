import matplotlib.pyplot as plt

import utils

__author__ = 'Khaled Diab (kdiab@sfu.ca)'


def plot_heatmap(x, y, z,
                 xaxis_label=None, yaxis_label=None, mapaxis_label=None,
                 x_sci=True, y_sci=True, name=None):
    assert utils.is_list(x) == utils.is_list(y) == utils.is_list(z)

    fig, ax = plt.subplots()
    ax.hexbin(x, y, C=z, gridsize=30, cmap=plt.get_cmap('Blues'), bins=None)

    utils.set_sci_axis(ax, x_sci, y_sci)

    pcm = ax.get_children()[2]
    cb = plt.colorbar(pcm, ax=ax)
    cb.set_label(mapaxis_label)
    utils.set_axis_labels(ax, xaxis_label, yaxis_label)
    utils.finalize(ax)
    utils.save_pdf(name)