import matplotlib.pyplot as plt
import seaborn as sns

import utils

__author__ = 'Khaled Diab (kdiab@sfu.ca)'


def plot_box(xs, ys,
             xaxis_label=None, yaxis_label=None,
             x_sci=False, y_sci=True,
             name=None):
    fig, ax = plt.subplots()
    ax = sns.boxplot(x=xs, y=ys, linewidth=1, fliersize=1)
    utils.set_sci_axis(ax, x_sci, y_sci)
    utils.set_axis_labels(ax, xaxis_label, yaxis_label)
    utils.finalize(ax)
    utils.save_pdf(name)