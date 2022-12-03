#needed to import numpy, gdal, matlab, and tkinter
import matlab as mat
from osgeo import gdal
from mayavi import mlab
import tkinter as tk
import numpy as np
from tkinter import filedialog


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
    mlab.surf(data_array, warp_scale = 0.01, colormap = "cool")

    #mlab shows the plotted 3D DEM
    mlab.show()
    



def generate_terrain():
    columns = 100
    rows = 100


    #large_array = np.random.randint(0,10, size = (rows,columns))
    large_array = np.random.random((rows,columns))
    
    
    mlab.surf(large_array, warp_scale = 1, colormap = "cool")
    mlab.show()




def browser_file_name():
    select_file_name = filedialog.askopenfilename(initialdir = "/", title = "Select a File")


#initializing the window
x = tk.Tk()

#window size
x.geometry("400x350")

#window title
x.title("3D Terrain Generation")
x.configure(bg = "dark slate blue")

def file_browser_window():
    x2 = tk.Tk()
    x2.title("File Browser")
    x2.geometry("400x400")
    x2.configure(bg = "dark slate gray")

    file_select = tk.Button(x2, text = "Select Files", width = 20, height = 5, bg = "grey", bd = 6, command = browser_file_name)
    file_select.grid(row = 1, column = 1)

    file_browser_quit = tk.Button(x2, text = "Exit", width = 20, height = 5, bg = "grey", bd = 6, command = quit)
    file_select.grid(row = 1, column = 2)




#button properties, command is the function/action performed
exit_button = tk.Button(x, text = "Exit...", width = 20, height = 5, bg = "grey", activebackground = "dark slate gray", bd = 6, command = x.destroy)
exit_button.grid(row = 2, column = 2)

dem_button = tk.Button(x, text = "Create 3D Elevation Model", width = 30, height = 10, bg = "grey", activebackground = "dark slate gray", 
bd = 6, command = convert_file)
dem_button.grid(row = 1, column = 1)


browse_button = tk.Button(x, text = "Browse Files...", width = 20, height = 5, bg = "grey", activebackground = "dark slate gray", bd = 6, command= file_browser_window)
browse_button.grid(row = 1, column = 2)


random_generation_button = tk.Button(x, text = "Generate Unique/Random 3D Terrain", width = 30, height = 10, bg = "grey", activebackground = "dark slate gray", 
bd = 6, command = generate_terrain)
random_generation_button.grid(row = 2, column = 1)


#running the "x" GUI variables
x.mainloop()


