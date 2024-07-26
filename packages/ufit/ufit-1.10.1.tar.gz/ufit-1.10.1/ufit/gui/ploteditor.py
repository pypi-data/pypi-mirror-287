#  -*- coding: utf-8 -*-
# *****************************************************************************
# ufit, a universal scattering fitting suite
#
# Copyright (c) 2013-2024, Georg Brandl and contributors.  All rights reserved.
# Licensed under a 2-clause BSD license, see LICENSE.
# *****************************************************************************

# Originally matplotlib.backends.qt_editor.figureoptions
# Copyright © 2009 Pierre Raybaut
# Licensed under the terms of the MIT License
# see the mpl licenses directory for a copy of the license

"""Module that provides a GUI-based editor for matplotlib's figure options"""

import os.path as osp
import re

import matplotlib
from matplotlib import cm, colors as mcolors, image as mimage, markers

try:
    from matplotlib.backends.qt_editor import formlayout
except ImportError:  # MPL 3.3+
    import matplotlib.backends.qt_editor._formlayout as formlayout

from matplotlib.backends.qt_compat import QtGui


def get_icon(name):
    basedir = osp.join(matplotlib.rcParams['datapath'], 'images')
    return QtGui.QIcon(osp.join(basedir, name))


LINESTYLES = {'-': 'Solid',
              '--': 'Dashed',
              '-.': 'DashDot',
              ':': 'Dotted',
              'None': 'None',
              }

DRAWSTYLES = {
    'default': 'Default',
    'steps-pre': 'Steps (Pre)', 'steps': 'Steps (Pre)',
    'steps-mid': 'Steps (Mid)',
    'steps-post': 'Steps (Post)'}

MARKERS = markers.MarkerStyle.markers


