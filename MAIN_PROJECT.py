#needed to import numpy, gdal, and matlab
import numpy
import matlab as mat
from osgeo import gdal
from mayavi import mlab
import tkinter as tk
from numpy import random
#import system - Might not need?



def convert_file():

    #assigning the file path for the tif image
    file_path = 'D:\Random Stuff\image.tif'
    ######## Want to make the file_path a possible input for users to load custom DEM files through GUI instead of changing code #######

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
x.geometry("400x350")

#window title
x.title("3D Terrain Generation")
x.configure(bg = "dark slate blue")



#button properties, command is the function/action performed
dem_button = tk.Button(x, text = "Create 3D Elevation Model", width = 30, height = 10, bg = "grey", activebackground = "dark slate gray", bd = 6, command = convert_file)
dem_button.grid(row = 1, column = 1)

browse_button = tk.Button(x, text = "Browse Files...", width = 20, height = 5, bg = "grey", activebackground = "dark slate gray", bd = 6)
browse_button.grid(row = 1, column = 2)

random_generation_button = tk.Button(x, text = "Generate Unique/Random 3D Terrain", width = 30, height = 10, bg = "grey", activebackground = "dark slate gray", bd = 6)
random_generation_button.grid(row = 2, column = 1)


#running the "x" GUI variables
x.mainloop()






##################want to perhaps run code from another file???##################################
#os.system("D:\Random Stuff\array_test.py")

#the code that I want to run from the array_test.py file
#will need to adjust and create loop for a 1000x1000(or larger) grid (1000x1000 pixels)

x1 = random.rand()
y1 = random.rand()
z1 = random.rand()

x2 = random.rand()
y2 = random.rand() ########################  Create loop to generate a large array. Maybe 1000 x 1000 ############
z2 = random.rand()

x3 = random.rand()
y3 = random.rand()
z3 = random.rand()

############# [x,y,z] values #########
test_array = ([x1,y1,z1], [x2,y2,z2], [x3,y3,z3])



a = 0
b = 0
c = range(1000)

large_array = ([a],[b],[c])

for array_position in c:
    asd