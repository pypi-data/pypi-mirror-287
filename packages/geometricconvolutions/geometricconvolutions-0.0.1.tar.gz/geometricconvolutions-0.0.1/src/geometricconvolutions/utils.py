import numpy as np
import pylab as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap
import cmastro
from geometric import TINY

# Visualize the filters.

FIGSIZE = (4, 3)
XOFF, YOFF = 0.15, -0.1

def setup_plot():
    fig = plt.figure(figsize=FIGSIZE)
    return fig

def nobox(ax):
    # ax.set_xticks([])
    # ax.set_yticks([])
    ax.axis("off")
    return

def finish_plot(ax, title, pixels, D):
    ax.set_title(title)
    if D == 2:
        ax.set_xlim(np.min(pixels)-0.55, np.max(pixels)+0.55)
        ax.set_ylim(np.min(pixels)-0.55, np.max(pixels)+0.55)
    if D == 3:
        ax.set_xlim(np.min(pixels)-0.75, np.max(pixels)+0.75)
        ax.set_ylim(np.min(pixels)-0.75, np.max(pixels)+0.75)
    ax.set_aspect("equal")
    nobox(ax)
    return

def plot_boxes(ax, xs, ys):
    for x, y in zip(xs, ys):
        ax.plot([x-0.5, x-0.5, x+0.5, x+0.5, x-0.5],
                 [y-0.5, y+0.5, y+0.5, y-0.5, y-0.5], "k-", lw=0.5, zorder=10)
    return

def fill_boxes(ax, xs, ys, ws, vmin, vmax, cmap, zorder=-100, colorbar=False, alpha=1.):
    cmx = cm.ScalarMappable(cmap=cm.get_cmap(cmap))
    cmx.set_clim(vmin, vmax)
    cs = cmx.to_rgba(ws)
    if colorbar:
        plt.colorbar(cmx, ax=ax)
    for x, y, c in zip(xs, ys, cs):
        ax.fill_between([x - 0.5, x + 0.5], [y - 0.5, y - 0.5], [y + 0.5, y + 0.5],
                             color=c, zorder=zorder, alpha=alpha)
    return

def plot_scalars(ax, M, xs, ys, ws, boxes=True, fill=True, symbols=True,
                 vmin=-2., vmax=2., cmap="cma:unph", colorbar=False):
    if boxes:
        plot_boxes(ax, xs, ys)
    if fill:
        fill_boxes(ax, xs, ys, ws, vmin, vmax, cmap, colorbar=colorbar)
    if symbols:
        height = ax.get_window_extent().height
        ss = (5 * height / M) * np.abs(ws)
        ax.scatter(xs[ws > TINY], ys[ws > TINY],
                   marker="+", c="k",
                   s=ss[ws > TINY], zorder=100)
        ax.scatter(xs[ws < -TINY], ys[ws < -TINY],
                   marker="_", c="k",
                   s=ss[ws < -TINY], zorder=100)
    return

def plot_scalar_filter(geom_filter, title, ax=None):
    assert geom_filter.k == 0
    if geom_filter.D not in [2, 3]:
        print("plot_scalar_filter(): Only works for D in [2, 3].")
        return
    if ax is None:
        fig = setup_plot()
        ax = fig.gca()
    MtotheD = geom_filter.N ** geom_filter.D
    xs, ys, zs = np.zeros(MtotheD), np.zeros(MtotheD), np.zeros(MtotheD)
    ws = np.zeros(MtotheD)
    for i, key in enumerate(geom_filter.keys()):
        ws[i] = geom_filter[key]
        if geom_filter.D == 2:
            xs[i], ys[i] = np.array(key)
        elif geom_filter.D == 3:
            xs[i], ys[i] = key[0] + XOFF * key[2], key[1] + XOFF * key[2]
    plot_scalars(ax, geom_filter.N, xs, ys, ws, vmin=-3., vmax=3.)
    finish_plot(ax, title, geom_filter.key_array(), geom_filter.D)
    return ax

