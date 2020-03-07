#!usr/bin/python

# Final control 
# for controlling the main call 
# to the window screens 
# that handles all the views of the app 
#
from Tkinter import *
from AppElements import *
from WindowScreens import *
import tkMessageBox 

rootUI=Tk()                     # Tkinter root object
control=Screens(rootUI)         # Screen/View control object 
rootUI.wm_title(" TICKET BOOKING UI ")          # window title
rootUI.geometry("1200x600")                     # window size
rootUI.resizable(False,False)                   # fixing aspect ratio       
rootUI.mainloop()                               # main loop for witholding window until exit
