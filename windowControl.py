#!usr/bin/python

# final control
from Tkinter import *
from AppElements import *
from WindowScreens import *
import tkMessageBox 

rootUI=Tk()
control=Screens(rootUI)
rootUI.wm_title(" TICKET BOOKING UI ")
rootUI.geometry("1200x600")
rootUI.resizable(False,False)
rootUI.mainloop()
