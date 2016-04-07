import matplotlib.pyplot as plt
import seaborn as sns

__author__ = 'Khaled Diab (kdiab@sfu.ca)'

# Line Styles
DEFAULT_LINE_WIDTH = 5
ALTERNATIVE_LINE_WIDTH = 5
LINE_STYLES = ['-', '--', '-.', ':']

# Font
TEX_ENABLED = True
TICK_FONT_SIZE = 30
AXIS_FONT_SIZE = 30
LEGEND_FONT_SIZE = 30

# COLOR
DEFAULT_PALETTE = sns.color_palette(palette='muted')
ALTERNATIVE_PALETTE = sns.color_palette(palette='pastel')
BAR_PALETTE = sns.cubehelix_palette(5, start=0.3, rot=-.5)

DEFAULT_RC = {'lines.linewidth': DEFAULT_LINE_WIDTH,
              'axes.labelsize': AXIS_FONT_SIZE,
              'xtick.labelsize': TICK_FONT_SIZE,
              'ytick.labelsize': TICK_FONT_SIZE,
              'legend.fontsize': LEGEND_FONT_SIZE}

ALTERNATIVE_RC = {'lines.linewidth': ALTERNATIVE_LINE_WIDTH,
                  'axes.labelsize': AXIS_FONT_SIZE,
                  'xtick.labelsize': TICK_FONT_SIZE,
                  'ytick.labelsize': TICK_FONT_SIZE,
                  'legend.fontsize': LEGEND_FONT_SIZE}

sns.set_context(context='paper', rc=DEFAULT_RC)
sns.set_style(style='ticks')
sns.set_palette(DEFAULT_PALETTE)
plt.rc('text', usetex=TEX_ENABLED)
plt.rc('legend', handlelength=1., handletextpad=0.)