def plot_vectors(ax, xs, ys, ws, boxes=True, fill=True,
                 vmin=0., vmax=2., cmap="cma:lacerta_r", scaling=0.33):
    if boxes:
        plot_boxes(ax, xs, ys)
    if fill:
        fill_boxes(ax, xs, ys, np.linalg.norm(ws, axis=-1), vmin, vmax, cmap, alpha=0.25)
    for x, y, w in zip(xs, ys, ws):
        normw = np.linalg.norm(w)
        if normw > TINY:
            ax.arrow(x - scaling * w[0], y - scaling * w[1],
                     2 * scaling * w[0], 2 * scaling * w[1],
                     length_includes_head=True,
                     head_width= 0.24 * scaling * normw,
                     head_length=0.72 * scaling * normw,
                     color="k", zorder=100)
    return

def plot_vector_filter(geom_filter, title, ax=None):
    assert geom_filter.k == 1
    if geom_filter.D not in [2, 3]:
        print("plot_vector_filter(): Only works for D in [2, 3].")
        return
    if ax is None:
        fig = setup_plot()
        ax = fig.gca()
    MtotheD = geom_filter.N ** geom_filter.D
    xs, ys, zs = np.zeros(MtotheD), np.zeros(MtotheD), np.zeros(MtotheD)
    ws = np.zeros((MtotheD, geom_filter.D))
    for i, key in enumerate(geom_filter.keys()):
        ws[i] = geom_filter[key]
        if geom_filter.D == 2:
            xs[i], ys[i] = np.array(key)
        elif geom_filter.D == 3:
            xs[i], ys[i] = key[0] + XOFF * key[2], key[1] + YOFF * key[2]
    plot_vectors(ax, xs, ys, ws, vmin=0., vmax=3.)
    finish_plot(ax, title, geom_filter.key_array(), geom_filter.D)
    return ax

Rx = np.array([[-1.0, -1.0, 1.0, 1.0, -1.0, 0.0,  1.0],
               [-1.5,  1.5, 1.5, 0.2, -0.2, 0.0, -1.5]])

def plot_one_tensor(ax, x, y, T, color="k", zorder=0, scaling=0.2):
    dx, dy = scaling * T @ Rx
    ax.plot(x + dx, y + dy, ls="-", color=color)
    return

def plot_tensors(ax, xs, ys, ws, boxes=True, fill=True,
                 vmin=0., vmax=2., cmap="cma:hesperia_r", scaling=0.33):
    if boxes:
        plot_boxes(ax, xs, ys)
    if fill:
        fill_boxes(ax, xs, ys, np.linalg.norm(ws, axis=-1), vmin, vmax, cmap, alpha=0.25)
    for x, y, w in zip(xs, ys, ws):
        normw = np.linalg.norm(w)
        if normw > TINY:
            plot_one_tensor(ax, x, y, w, color="k", zorder=100)
    return

def plot_tensor_filter(geom_filter, title, ax=None):
    assert geom_filter.k == 2, "plot_tensor_filter(): Only 2-tensors (for now)."
    if geom_filter.D not in [2, ]:
        print("plot_vector_filter(): Only works for D in [2, ].")
        return
    if ax is None:
        fig = setup_plot()
        ax = fig.gca()
    MtotheD = geom_filter.N ** geom_filter.D
    xs, ys = np.zeros(MtotheD), np.zeros(MtotheD)
    ws = np.zeros((MtotheD, geom_filter.D, geom_filter.D))
    for i, key in enumerate(geom_filter.keys()):
        ws[i] = geom_filter[key]
        if geom_filter.D == 2:
            xs[i], ys[i] = np.array(key)
        elif geom_filter.D == 3:
            xs[i], ys[i] = key[0] + XOFF * key[2], key[1] + YOFF * key[2]
    plot_tensors(ax, xs, ys, ws, vmin=0., vmax=3.)
    finish_plot(ax, title, geom_filter.key_array(), geom_filter.D)
    return ax

