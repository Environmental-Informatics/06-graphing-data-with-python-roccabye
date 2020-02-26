#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab Assignment06 - Graphing Data with Python
Author - Alka Tiwari (tiwari13)
Github username: roccabye
Description:
    This program reads the data file(.txt) from "Input" folder (two have been provided) 
    and generate summary figures (.pdf) for that file in separate "output" folder.
The code in a folder "sourcecode".
"""
 # Import necessary libraries
import os
import pathlib
import numpy as np
import matplotlib.pyplot as plt

#The directory where Input text file is stored.
pathname = "/home/tiwari13/ABE65100/06-graphing-data-with-python-roccabye/Input"

# Using glob() to identify the .txt files in the input directory folder and do further plotting.
for file in pathlib.Path(pathname).glob('*.txt'):
    base = os.path.basename(file)                                             #Extracting the basename from the input file
    base = os.path.splitext(base)[0]                                          #Extracting the base from the input file i.e. without the extension
    
    #Using NumPy command genfromtxt() and use the first line as a header to define the name of arrays that are generated.
    data = np.genfromtxt(file,names = True )                                  
    
    # set figure size and facecolor to cyan
    plt.figure(figsize=(10,10), facecolor='c')
     
    # The title of the figure.
    plt.suptitle(base)	
	
    # Top Plot (1)
    plt.subplot(311)                                                          # reserving space with subplot
    plt.plot(data['Year'],data['Mean'],'k')                                   # plotting the mean of daily streamflow using lines of black (k)
    plt.plot(data['Year'],data['Max'],'r')                                    # plotting the maximum of daily streamflow using lines of red (r)
    plt.plot(data['Year'],data['Min'],'b')                                    # plotting the minimum of daily streamflow using lines of blue (b)
    plt.legend(['Mean','Max','Min'],bbox_to_anchor = (0.,1.02,1.,0.102),loc="upper right", mode="expand", borderaxespad=0, ncol=3)	
    plt.xlabel('Year')
    plt.ylabel('Streamflow (cfs)')
    
    # Ticks on x-axis for Year
    plt.xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 10, dtype='int')])	
    
    # Middle Plot (2)
    plt.subplot(312)
    plt.plot(data['Year'],data['Tqmean']*100,'--D')						     # Diamond symbol to represent the annual values of Tqmeanx100%
    plt.xlabel('Year')
    plt.ylabel('Tqmean (%)')
    
    # Ticks on x-axis for Year
    plt.xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 10, dtype='int')])	
    
    # Bottom Plot (3)
    plt.subplot(313)
    plt.bar(data['Year'],data['RBindex'])                                     # A bar plot of R-B index
    plt.xlabel('Year')
    plt.ylabel('R-B Index (ratio)')
    
    # Ticks on x-axis for Year
    plt.xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 10, dtype='int')])	
    
    # saving figure with pdf extension
    plt.savefig("/home/tiwari13/ABE65100/06-graphing-data-with-python-roccabye/output/"+base+".pdf")
    
  