def figure_edit(axes, parent=None):
    """Edit matplotlib figure options"""
    sep = (None, None)  # separator

    # Get / General
    # Cast to builtin floats as they have nicer reprs.
    xmin, xmax = map(float, axes.get_xlim())
    ymin, ymax = map(float, axes.get_ylim())
    general = [('Title', axes.get_title()),
               ('Title size', matplotlib.rcParams['axes.titlesize']),
               ('Label size', matplotlib.rcParams['axes.labelsize']),
               ('Legend size', matplotlib.rcParams['legend.fontsize']),
               sep,
               sep,
               (None, "<b>X-Axis</b>"),
               ('Left', xmin), ('Right', xmax),
               ('Label', axes.get_xlabel()),
               ('Scale', [axes.get_xscale(), 'linear', 'log', 'logit']),
               ('Tick label size', matplotlib.rcParams['xtick.labelsize']),
               sep,
               (None, "<b>Y-Axis</b>"),
               ('Bottom', ymin), ('Top', ymax),
               ('Label', axes.get_ylabel()),
               ('Scale', [axes.get_yscale(), 'linear', 'log', 'logit']),
               ('Tick label size', matplotlib.rcParams['ytick.labelsize']),
               sep,
               ('(Re-)Generate automatic legend', False),
               ]

    # Save the unit data
    xconverter = axes.xaxis.converter
    yconverter = axes.yaxis.converter
    xunits = axes.xaxis.get_units()
    yunits = axes.yaxis.get_units()

    # Sorting for default labels (_lineXXX, _imageXXX).
    def cmp_key(label):
        match = re.match(r"(_line|_image)(\d+)", label)
        if match:
            return match.group(1), int(match.group(2))
        return label, 0

    # Get / Curves
    linedict = {}
    lines = set()
    unnamed = 0

    # add containered lines by legend name (errorbar)
    for container in axes.containers:
        label = container.get_label()
        if label == '_nolegend_':
            unnamed += 1
            label = 'unnamed #%d' % unnamed
        for obj in container:
            if isinstance(obj, matplotlib.lines.Line2D):
                linedict[label] = obj
                lines.add(obj)
                break

    # add normal lines
    for line in axes.get_lines():
        if line in lines:
            continue
        label = line.get_label()
        if label == '_nolegend_':
            unnamed += 1
            label = 'unnamed #%d' % unnamed
        linedict[label] = line

    curves = []

    def prepare_data(d, init):
        """Prepare entry for FormLayout.

        `d` is a mapping of shorthands to style names (a single style may
        have multiple shorthands, in particular the shorthands `None`,
        `"None"`, `"none"` and `""` are synonyms); `init` is one shorthand
        of the initial style.

        This function returns an list suitable for initializing a
        FormLayout combobox, namely `[initial_name, (shorthand,
        style_name), (shorthand, style_name), ...]`.
        """
        # Drop duplicate shorthands from dict (by overwriting them during
        # the dict comprehension).
        name2short = {name: short for short, name in d.items()}
        # Convert back to {shorthand: name}.
        short2name = {short: name for name, short in name2short.items()}
        # Find the kept shorthand for the style specified by init.
        canonical_init = name2short[d[init]]
        # Sort by representation and prepend the initial value.
        return ([canonical_init] +
                sorted(short2name.items(),
                       key=lambda short_and_name: short_and_name[1]))

    curvelabels = sorted(linedict, key=cmp_key)
    for label in curvelabels:
        line = linedict[label]
        color = mcolors.to_hex(
            mcolors.to_rgba(line.get_color(), line.get_alpha()),
            keep_alpha=True)
        ec = mcolors.to_hex(
            mcolors.to_rgba(line.get_markeredgecolor(), line.get_alpha()),
            keep_alpha=True)
        fc = mcolors.to_hex(
            mcolors.to_rgba(line.get_markerfacecolor(), line.get_alpha()),
            keep_alpha=True)
        curvedata = [
            ('Label', label),
            sep,
            (None, '<b>Line</b>'),
            ('Line style', prepare_data(LINESTYLES, line.get_linestyle())),
            ('Draw style', prepare_data(DRAWSTYLES, line.get_drawstyle())),
            ('Width', line.get_linewidth()),
            ('Color (RGBA)', color),
            sep,
            (None, '<b>Marker</b>'),
            ('Style', prepare_data(MARKERS, line.get_marker())),
            ('Size', line.get_markersize()),
            ('Face color (RGBA)', fc),
            ('Edge color (RGBA)', ec)]
        curves.append([curvedata, label, ""])
    # Is there a curve displayed?
    has_curve = bool(curves)

    # Get / Images
    imagedict = {}
    for image in axes.get_images():
        label = image.get_label()
        if label == '_nolegend_':
            continue
        imagedict[label] = image
    imagelabels = sorted(imagedict, key=cmp_key)
    images = []
    cmaps = [(cmap, name) for name, cmap in sorted(cm.cmap_d.items())]
    for label in imagelabels:
        image = imagedict[label]
        cmap = image.get_cmap()
        if cmap not in cm.cmap_d.values():
            cmaps = [(cmap, cmap.name)] + cmaps
        low, high = image.get_clim()
        imagedata = [
            ('Label', label),
            ('Colormap', [cmap.name] + cmaps),
            ('Min. value', low),
            ('Max. value', high),
            ('Interpolation',
             [image.get_interpolation()]
             + [(name, name) for name in sorted(mimage.interpolations_names)])]
        images.append([imagedata, label, ""])
    # Is there an image displayed?
    has_image = bool(images)

    datalist = [(general, "Axes", "")]
    if curves:
        datalist.append((curves, "Curves", ""))
    if images:
        datalist.append((images, "Images", ""))

    def apply_callback(data):
        """This function will be called to apply changes"""
        orig_xlim = axes.get_xlim()
        orig_ylim = axes.get_ylim()

        general = data.pop(0)
        curves = data.pop(0) if has_curve else []
        images = data.pop(0) if has_image else []
        if data:
            raise ValueError("Unexpected field")

        # Set / General
        (title, titlesize, labelsize, legendsize,
         xmin, xmax, xlabel, xscale, xticksize,
         ymin, ymax, ylabel, yscale, yticksize,
         generate_legend) = general

        if axes.get_xscale() != xscale:
            axes.set_xscale(xscale)
        if axes.get_yscale() != yscale:
            axes.set_yscale(yscale)

        axes.set_title(title)
        axes.set_xlim(xmin, xmax)
        axes.set_xlabel(xlabel)
        axes.set_ylim(ymin, ymax)
        axes.set_ylabel(ylabel)

        orig_sizes = (matplotlib.rcParams['axes.titlesize'],
                      matplotlib.rcParams['axes.labelsize'],
                      matplotlib.rcParams['legend.fontsize'],
                      matplotlib.rcParams['xtick.labelsize'],
                      matplotlib.rcParams['ytick.labelsize'])
        new_sizes = (titlesize, labelsize, legendsize, xticksize, yticksize)

        # Restore font data
        matplotlib.rcParams['axes.titlesize'] = titlesize
        matplotlib.rcParams['axes.labelsize'] = labelsize
        matplotlib.rcParams['legend.fontsize'] = legendsize
        matplotlib.rcParams['xtick.labelsize'] = xticksize
        matplotlib.rcParams['ytick.labelsize'] = yticksize

        # Restore the unit data
        axes.xaxis.converter = xconverter
        axes.yaxis.converter = yconverter
        axes.xaxis.set_units(xunits)
        axes.yaxis.set_units(yunits)
        axes.xaxis._update_axisinfo()
        axes.yaxis._update_axisinfo()

        # Set / Curves
        for index, curve in enumerate(curves):
            line = linedict[curvelabels[index]]
            (label, linestyle, drawstyle, linewidth, color, marker, markersize,
             markerfacecolor, markeredgecolor) = curve
            line.set_label(label)
            line.set_linestyle(linestyle)
            line.set_drawstyle(drawstyle)
            line.set_linewidth(linewidth)
            rgba = mcolors.to_rgba(color)
            line.set_alpha(None)
            line.set_color(rgba)
            if marker != 'none':
                line.set_marker(marker)
                line.set_markersize(markersize)
                line.set_markerfacecolor(markerfacecolor)
                line.set_markeredgecolor(markeredgecolor)

        # Set / Images
        for index, image_settings in enumerate(images):
            image = imagedict[imagelabels[index]]
            label, cmap, low, high, interpolation = image_settings
            image.set_label(label)
            image.set_cmap(cm.get_cmap(cmap))
            image.set_clim(*sorted([low, high]))
            image.set_interpolation(interpolation)

        # re-generate legend, if checkbox is checked
        if generate_legend:
            draggable = None
            ncol = 1
            if axes.legend_ is not None:
                old_legend = axes.get_legend()
                draggable = old_legend._draggable is not None
                ncol = old_legend._ncol
            new_legend = axes.legend(ncol=ncol)
            if new_legend:
                new_legend.draggable(draggable)

        # Redraw
        figure = axes.get_figure()
        figure.canvas.draw()
        if not (axes.get_xlim() == orig_xlim and axes.get_ylim() == orig_ylim):
            figure.canvas.toolbar.push_current()
        if orig_sizes != new_sizes:
            figure.canvas.ufit_replot()
            figure.tight_layout(pad=2)

    data = formlayout.fedit(datalist, title="Figure options", parent=parent,
                            icon=get_icon('qt4_editor_options.svg'),
                            apply=apply_callback)
    if data is not None:
        apply_callback(data)