def plot_nothing(ax):
    ax.set_title(" ")
    nobox(ax)
    return

def plot_filters(filters, names, n):
    m = max(1, np.ceil(len(filters) / n).astype(int))
    assert len(filters) <= n * m
    bar = 8. # figure width in inches?
    fig, axes = plt.subplots(m, n, figsize = (bar, 1.15 * bar * m / n), # magic
                             squeeze=False)
    axes = axes.flatten()
    plt.subplots_adjust(left=0.001/n, right=1-0.001/n, wspace=0.2/n,
                        bottom=0.001/m, top=1-0.001/m-0.1/m, hspace=0.2/m)
    for i, (ff, name) in enumerate(zip(filters, names)):
        if ff.k == 0:
            plot_scalar_filter(ff, name, ax=axes[i])
        if ff.k == 1:
            plot_vector_filter(ff, name, ax=axes[i])
        if ff.k == 2:
            plot_tensor_filter(ff, name, ax=axes[i])
    for i in range(len(filters), n * m):
        plot_nothing(axes[i])
    return fig


# Visualize geometric images

def setup_image_plot():
    ff = plt.figure(figsize=(8, 6))
    return ff

def plot_scalar_image(image, vmin=-1., vmax=1., ax=None, colorbar=False):
    assert image.D == 2
    assert image.k == 0
    if ax is None:
        ff = setup_image_plot()
        ax = ff.gca()
    plotdata = np.array([[key[0], key[1], image[key]]
                         for key in image.keys()])
    ax.set_aspect("equal", adjustable="box")
    if vmin is None:
        vmin = np.percentile(plotdata[:, 2],  2.5)
    if vmax is None:
        vmax = np.percentile(plotdata[:, 2], 97.5)
    plot_scalars(ax, image.N, plotdata[:, 0], plotdata[:, 1], plotdata[:, 2],
                 symbols=False, vmin=vmin, vmax=vmax, colorbar=colorbar)
    image_axis(ax, plotdata)
    return ax

def image_axis(ax, plotdata):
    ax.set_xlim(np.min(plotdata[:, 0])-0.5, np.max(plotdata[:, 0])+0.5)
    ax.set_ylim(np.min(plotdata[:, 1])-0.5, np.max(plotdata[:, 1])+0.5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

def plot_vector_image(image, ax=None):
    assert image.D == 2
    assert image.k == 1
    if ax is None:
        ff = setup_image_plot()
        ax = ff.gca()
    plotdata = np.array([[key[0], key[1], image[key][0], image[key][1]]
                         for key in image.keys()])
    plot_vectors(ax, plotdata[:, 0], plotdata[:, 1], plotdata[:, 2:4],
                 boxes=True, fill=True, scaling=0.5)
    image_axis(ax, plotdata)
    return ax

def plot_image(image, **kwargs):
    assert image.D == 2
    if image.k == 0:
        plot_scalar_image(image, **kwargs)
    if image.k == 1:
        plot_vector_image(image, **kwargs)

def plot_images(images):
    """
    # Notes:
    - This takes a list of lists, each inner list is an image and
      a LaTeX expression.
    """
    nim = len(images)
    n = np.floor(np.sqrt(nim)).astype(int)
    m = np.ceil(nim / n).astype(int)
    print(len(images), n, m)
    bar = 10. # inches?
    fig, axes = plt.subplots(m, n, figsize = (bar, 0.2 * m + bar * m / n)) # magic
    axes = np.atleast_1d(axes).flatten()
    plt.subplots_adjust(left=0.001, right=0.999, wspace=0.2/n,
                        bottom=0.001, top=0.999-0.07/m, hspace=0.2/m)
    for ax, (image, latex) in zip(axes, images):
        plot_image(image, ax=ax)
        finish_plot(ax, "$" + latex + "$", image.key_array(), image.D)
    for i in range(nim, n * m):
        plot_nothing(axes[i])
    return fig
