#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import csv
import time
import tkinter.messagebox 
from tkinter import *
from tkinter import filedialog

# Function for opening the file explorer window
def browseFiles():
    file_name = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV files", "*.csv*"), ("all files", "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text=file_name)
    if (len(file_name) == 0):
        msg = 'No file was selected. Please upload a valid file.' 
        tkinter.messagebox.showinfo('Select a file', msg)
    else:
        df = pd.read_csv(file_name)              
                
        if(len(df) == 0):      
            msg = 'File has no data. Please upload a valid file.'
            tkinter.messagebox.showinfo('Select a file', msg)
        else:
            df.to_csv('Converted_data.csv', sep=',', index=False)
      

# Addresses conversion function
def convert(lat, lon):   
    # Set random noise value for adding to coordinates - not used in current program version
    noise = np.random.normal(0.0041,0.001) * np.sign(np.random.normal(0, 1, 1))[0]
    lat += noise
    noise = np.random.normal(0.0041,0.001) * np.sign(np.random.normal(0, 1, 1))[0]
    lon += noise
    locat= (lat,lon)
    return locat
    
                        
#Defining the 'compute' button function 
def compute():
    
        
    try:

        with open("Converted_data.csv",'r') as file:
            try:
                df = pd.read_csv(file)
                df['latitude'] = ""
                df['longitude'] = ""
                for row in range(len(df)):
                    Address = df['address'].values[row]
                    city = df['city'].values[row]
                    state = df['state'].values[row]
                    zip_code = str(df['zip'].values[row])
                   
                    #...addresses conversion to coordinates.........
                    from geopy.geocoders import Nominatim
                    from geopy import distance
                    # Timeout value may need to be adjusted depending on the size of data being processed
                    geolocator = Nominatim(user_agent='Addr_to_Coord_GUI', timeout=2000)
            #...............patient into input here.......................................................
                    t=(Address+', '+ city+', '+ state+', '+ zip_code)
            #.............................................................................................
                    g = [geolocator.geocode(t)]

                    zip_cd = ""
                    lat_np = g[0].latitude
                    lon_np = g[0].longitude
                    # Apply location conversion until a valid zip code is obtained
                    # while (len(zip_cd) == 0):
                        # locat= convert(lat_np,lon_np)
                        # lat_np = locat[0]
                        # lon_np = locat[1]
                        # locatn = geolocator.reverse(locat)                       
                        # address = locatn.raw['address']
                        # zip_cd = address.get('postcode','')

                    df['latitude'].values[row] = lat_np
                    df['longitude'].values[row] = lon_np
                    print('Patient #'+str(row+1)+' converted')
                    time.sleep(1) # A maximum of one request per second is allowed per Nominatim user policy
                    
                df.to_csv('Converted_data.csv', sep=',', index=False)

                msg = "Data has been converted"  
                      
            except csv.Error as e:
                msg = "No data in file "+ e
    except ValueError:
        if len(str(msg)) == 0:
            msg = "Invalid values!"
    tkinter.messagebox.showinfo('Converting', msg)


#------------------------------------------------------------------------------------------------------------------------------
# Main window
win = tkinter.Tk()
win.title("Address to Coordinates Conversion")
win.geometry("600x300")

frame = tkinter.Frame(win, width=300, height=200)
frame.pack()

#Creating the GUI layout
gui_frame = tkinter.LabelFrame(frame, text = "Convert Addresses")
gui_frame.grid(row= 0, column= 0, padx = 20, pady = 20)

# Create a File Explorer 
label_file_explorer = Label(gui_frame, text = "Input File", width = 70, height = 3, fg = "blue")
label_file_explorer.grid(column = 1, row = 1, padx = 20, pady = 10)

button_explore = Button(gui_frame, text = "Browse Files", command = browseFiles)
button_explore.grid(column = 1, row = 2, padx = 20, pady = 10)       
             
btn = Button(gui_frame, text="Convert",command = compute)
btn.grid(row = 3, column = 1, padx = 20, pady = 10)
 
button_exit = Button(gui_frame, text = "Exit", command = exit) 
button_exit.grid(column = 1, row = 5, padx = 10, pady = 10)
    
#-------------------------------------------------------------------------------------------------------------------------------

win.mainloop() 
