#!usr/bin/python

# File ValidationChecks.py : Class Validation
#   checks the availability of the backing data files 
#       and also if a staion / user is valid provided the information is given 
#       Upations of the data is also carried out 
##
import tkMessageBox as tkm
from FileManagement import *
from Tickets import *

class Validation(FileHandler,Ticket):
    """ Class Validation for handling all validation tasks; as additional perks also updates data to files and checks back data from files """

    usr_dct=None        ## holds username to password links
    usr_det=None        ## holds username to additional user details
    info_des=None       ## holds information of stations 

    def __init__(self):
        self.traceback()

    def traceback(self):
        """ Traceback files to check their contents; failure in traceback will stop the UI completely"""
        try:
            self.usr_dct=self.getFile('userInfo.txt')
            self.usr_dct=eval(self.usr_dct)
            self.info_des=eval(self.getFile('infoDB.txt'))
            self.usr_det=self.getFile('UserDetails.txt')
            self.usr_det=eval(self.usr_det)
            
        except:
            tkm.showerror('ERROR ',' DATA FILES TAMPERED ')
            return False
        
        return True

    def userValid(self,usrid,pword):
        """ Validate if a username is exactly linked to a given password """
        for user in self.usr_dct:
            if (user == usrid) and (self.usr_dct[user] == pword):
                return True
        
        return False

    def validDestinations(self,des1,des2):
        """ Check info of destinations """
        if des1 in self.info_des and des2 in self.info_des:
            return True
        else:
            return False
    
    def validClass(self,clas):
        """ Check if category of travel exists """
        if clas in ['SL','II','CC','2A','3A']:
            return True
        else:
            return False

    def updateInfo(self):
        """ Updates info of stations """
        self.setFile('infoDB.txt',self.info_des)

    def updateUsrInfo(self):
        """ Updates information of username and password"""
        self.setFile('userInfo.txt',self.usr_dct)

    def updateUsrDet(self):
        """ Updates information of userdetails """
        self.setFile('UserDetails.txt',self.usr_det)


 ## end of class 