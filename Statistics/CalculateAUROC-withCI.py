# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:09:48 2021

@author: nghaffarilal
"""
import pandas as pd
from sklearn import metrics
import numpy as np

def CalculateAUCwithConfidenceInterval(fileAdress, labelDictionary, yTrueColumnLabel, randomState = 666): 

    """
        CalculateAUCwithConfidenceInterval. The input to the function is an .xlsx or .csv format file and specified column to calculate the area under 
        the receiver operative curve with 1000x bootstrapping confidence Interval.
        
        Arguments:
            fileAdress: adress to the .csv or .xlsx file.     
            labelDictionary: a dictionary indicating the labels and their corresponding string name. As an example : {0 : 'positive', 1 : 'negative'}
            yTrueColumnLabel: name of the specified column indicating the y True column.l
        Returns:
            prints the AUC with the high and lower confidence intervals. 
    """ 
    
    if '.csv' in fileAdress:
        data = pd.read_csv(fileAdress)
    else:
        data = pd.read_excel(fileAdress)
                 
    y_true = list(data[yTrueColumnLabel])
    keys = list(labelDictionary.keys())    
    for key in keys:
        y_pred = data[key]
        fpr, tpr, thresholds = metrics.roc_curve(y_true, y_pred, pos_label = labelDictionary[key])
        print('TOTAL AUC FOR target {} IN THIS DATASET IS : {} '.format(key, np.round(metrics.auc(fpr, tpr), 3)))
        auc_values = []
        nsamples = 1000
        rng = np.random.RandomState(randomState)
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        for i in range(nsamples):
            indices = rng.randint(0, len(y_pred), len(y_pred))
            if len(np.unique(y_pred[indices])) < 2 or np.sum(y_true[indices]) == 0:
                continue    
            fpr, tpr, thresholds = metrics.roc_curve(y_true[indices], y_pred[indices], pos_label = labelDictionary[key])
            auc_values.append(metrics.auc(fpr, tpr))
        
        auc_values = np.array(auc_values)
        auc_values.sort()         
        print('Lower Confidebnce Interval For Target {}: {}'.format(key, np.round(auc_values[int(0.025 * len(auc_values))], 3)))        
        print('Higher Confidebnce Interval For Target {} : {}'.format(key, np.round(auc_values[int(0.975 * len(auc_values))], 3)))
        print('*' * 30)

