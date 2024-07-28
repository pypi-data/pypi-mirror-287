import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import Normalize
import matplotlib as mpl
import beautifulplots.beautifulplots as bp


def scatterplot(df, x, y, ax=None, test_mode=False, **kwargs):
    """Scatterplot function.
    The underlying barplot is ased on the Seaborn with additions, such as data labels,
    and improved default parameters. Refer to beautifulplots plot_defaults for a complete list of options.

    Args:
        df (DataFrame): The input DataFrame containing colums corresponding to bar_plot values ("bar_values") and column names (see examples in documentation)

        x: Dataframe column corresponding to the  x-axis

        y: Column or list of columns corresponding to the y-axis

        ax (axis): matplotlib axis (optional), default = None. If axis is None, then create a matplolib figure, axis to host the barplot

        color: default = None (Matplotlib default). Matplotlib compatabile color name as text or RGB values, for example, color = [51/235,125/235,183/235].

        palette: Matplotlib compatible color palette name, for example, "tab20"

        hue: Name of hue dimension variable (i.e., DataFrame column name)

        additional options:  see beautifulplot.plot_defaults for additional input variables.

    Returns:
        returns True if processing completes succesfully (without errors).
    """

    # hline_label=None, vline_label=None,
    # annotate
    # get default plot option dictionary
    plot_options = bp.get_kwargs(**kwargs)

    plot_options.update({"y_lims": (0.9, 100)})
    plot_options.update({"x_lims": (-0.05, 1.8)})

    hue = plot_options["hue"]
    errorbar = plot_options["errorbar"]
    alpha = plot_options["alpha"]
    hue = plot_options["hue"]
    palette = plot_options["palette"]
    color = plot_options["color"]
    marker = plot_options["marker"]
    markers = plot_options["markers"]
    style = plot_options["style"]
    ycurrency = plot_options["y_currency"]
    ylabel = plot_options["y_axis_label"]
    yaxisformat = plot_options["y_axis_format"]

    # make sure y and marker are iterable
    if not isinstance(y, list):
        y = [y]
    if marker == None:
        if not isinstance(marker, list):
            marker = len(y) * [marker]
    else:
        if not isinstance(marker, list):
            marker = [marker]

    if ax == None:
        mpl.rcParams.update(mpl.rcParamsDefault)  # reset plot/figure parameters
        plt.style.use(plot_options["pltstyle"])
        fig, _ax = plt.subplots(nrows=1, ncols=1, figsize=plot_options["figsize"])
    else:
        _ax = ax

    for _y, _marker in zip(y, marker):

        label = _y if hue == None else None

        gkwargs = {}
        gkwargs["data"] = df
        gkwargs["x"] = x
        gkwargs["y"] = _y
        gkwargs["ax"] = _ax
        gkwargs["style"] = style

        if label:
            plot_options["label"] = label
        if plot_options["palette"]:
            gkwargs["palette"] = plot_options["palette"]
        if plot_options["color"]:
            gkwargs["color"] = plot_options["color"]
        if _marker:
            gkwargs["marker"] = _marker
        if hue:
            gkwargs["hue"] = hue
        if markers:
            gkwargs["markers"] = markers
        if alpha:
            gkwargs["alpaha"] = alpha

        g = sns.scatterplot(**gkwargs)

    bp.set_axisparams(plot_options, _ax, g)
    bp.set_yaxis_format(_ax, yaxisformat, ycurrency)

    # plot show if easy lineplot created the figure
    if ax == None and test_mode == False:
        plt.show()  # if simpl_plot created the figure then plt.show()

    return None
