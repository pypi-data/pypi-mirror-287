#  -*- coding: utf-8 -*-
# *****************************************************************************
# ufit, a universal scattering fitting suite
#
# Copyright (c) 2013-2024, Georg Brandl and contributors.  All rights reserved.
# Licensed under a 2-clause BSD license, see LICENSE.
# *****************************************************************************

from enum import Enum

import numpy as np

_marker_size = 10
_bz_width = 0.5
_label_size = 18
inva = np.array([-1, 1])


class PlaneType(Enum):
    HHLPLANE = 0
    H0LPLANE = 1
    HK0PLANE = 2

    def GetVector(inp):  # pylint: disable=no-self-argument
        if inp == PlaneType.H0LPLANE:
            return (0, 1, 0)
        if inp == PlaneType.HK0PLANE:
            return (0, 0, 1)
        if inp == PlaneType.HHLPLANE:
            return (1, -1, 0)
        raise NotImplementedError


class BZCreator:
    """ Experimantal version of the brillouin zone plotter """
    # Only BCT2 structure is supported now

    def __init__(self, gpts, a, c, plane):
        # just for bct2 - body centered tetragonal 2 brilluin zone yet
        if c < a:
            raise NotImplementedError
        # sp:
        self.a = a
        self.c = c

        self.sps = {
            "P":      [0.5,                     0.5,                     0.5],
            "Y1":     [(-a**2 + c**2)/(2*c**2), (-a**2 + c**2)/(2*c**2), 1.0],
            "Y":      [(a**2 + c**2)/(2*c**2),  (-a**2 + c**2)/(2*c**2), 0],
            "X":      [0.5,                     0.5,                     0],
            "Z":      [0,                       0,                       1.0],
            "Sigma":  [(a**2 + c**2)/(2*c**2),  0,                       0],
            "Sigma1": [(-a**2 + c**2)/(2*c**2), 0,                       1.0],
            "N":      [0.5,                     0,                       0.5],
            # "Gamma": [0, 0, 0],
        }
        self.gpts = gpts
        if plane[0] == plane[1] == 0:
            self.pt = PlaneType.HK0PLANE
        elif (plane[2] == 0) and (plane[0] == 0 or plane[1] == 0):
            self.pt = PlaneType.H0LPLANE
        elif (plane[2] == 0) and (abs(plane[1]) == abs(plane[0])):
            self.pt = PlaneType.HHLPLANE
        else:
            raise NotImplementedError

    def doPlot(self, plt, alph=0.1, show_labels=True, lw=_bz_width):

        plt.plot(self.gpts[:, 0], self.gpts[:, 1], 'o',
                 markersize=_marker_size + 3, alpha=alph)

        # pts
        pts = self.getPts()
        for p in pts:
            plt.plot(p[:, 0], p[:, 1], 'o',
                     markersize=_marker_size, alpha=alph)

        # lines
        pts = self.getLines()
        for p in pts:
            plt.plot(p[:, 0], p[:, 1], 'k--', linewidth=lw)

        # misc
        if self.pt == PlaneType.HK0PLANE:
            plt.set_aspect(1)
            plt.set_xlabel('h (r.l.u.)', fontsize=_label_size)
            plt.set_ylabel('k (r.l.u.)', fontsize=_label_size)
            if show_labels:
                plt.text(0.07, -0.05, r'$\Gamma$', fontsize=_label_size)
                plt.text(0.65, -0.05, r'$\Sigma$', fontsize=_label_size)
                plt.text(0.65,  0.27, r'Y', fontsize=_label_size)
                plt.text(0.55,  0.55, r'X', fontsize=_label_size)
        elif self.pt == PlaneType.H0LPLANE:
            plt.set_aspect(self.a/self.c)
            plt.set_xlabel('h (r.l.u.)', fontsize=_label_size)
            plt.set_ylabel('l (r.l.u.)', fontsize=_label_size)
            if show_labels:
                plt.text(0.07, -0.08, r'$\Gamma$', fontsize=_label_size)
                plt.text(0.45, -0.08, r'$\Sigma$', fontsize=_label_size)
                plt.text(0.57,  0.40, r'N', fontsize=_label_size)
                plt.text(0.07,  1.07, r'Z', fontsize=_label_size)
        elif self.pt == PlaneType.HHLPLANE:
            plt.set_aspect(self.a/self.c*np.sqrt(2))
            plt.set_xlabel('h (r.l.u.)', fontsize=_label_size)
            plt.set_ylabel('l (r.l.u.)', fontsize=_label_size)
            # if show_labels:
            #     plt.text(0.07, -0.08, r'$\Gamma$', fontsize=_label_size)
            #     plt.text(0.45, -0.08, r'$\Sigma$', fontsize=_label_size)
            #     plt.text(0.57,  0.40, r'N', fontsize=_label_size)
            #     plt.text(0.07,  1.07, r'Z', fontsize=_label_size)

    def getPts(self):

        retpts = []
        for sp in self.sps.values():
            # if (self.pt == PlaneType.H0LPLANE and sp[self.cz] == 0):  # only points in this plane
            if np.dot(PlaneType.GetVector(self.pt), sp) == 0:
                if self.pt in (PlaneType.H0LPLANE, PlaneType.HHLPLANE):
                    vec = [sp[0], sp[2]]
                elif self.pt == PlaneType.HK0PLANE:
                    vec = sp[:2]
                else:
                    raise NotImplementedError

                pts = []
                # print name, sp
                for gpt in self.gpts:
                    pts.append(gpt + vec)
                    pts.append(gpt - vec)
                    pts.append(gpt + vec * inva)
                    pts.append(gpt - vec * inva)
                    if self.pt == PlaneType.HK0PLANE:  # tetragonal
                        vec.reverse()
                        pts.append(gpt + vec)
                        pts.append(gpt - vec)
                        pts.append(gpt + vec * inva)
                        pts.append(gpt - vec * inva)
                retpts.append(np.array(pts))
        return retpts

    def getLines(self):

        def additem(col, main, v):
            col.append([main + v, np.arctan2(*(v))])

        retpts = []
        for gpt in self.gpts:
            pts = []
            for sp in self.sps.values():
                if np.dot(PlaneType.GetVector(self.pt), sp) == 0:  # only points in this plane
                    if self.pt in (PlaneType.H0LPLANE, PlaneType.HHLPLANE):
                        vec = [sp[0], sp[2]]
                    elif self.pt == PlaneType.HK0PLANE:
                        vec = sp[:2]
                    else:
                        raise NotImplementedError

                    additem(pts, gpt, vec)
                    vec[:] = [-x for x in vec]
                    additem(pts, gpt, vec)
                    vec = list(vec * inva)
                    additem(pts, gpt, vec)
                    vec[:] = [-x for x in vec]
                    additem(pts, gpt, vec)
                    if self.pt == PlaneType.HK0PLANE:  # tetragonal
                        vec.reverse()
                        additem(pts, gpt, vec)
                        vec[:] = [-x for x in vec]
                        additem(pts, gpt, vec)
                        vec = list(vec * inva)
                        additem(pts, gpt, vec)
                        vec[:] = [-x for x in vec]
                        additem(pts, gpt, vec)
            # pts.sort()
            # ptdict = {}
            # for pt in pts:
            #     ptdict[pt[1]] = pt[0]
            pts = sorted(pts, key=lambda s: s[1])

            pts = np.array(pts)[:, 0]
            pts = np.array(list(pts))
            retpts.append(pts)
        return retpts
