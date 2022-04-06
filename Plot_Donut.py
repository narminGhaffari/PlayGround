# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:42:09 2021

@author: Narmin Ghaffari Laleh
"""

###############################################################################

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

###############################################################################

def PlotDonut (subsetValues, savePath, color = ['#a50026', '#fdae61'], figTitle = 'Donut Figure'):
    
    """
        Plots donut figure. The input to the function can be single list or the list of lists to plot and save the figures automatically. 
        Arguments:
            subsetValues: is a list containing the values for the donut figure.            
            example: subsetValues = [10, 20]            
            savePath: a path containing the image name to save the figure.            
            color: list of colors to fill the parts of donut figure.            
            figTitle: the title of the figure.            
        Returns:
            A donut figure saved in the specified directory.
    """     
    
    assert len(subsetValues) == len(color)   
     
    fig, ax = plt.subplots()
    mpl.rcParams['font.size'] = 10
    mypie,texts = ax.pie(subsetValues, radius=1,pctdistance = 1.4, colors = color)    
    plt.setp(mypie, width=0.5, edgecolor='white')
    ax.set_title(figTitle)
    
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")    
    for i, p in enumerate(mypie):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(str(subsetValues[i]) + '(' + str(np.round(subsetValues[i] / np.sum(subsetValues),2)*100) + '%)',
                    xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
    ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
    plt.savefig(savePath, bbox_inches='tight', dpi=500, pad_inches = 0.5)
    plt.close()

###############################################################################
 