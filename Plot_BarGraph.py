# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:13:02 2021

@author: Narmin Ghaffari Laleh
"""

###############################################################################

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

##############################################################################

def PlotBarGraph (fileAdress, columnName, savePath, figTitle = 'Bar Graph', xlabel = 'x' , ylabel = 'y', dropNA = False):
    
    """
        Plots Bar graph. The input to the function is an .xlsx or .csv format file and specified column to plot the bar graph.
        Arguments:
            fileAdress: adress to the .csv or .xlsx file.         
            columnName: name of the specified column to draw the bar graph based on its values.            
            savePath: a path containing the image name to save the figure.            
            figTitle: the title of the figure.
            xlabel: the label to use for x axis.
            ylabel: the label to use for y axis.
            dropNA: if True, then it will drop all the rows which they contain na for the specified column.
        Returns:
            a bar grpah saved in the specified directory.
    """   
    
    if '.csv' in fileAdress:
        data = pd.read_csv(fileAdress)
    else:
        data = pd.read_excel(fileAdress)
    if dropNA:    
        data.dropna(subset = [columnName], inplace = True)
    else:
        data[columnName] = data[columnName].fillna('none')
    
    uniqueValues = data[columnName].unique()
    uniqueValues_count = []
    for uniqueValue in uniqueValues:
        uniqueValues_count.append(list(data[columnName]).count(uniqueValue))
        
    fig, ax = plt.subplots(figsize = (20,20))  
    my_cmap = plt.cm.get_cmap('GnBu')
    normalized_Values = [x / max(uniqueValues_count) for x in uniqueValues_count]
    colors = my_cmap(normalized_Values)
    
    mpl.rcParams['font.size'] = 30
    plt.bar(uniqueValues, uniqueValues_count, color = colors)
    plt.xticks(fontsize = 30)
    plt.yticks(fontsize = 30)  
    plt.ylabel(ylabel, fontsize = 30)
    plt.xlabel(xlabel, fontsize = 30)
    plt.title(figTitle)
    plt.xticks(uniqueValues)   
    ax.set_aspect(1.0/ax.get_data_ratio(), adjustable = 'box')
    plt.savefig(savePath, bbox_inches='tight', dpi=500, pad_inches = 0.5)
    plt.close()
































