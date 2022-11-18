#needed to import numpy, gdal, and matlab
import numpy
import matlab as mat
from osgeo import gdal
from mayavi import mlab
import tkinter as tk



def convert_file():

    #assigning the file path for the tif image
    file_path = 'D:\Random Stuff\image.tif'

    #opening the tif file and assigning it
    file = gdal.Open(file_path)

    #the assigned file is now being converted into an array based on the grayscale values
    data_array = file.ReadAsArray()

    #creating the figure dimensions and assigning colors to values (Height)
    # 1025 for x and y size because original tif pixels 
    mlab.figure(size = (1025, 1025))

    #mlab surf function takes the 2D numpy array and plots the surface, warp scale is vertical exaggeration/scale factor
    #################### Potentially use this surf function to plot and create a 3D version of a randomly generated array #############################
    mlab.surf(data_array, warp_scale = 0.01, colormap = "cool")

    #mlab shows the plotted 3D DEM
    mlab.show()