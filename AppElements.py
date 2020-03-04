#!usr/in/python

from Tkinter import *
from ttk import *
import tkMessageBox as tkMB


class Widgets():

    master=None
    elementList=[]
    def __init__(self,TkObj):
        """Primary initialize """
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

#### Test procedure ----v
#root=Tk()
#ev=Elements(root)
#root.wm_title(" AppWindow ")
#root.geometry("1200x600")
#root.mainloop()