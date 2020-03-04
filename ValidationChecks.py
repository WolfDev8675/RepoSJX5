#!usr/bin/python
import tkMessageBox as tkm
from FileManagement import *
from Tickets import *

class Validation(FileHandler,Ticket):
    

    usr_dct=None
    usr_det=None
    info_des=None

    def __init__(self):
        self.traceback()

    def traceback(self):
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
        for user in self.usr_dct:
            if (user == usrid) and (self.usr_dct[user] == pword):
                return True
        
        return False

    def validDestinations(self,des1,des2):
        if des1 in self.info_des and des2 in self.info_des:
            return True
        else:
            return False
    
    def validClass(self,clas):
        if clas in ['SL','II','CC','2A','3A']:
            return True
        else:
            return False

    def updateInfo(self):
        self.setFile('infoDB.txt',self.info_des)

    def updateUsrInfo(self):
        self.setFile('userInfo.txt',self.usr_dct)

    def updateUsrDet(self):
        self.setFile('UserDetails.txt',self.usr_det)
