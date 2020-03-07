#!usr/in/python

#
# File AppElements.py : Class Widgets
#   contains methods to create elements in 
#   the app screen
#
from Tkinter import *
from ttk import *
import tkMessageBox as tkMB


class Widgets():
    """ Widgets Class to handle creation of widgets and hold the master(Tkinter.TK object) used to create the widgets on the screen"""
    master=None
    elementList=[]
    def __init__(self,TkObj):
        """Primary initialization setting up Widgets.master to Tkinter.TK object"""
        self.master=TkObj
        
    def createButton(self,master=None,buttonText="",directive=None,placeX=None,placeY=None):
        """ Create a Button to place on the App window """
        b=Button(master,text=buttonText,command=directive)
        b.place(x=placeX,y=placeY)
        return b

    def createLabel(self,master=None,labelText="",widthLabel=None,colorBackground=None,fontStyle=None,fontSize=None,placeX=None,placeY=None):
        """ Create a Label to place on the App window """
        l=Label(master,text=labelText,width=widthLabel,font=(fontStyle,fontSize))
        l.configure(background=colorBackground)
        l.place(x=placeX,y=placeY)
        return l
    
    def createEntry(self,master=None,prompt=None,widthEntry=None,colorBackground=None,fontStyle=None,fontSize=None,placeX=None,placeY=None):
        """ Create an input entry """
        e=Entry(master,text=prompt,width=widthEntry,font=(fontStyle,fontSize))
        e.configure(background=colorBackground)
        e.place(x=placeX,y=placeY)
        return e
    
    def createLabelV2(self,master=None,labelText='',widthLabel=None,wrapSize=None,colorBackground=None,fontStyle=None,fontSize=None,placeX=None,placeY=None):
        """ Create a Label to place on the App window with textwrap enabled and alignment justified at center(version 2)"""
        l=Label(master,text=labelText,width=widthLabel,font=(fontStyle,fontSize),wraplength=wrapSize,justify='center')
        l.configure(background=colorBackground)
        l.place(x=placeX,y=placeY)
        return l

    def createText(self,master=None,widthText=None,heightText=None,colorBackground=None,fontStyle=None,fontSize=None,placeX=None,placeY=None):
        """ Create an input Text with enabled height """
        e=Text(master,width=widthText,height=heightText,font=(fontStyle,fontSize))
        e.configure(background=colorBackground,state='normal')
        e.place(x=placeX,y=placeY)
        return e
    
    def createEntryP(self,master=None,prompt=None,widthEntry=None,colorBackground=None,fontStyle=None,fontSize=None,placeX=None,placeY=None):
        """ Create an input entry for passwords """
        e=Entry(master,text=prompt,width=widthEntry,show='*',font=(fontStyle,fontSize))
        e.configure(background=colorBackground)
        e.place(x=placeX,y=placeY)
        return e

##  End of Class 


#### Test procedure ----v
#root=Tk()
#ev=Widgets(root)
#ev.createLabel(ev.master," Heading1 ",300,"#f5c9f5","garamond",20,0,0)
#root.wm_title(" AppWindow ")
#root.geometry("1200x600")
#root.mainloop()