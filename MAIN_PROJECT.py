#importing all necessary libraries
from osgeo import gdal
from mayavi import mlab
import tkinter as tk
import numpy as np
#from scipy import stats as stat
from matplotlib import pyplot as plot
from tkinter import filedialog
from perlin_numpy import generate_fractal_noise_2d

current_opened_file = "D:/Random Stuff/image.tif"
#assigned_file_directory = ""

def file_browser():
    select_file_name = filedialog.askopenfilename(initialdir = "/D:Random Stuff", title = "Select a File",)

    if (select_file_name):
        global current_opened_file 
        current_opened_file = select_file_name
        current_selected_file.configure(text = "Current Selected File: " + current_opened_file)
        
        #split_function = select_file_name.split("/")
        #split_file_name = (split_function[0] + "//" + split_function[1] + "//" + split_function[2])
        #assigned_file_directory = '"' + select_file_name + '"'


def statistics(a):
    mean = np.mean(a)
    median = np.median(a)
    #mode = stat.mode(a)
    standard_dev = np.std(a)
    min = np.min(a)
    max = np.max(a)
    color_scheme = ["#264653","#2A9D8F","#E9C46A","#F4A261","#E76F51"]

    plot.bar(["Mean","Median","Stand. Dev.","Minimum","Maximum"] , [mean, median, standard_dev, min, max], color = color_scheme)
    plot.title("Terrain Statistics")
    plot.ylabel("Terrain Height")

    plot.show()

def convert_file():

    #assigning the file path for the tif image
    file_path = current_opened_file

    #opening the tif file and assigning it
    file = gdal.Open(file_path)

    #the assigned file is now being converted into an array based on the grayscale values
    data_array = file.ReadAsArray()

    #creating the figure dimensions and assigning colors to values (Height) 
    mlab.figure(size = (1025, 1025))

    #mlab surf function takes the 2D numpy array and plots the surface, warp scale is vertical exaggeration/scale factor
    mlab.surf(data_array, warp_scale = 0.01, colormap = "cool")

    statistics(data_array)
    
    #mlab shows the plotted 3D DEM
    mlab.show()
    



def generate_terrain():
    mlab.figure(size = (1025,1025))
    
    #perlin noise method
    fractal_noise = generate_fractal_noise_2d((1024,1024), (4,4), 8)
    
    mlab.surf(fractal_noise, warp_scale = 50, colormap = "cool")

    statistics(fractal_noise)

    mlab.show()



#initializing the window
x = tk.Tk()

#window size
x.geometry("600x338")

#window title
x.title("3D Terrain Generation")
x.configure(bg = "dark slate blue")




#button properties, command is the function/action performed
exit_button = tk.Button(x, text = "Exit...", width = 20, height = 5, bg = "grey", activebackground = "dark slate gray", bd = 6, command = x.destroy)
exit_button.place(x = 235, y = 245)

browse_button = tk.Button(x, text = "Browse Files...", width = 20, height = 5, bg = "grey", activebackground = "dark slate gray", bd = 6, command= file_browser)
browse_button.place(x = 235, y = 0)

dem_button = tk.Button(x, text = "Create 3D Elevation Model", width = 30, height = 10, bg = "grey", activebackground = "dark slate gray", 
bd = 6, command = convert_file)
dem_button.grid(row = 1, column = 1)

random_generation_button = tk.Button(x, text = "Generate Unique/Random 3D Terrain", width = 30, height = 10, bg = "grey", activebackground = "dark slate gray", 
bd = 6, command = generate_terrain)
random_generation_button.grid(row = 2, column = 1)

current_selected_file = tk.Label(x, text= "Current Selected File: " + current_opened_file, width = 50, height = 1, fg = "White", bg = "dark slate blue", anchor= "sw")
current_selected_file.place(x = 235, y = 160)



#running the "x" GUI variables
x.mainloop()


