#needed to import numpy, gdal, and matlab
import numpy
import matlab as mat
from osgeo import gdal
from mayavi import mlab
import tkinter as tk
import system



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
    






#initializing the window
x = tk.Tk()

#window size
x.geometry("375x400")

#window title
x.title("GUI Program")



#button properties, command is the function/action performed
dem_button = tk.Button(x, text = "Create 3D Elevation Model", width = 25, height = 10, activebackground = "red", command = convert_file)
dem_button.grid(row = 1, column = 1)

browse_button = tk.Button(x, text = "Browse Files...", width = 25, height = 10, activebackground = "red")
browse_button.grid(row = 1, column = 2)

########################### want to insert another button to call a function that will generate a random DEM array #############################


#running the "x" GUI variables
x.mainloop()


##################want to perhaps run code from another file???##################################
#os.system("D:\Random Stuff\array_test.py")

