#!usr/bin/python

from Tkinter import *
from ttk import *
import tkMessageBox as tkMB
from ValidationChecks import *
from AppElements import *
from Tickets import *

class Screens(Widgets,Validation,Ticket):

    currentUser=['','']
    superUser=['masterC659','plcc982#F']

    def __init__(self,TkObj):
        self.master=TkObj
        startup=self.traceback()
        if not(startup):
            self.master.destroy()
        
        self.welcomeScreen()
        
        

    def welcomeScreen(self):
        self.clearWindow()
        lh=self.createLabel(self.master," Ticket Booking System ",300,"#f5c9f5","garamond",20,0,0)
        self.elementList.append(lh)
        lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
        self.elementList.append(lf)
        b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
        self.elementList.append(b1)
        b2=self.createButton(self.master," Maintenance ",self.maintenanceFn1,1110,0)
        self.elementList.append(b2)
        l1=self.createLabel(self.master," Username ",50,"#696969","Garamond",17,50,200)
        self.elementList.append(l1)
        e1=self.createEntry(self.master," username ",44,'#696969',"garamond",14,155,202)
        self.elementList.append(e1)
        l2=self.createLabel(self.master," Password ",50,"#696969","garamond",17,50,230)
        self.elementList.append(l2)
        e2=self.createEntryP(self.master," password ",44,'#696969',"garamond",14,155,232)
        self.elementList.append(e2)
        self.currentUser=[e1.get(),e2.get()]
        b3=self.createButton(self.master," Log in ",self.welcomeScreen,450,262)
        self.elementList.append(b3)
        if e1.get()=='' and e2.get()=='':
            tkMB.showinfo("Warning","Empty query ")
            b3=self.createButton(self.master," Log in ",self.welcomeScreen,450,262)
            self.elementList.append(b3)
        else:
            b3=self.createButton(self.master," Log in ",self.userLogIn,450,262)
            self.elementList.append(b3)
        b4=self.createButton(self.master," Register ",self.registration,450,300)
        self.elementList.append(b4)
        
        self.currentUser=[e1.get(),e2.get()]
        

    def userLogIn(self):
        if self.userValid(self.currentUser[0],self.currentUser[1])==True:
            self.clearWindow()
            self.dashboard()
        else:
            tkMB.showwarning("Authentication Error "," UserID or Password is not valid ")
            self.welcomeScreen()
    
    def dashboard(self):
        self.clearWindow()
        lh=self.createLabel(self.master," Dashboard ",300,"#55c9f5","garamond",20,0,0)
        self.elementList.append(lh)
        lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
        self.elementList.append(lf)
        id=self.currentUser[0]
        name=self.usr_det[id]['name']
        l1=self.createLabel(self.master, ('\t\t\t\t'+id+"\t\t-\t\t"+name) ,300,"#68c9f5","garamond",15,0,40)
        self.elementList.append(l1)
        b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
        self.elementList.append(b1)
        b2=self.createButton(self.master," < ",self.intermediate,10,41)
        self.elementList.append(b2)
        b3=self.createButton(self.master," Normal \n Booking ",self.bookingNorm,250,200)
        self.elementList.append(b3)
        b3=self.createButton(self.master," Platform \n Booking ",self.bookingPlat,500,200)
        self.elementList.append(b3)
        b4=b2=self.createButton(self.master," Edit \n Personal \n Info ",self.userEdit,1115,70)
        self.elementList.append(b2)

    def intermediate(self):
        tkMB.showinfo('Message','You have been Logged out ! ... ')
        self.welcomeScreen()

    def registration(self):
         self.clearWindow()
         lh=self.createLabel(self.master," Registration - new user ",300,"#56c962","garamond",25,0,0)
         self.elementList.append(lh)
         lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
         self.elementList.append(lf)
         b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
         self.elementList.append(b1)
         b2=self.createButton(self.master," < ",self.welcomeScreen,10,41)
         self.elementList.append(b2)
         l1=self.createLabel(self.master," User Name* ",30,"#759aaa","garamond",17,30,120)
         self.elementList.append(l1)
         e1=self.createEntry(self.master," userreg ",20,'#698869',"garamond",14,170,122)
         self.elementList.append(e1)
         l2=self.createLabel(self.master," password  ",30,"#759aaa","garamond",17,420,120)
         self.elementList.append(l2)
         e2=self.createEntryP(self.master," pasreg ",20,'#698869',"garamond",14,560,122)
         self.elementList.append(e2)
         l3=self.createLabel(self.master," Full Name  ",50,"#759aaa","garamond",17,30,200)
         self.elementList.append(l3)
         e3=self.createEntry(self.master," namereg ",40,'#698869',"garamond",14,190,202)
         self.elementList.append(e3)
         l4=self.createLabel(self.master," Address \n\n ",50,"#759aaa","garamond",17,30,270)
         self.elementList.append(l4)
         e4=self.createEntry(self.master," addreg ",40,'#698869',"garamond",14,190,272)
         self.elementList.append(e4)
         l5=self.createLabel(self.master," Phone  ",50,"#759aaa","garamond",17,30,390)
         self.elementList.append(l5)
         e5=self.createEntry(self.master," phonereg ",40,'#698869',"garamond",14,190,392)
         self.elementList.append(e5)
         l6=self.createLabel(self.master," Registered ID   ",50,"#759aaa","garamond",17,30,460)
         self.elementList.append(l6)
         e6=self.createEntry(self.master," regidEd ",40,'#698869',"garamond",14,190,462)
         self.elementList.append(e6)
         b3=self.createButton(self.master," Register ",self.register,700,450)
         self.elementList.append(b3)
         self.userR=[e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()]
         
    def register(self):
        self.registration()
        self.clearWindow()
        if self.userR[0] == '' or self.userR[1] == '' or self.userR[2] == '' or self.userR[3] == '' or self.userR[4] == '':
            tkMB.showwarning('Notification',' ONE OR MORE FIELDS EMPTY. \n User not registerable \n Reconsider filling voids ')
            self.registration()
        else:
            self.usr_dct.update({self.userR[0]:self.userR[1]})
            self.usr_det.update({self.userR[0]:{'name':self.userR[2],'address':self.userR[3],'phone':self.userR[4],'reg_id':self.userR[5]}})
            self.updateUsrInfo()
            self.updateUsrDet()
            tkMB.showinfo('Notification',' User Registered as : '+ self.userR[0])
            self.welcomeScreen()

    def maintenanceFn1(self):
        self.clearWindow()
        lh=self.createLabel(self.master," Maintenance ",300,"#f5c992","garamond",25,0,0)
        self.elementList.append(lh)
        lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
        self.elementList.append(lf)
        b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
        self.elementList.append(b1)
        b2=self.createButton(self.master," < ",self.welcomeScreen,10,41)
        self.elementList.append(b2)
        l1=self.createLabel(self.master," Main ID ",50,"#696980","Garamond",17,50,200)
        self.elementList.append(l1)
        e1=self.createEntry(self.master," MainID ",44,'#696969',"garamond",14,155,202)
        self.elementList.append(e1)
        l2=self.createLabel(self.master," Password ",50,"#696980","garamond",17,50,230)
        self.elementList.append(l2)
        e2=self.createEntryP(self.master," MasterPass ",44,'#696969',"garamond",14,155,232)
        self.elementList.append(e2)
        b3=self.createButton(self.master," Proceed ",self.maintenanceFn1,450,262)
        self.elementList.append(b3)
        if self.superUser == [e1.get(),e2.get()] :
            b3=self.createButton(self.master," Proceed ",self.maintenanceFn2,450,262)
            self.elementList.append(b3)
        else:
            if e1.get()=='' and e2.get()=='':
                tkMB.showinfo("Warning","Empty query ")
            else:
                tkMB.showwarning(" Authentication Error"," INCORRECT AUTHENTICATION ATTEMPT  ")

    def maintenanceFn2(self):
        tkMB.showwarning('Warning Notification','Super User control Granted ')
        self.clearWindow()
        lh=self.createLabel(self.master," Maintenance ",300,"#f5c992","garamond",25,0,0)
        self.elementList.append(lh)
        lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
        self.elementList.append(lf)
        b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
        self.elementList.append(b1)
        b2=self.createButton(self.master," < ",self.intermediate,10,41)
        self.elementList.append(b2)
        stns=str(self.info_des)
        lInfo=self.createLabelV2(self.master,'STATIONS AVAILABLE \n'+stns,147,1150,'#e0e0ff','garamond',13,10,65)
        self.elementList.append(lInfo)
        direc='Add Station not in the station list or edit an existing station name code '
        ldirec=self.createLabel(self.master,direc,90,'#605078','garamond',12,10,300)
        self.elementList.append(ldirec)
        l1=self.createLabel(self.master," Add Station ",50,"#698880","Garamond",17,50,340)
        self.elementList.append(l1)
        e1=self.createEntry(self.master," addVal ",44,'#698869',"garamond",14,180,342)
        self.elementList.append(e1)
        b3=self.createButton(self.master," Append ",self.appendVal,610,342)
        self.elementList.append(b3)
        l2=self.createLabel(self.master," Replace ",50,"#698880","Garamond",17,50,390)
        self.elementList.append(l2)
        e2=self.createEntry(self.master," replace ",44,'#698869',"garamond",14,180,392)
        self.elementList.append(e2)
        l3=self.createLabel(self.master," With ",50,"#698880","garamond",17,50,420)
        self.elementList.append(l3)
        e3=self.createEntry(self.master,"  with",44,'#698869',"garamond",14,180,422)
        self.elementList.append(e3)
        b4=self.createButton(self.master," Replace ",self.replaceVal,610,410)
        self.elementList.append(b4)
        
        self.edits=[e1.get(),e2.get(),e3.get()]
        

    def appendVal(self):
        if self.edits[0]=='':
            tkMB.showwarning('Warning ',' Nothing to append ')
            self.maintenanceFn2()
        elif self.edits[0] in self.info_des:
            tkMB.showwarning('Warning ',' Field value already exists ')
            self.maintenanceFn2()
        else:
            tkMB.showinfo('Notification ',' Field value appended ')
            self.info_des.append(self.edits[0])
            self.updateInfo()
            self.maintenanceFn2()
        
    def replaceVal(self):
        if self.edits[1] == '' or self.edits[2]=='':
            tkMB.showwarning('Warning ',' Required fields empty ')
            self.maintenanceFn2()
        elif self.edits[1] not in self.info_des:
            tkMB.showwarning('Warning ',' Failed to find Replace element ')
            self.maintenanceFn2()
        elif self.edits[2] in self.info_des:
            tkMB.showwarning('Warning ',' Replacement element already exists ')
            self.maintenanceFn2()
        else:
            for i in range(len(self.info_des)):
                if self.edits[1] == self.info_des[i]:
                    self.info_des[i]=self.edits[2]
                    break
            tkMB.showinfo('Notification ',' Replacement successful ')
            self.updateInfo()
            self.maintenanceFn2()

    def bookingNorm(self):
        self.clearWindow()
        lh=self.createLabel(self.master," Normal Booking  ",300,"#aacc22","garamond",25,0,0)
        self.elementList.append(lh)
        lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
        self.elementList.append(lf)
        b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
        self.elementList.append(b1)
        b2=self.createButton(self.master," < ",self.dashboard,10,41)
        self.elementList.append(b2)
        lhs1=self.createLabel(self.master," Passenger Details  ",40,"#759548","garamond",17,30,70)
        self.elementList.append(lhs1)
        l1=self.createLabel(self.master," Adults*  ",13,"#755948","garamond",17,30,120)
        self.elementList.append(l1)
        e1=self.createEntry(self.master," nosAd ",5,'#698869',"garamond",14,110,122)
        self.elementList.append(e1)
        l2=self.createLabel(self.master," Children   ",14,"#755948","garamond",17,200,120)
        self.elementList.append(l2)
        e2=self.createEntry(self.master," nosCh ",5,'#698869',"garamond",14,300,122)
        self.elementList.append(e2)
        l3=self.createLabel(self.master," Persons with Disability  ",30,"#755948","garamond",17,30,170)
        self.elementList.append(l3)
        e3=self.createEntry(self.master," nosPwd ",5,'#698869',"garamond",14,300,172)
        self.elementList.append(e3)
        l4=self.createLabel(self.master," Senior Citizens  ",30,"#755948","garamond",17,30,220)
        self.elementList.append(l4)
        e4=self.createEntry(self.master," nosScz ",5,'#698869',"garamond",14,300,222)
        self.elementList.append(e4)
        lhs2=self.createLabel(self.master," Journey Details  ",30,"#759548","garamond",17,600,120)
        self.elementList.append(lhs2)
        l5=self.createLabel(self.master," Class*  ",20,"#755948","garamond",17,600,170)
        self.elementList.append(l5)
        e5=self.createEntry(self.master," clas ",10,'#698869',"garamond",14,700,172)
        self.elementList.append(e5)
        l6=self.createLabel(self.master," From*  ",20,"#755948","garamond",17,600,210)
        self.elementList.append(l6)
        e6=self.createEntry(self.master," destI ",10,'#698869',"garamond",14,700,212)
        self.elementList.append(e6)
        l7=self.createLabel(self.master," To*  ",20,"#755948","garamond",17,600,250)
        self.elementList.append(l7)
        e7=self.createEntry(self.master," destF ",10,'#698869',"garamond",14,700,252)
        self.elementList.append(e7)
        lhs3=self.createLabel(self.master," Payment Details  ",45,"#759548","garamond",17,30,300)
        self.elementList.append(lhs3)
        l8=self.createLabel(self.master," Payment Gateway*   ",45,"#755948","garamond",17,30,340)
        self.elementList.append(l8)
        e8=self.createEntry(self.master," payGateN ",20,'#698869',"garamond",14,300,342)
        self.elementList.append(e8)
        b3=self.createButton(self.master," Proceed \n to \n Book  ",self.finalBookPathNRM,700,350)
        self.elementList.append(b3)
        b4=self.createButton(self.master," Check \n Class ",self.showClasses,1000,170)
        self.elementList.append(b4)
        b5=self.createButton(self.master," Check \n Destinations  ",self.destnationList,1000,220)
        self.elementList.append(b5)

        if e1.get()=='':
             self.bookEntries=[self.currentUser[0],0,0,0,0,0,e5.get(),e6.get(),e7.get(),e8.get()]
             tkMB.showwarning('Warning','Fill the "*" fields ')
        else:
            if e2.get() == '':c=0
            else: c=int(e2.get())
            if e3.get() == '':pd=0
            else: pd=int(e3.get())
            if e4.get() == '':sc=0
            else: sc=int(e4.get())
            count=1
            st=0
            en=0
            for pl in self.info_des:
                if pl==e6.get():
                    st=count
                if pl==e7.get():
                    en=count
                count+=1
            self.bookEntries=[self.currentUser[0],int(e1.get()),c,pd,sc,e5.get(),abs(st-en),e6.get(),e7.get(),e8.get()]
            
        

    def finalBookPathNRM(self):
        self.bookingNorm()
        if self.validDestinations(self.bookEntries[7],self.bookEntries[8]) and self.validClass(self.bookEntries[5]):
            self.finalBookPathNRM2()
        elif not (self.validDestinations(self.bookEntries[7],self.bookEntries[8])):
            tkMB.showerror(' Error ',' Journey Details incorrect \n Check Destinations ')
            self.bookingNorm()
        else:
            tkMB.showerror(' Error ',' Journey Details incorrect \n Check Travel Class')
            self.bookingNorm()

    def finalBookPathNRM2(self):
        self.clearWindow()
        lh=self.createLabel(self.master," Normal Booking  ",300,"#aacc22","garamond",25,0,0)
        self.elementList.append(lh)
        lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
        self.elementList.append(lf)
        b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
        self.elementList.append(b1)
        b2=self.createButton(self.master," < ",self.intermediate,10,41)
        self.elementList.append(b2)
        self.bookEntries.append(self.costNormal(self.bookEntries[1:7]))
        tkcts=self.genTicketNRM(self.bookEntries)
        tktsF=tkcts.next()
        tktsB=tkcts.next()
        tkMB.showinfo('Notification','Ticket generated at '+tktsF)
        l1=self.createLabel(self.master,tktsB,300,'#ffffff','garamond',10,10,65)
        self.elementList.append(l1)
        b3=self.createButton(self.master," Home ",self.intermediate,1100,41)
        self.elementList.append(b3)

    def bookingPlat(self):
         self.clearWindow()
         lh=self.createLabel(self.master," Platform Booking  ",300,"#aacc22","garamond",25,0,0)
         self.elementList.append(lh)
         lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
         self.elementList.append(lf)
         b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
         self.elementList.append(b1)
         b2=self.createButton(self.master," < ",self.dashboard,10,41)
         self.elementList.append(b2)
         l1=self.createLabel(self.master," Number of Individuals  ",50,"#755948","garamond",17,50,200)
         self.elementList.append(l1)
         e1=self.createEntry(self.master," nosIndv ",5,'#698869',"garamond",14,300,202)
         self.elementList.append(e1)
         l2=self.createLabel(self.master," Station Name   ",50,"#755948","garamond",17,50,230)
         self.elementList.append(l2)
         e2=self.createEntry(self.master," stn ",10,'#698869',"garamond",14,300,232)
         self.elementList.append(e2)
         l3=self.createLabel(self.master," Payment Gateway   ",50,"#755948","garamond",17,50,260)
         self.elementList.append(l3)
         e3=self.createEntry(self.master," payGateP ",20,'#698869',"garamond",14,300,262)
         self.elementList.append(e3)
         b3=self.createButton(self.master," Proceed \n to \n Book  ",self.finalBookPathPTM,700,350)
         self.elementList.append(b3)
         b4=self.createButton(self.master," Destinations  ",self.destnationList,700,250)
         self.elementList.append(b4)
         if e1.get()=='':
             self.bookEntries=[self.currentUser[0],0,e2.get(),e3.get()]
         else:
             self.bookEntries=[self.currentUser[0],int(e1.get()),e2.get(),e3.get()]

         

    def finalBookPathPTM(self):
        self.bookingPlat()
        if self.validDestinations(self.bookEntries[2],self.bookEntries[2]):
            self.clearWindow()
            lh=self.createLabel(self.master," Platform Booking  ",300,"#aacc22","garamond",25,0,0)
            self.elementList.append(lh)
            lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
            self.elementList.append(lf)
            b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
            self.elementList.append(b1)
            b2=self.createButton(self.master," < ",self.intermediate,10,41)
            self.elementList.append(b2)
            self.bookEntries.append(self.costPlatform(self.bookEntries[1]))
            tkcts=self.genTicketPTM(self.bookEntries)
            tktsF=tkcts.next()
            tktsB=tkcts.next()
            tkMB.showinfo('Notification','Ticket generated at '+tktsF)
            l1=self.createLabel(self.master,tktsB,300,'#ffffff','garamond',10,10,65)
            self.elementList.append(l1)
            b3=self.createButton(self.master," Home ",self.intermediate,1100,41)
            self.elementList.append(b3)
        else:
            tkMB.showerror(' Error ',' Journey Details incorrect \n Check Destinations ')
            self.bookingPlat()
        

    def userEdit(self):
         self.clearWindow()
         lh=self.createLabel(self.master," User Detail-- Editing  ",300,"#cc23dd","garamond",25,0,0)
         self.elementList.append(lh)
         lf=self.createLabel(self.master," (c) Bishal Biswas (: 1920-5201-40-02-002) [-- Project work for NIELIT course(: 1920-5201-40-02)]  ",100,None,"garamond",10,0,585)
         self.elementList.append(lf)
         b1=self.createButton(self.master," EXIT ",self.master.quit,1100,570)
         self.elementList.append(b1)
         b2=self.createButton(self.master," < ",self.dashboard,10,41)
         self.elementList.append(b2)
         l1=self.createLabel(self.master," User Name* ",30,"#7580aa","garamond",17,30,120)
         self.elementList.append(l1)
         #e1=self.createEntry(self.master," userEd ",20,'#698869',"garamond",14,170,122)
         #self.elementList.append(e1)
         l1p=self.createLabel(self.master,self.currentUser[0],20,"#eedeee","garamond",14,170,122)
         self.elementList.append(l1p)
         l2=self.createLabel(self.master," password \n ",30,"#7580aa","garamond",17,420,120)
         self.elementList.append(l2)
         e2=self.createEntryP(self.master," pasEd ",20,'#698869',"garamond",14,560,122)
         self.elementList.append(e2)
         l2p=self.createLabel(self.master,self.currentUser[1],10,"#eedeee","garamond",12,560,150)
         self.elementList.append(l2p)
         l3=self.createLabel(self.master," Full Name \n ",50,"#7580aa","garamond",17,30,200)
         self.elementList.append(l3)
         e3=self.createEntry(self.master," nameEd ",40,'#698869',"garamond",14,190,202)
         self.elementList.append(e3)
         l3p=self.createLabel(self.master,self.usr_det[self.currentUser[0]]['name'],10,"#eedeee","garamond",12,190,230)
         self.elementList.append(l3p)
         l4=self.createLabel(self.master," Address \n\n\n ",50,"#7580aa","garamond",17,30,270)
         self.elementList.append(l4)
         e4=self.createEntry(self.master," addEd ",40,'#698869',"garamond",14,190,272)
         self.elementList.append(e4)
         l4p=self.createLabelV2(self.master,self.usr_det[self.currentUser[0]]['address'],45,360,"#eedeee","garamond",12,190,300)
         self.elementList.append(l4p)
         l5=self.createLabel(self.master," Phone \n ",50,"#7580aa","garamond",17,30,390)
         self.elementList.append(l5)
         e5=self.createEntry(self.master," phoneEd ",40,'#698869',"garamond",14,190,392)
         self.elementList.append(e5)
         l5p=self.createLabel(self.master,self.usr_det[self.currentUser[0]]['phone'],10,"#eedeee","garamond",12,190,420)
         self.elementList.append(l5p)
         l6=self.createLabel(self.master," Registered ID  \n ",50,"#7580aa","garamond",17,30,460)
         self.elementList.append(l6)
         e6=self.createEntry(self.master," regidEd ",40,'#698869',"garamond",14,190,462)
         self.elementList.append(e6)
         l6p=self.createLabel(self.master,self.usr_det[self.currentUser[0]]['reg_id'],20,"#eedeee","garamond",12,190,490)
         self.elementList.append(l6p)
         b3=self.createButton(self.master," Update\nChanges ",self.commitChanges,700,450)
         self.elementList.append(b3)
         self.userE=[e2.get(),e3.get(),e4.get(),e5.get(),e6.get()]

    def commitChanges(self):
        self.userEdit()
        self.clearWindow()
        if self.userE[0] != '':
            self.usr_dct[self.currentUser[0]]=self.userE[0]
            self.currentUser[1]=self.userE[0]
        if self.userE[1] != '':
            self.usr_det[self.currentUser[0]]['name']=self.userE[1]
        if self.userE[2] != '':
            self.usr_det[self.currentUser[0]]['address']=self.userE[2]
        if self.userE[3] != '':
            self.usr_det[self.currentUser[0]]['phone']=self.userE[3]
        if self.userE[4] != '':
            self.usr_det[self.currentUser[0]]['reg_id']=self.userE[4]
        if self.userE[0] == '' and self.userE[1] == '' and self.userE[2] == '' and self.userE[3] == '' and self.userE[4] == '':
            tkMB.showinfo('Notification',' NO CHANGES MADE ')
            self.dashboard()
        else:
            self.updateUsrInfo()
            self.updateUsrDet()
            tkMB.showinfo('Notification',' Changes Registered')
            self.dashboard()
                              
    
    def destnationList(self):
        dests=str(self.info_des)
        tkMB.showinfo(' Destination List ',dests)
    
    def showClasses(self):
        clss=str(['SL','II','CC','2A','3A'])
        tkMB.showinfo(' Journey Classes ',clss)

    def clearWindow(self):
        for element in self.elementList:
            element.destroy()