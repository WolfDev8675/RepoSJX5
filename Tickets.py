#!usr/bin/python

# File Tickets.py : Class Ticket
# holds methods for ticket generation provided 
# that the rates for the tickets are predefined 
# 

import random as Rn
class Ticket():
    """ Class Ticket for handling ticket generation """
    
    __Tid=[]

    def __init__(self,Tid=None):
        """ Default unlinked usage initialization """
        if Tid == None:
            self.__Tid=self.idGen()
        else:
            self.__Tid=Tid

    def idGen(self):
        """ Generate a 10 digit ID """
        idLocal=10**10 * Rn.random() 
        idLocal=str(int(idLocal))
        self.__Tid=idLocal
        return self.__Tid
    
    def costNormal(self,data=[]):
        """ Generate a Normal Ticket price/cost """
        nAd=data[0]
        nC=data[1]
        nPD=data[2]
        nSc=data[3]
        coachT=data[4]
        dst=data[5]
        if dst<3:dst=3
        if dst<5 and dst>3:dst=5
        if dst<8 and dst>5:dst=8
        if dst<10 and dst>8:dst=10
        ## rate of tickets
        rate={'2A':{3:500,5:1000,8:1500,10:2000},'II':{3:5,5:10,8:15,10:20},'CC':{3:50,5:100,8:150,10:200},'SL':{3:75,5:150,8:225,10:300},'3A':{3:175,5:250,8:325,10:400}}
        tA=nAd*rate[coachT][dst]*1.00
        tC=nC*(rate[coachT][dst]*1.00/2.00)
        tPD=nPD*(0.35*rate[coachT][dst])
        tSc=nSc*(0.4*rate[coachT][dst])
        cost=tA+tC-tPD-tSc
        return cost

    def costPlatform(self,nIndv):
        """ Generate Platform ticket cost """
        return nIndv*5.00

    def genTicketNRM(self,data=[]):
        """ Generate a Normal Ticket for a passenger """
        user=data[0]
        nAd=data[1]
        nC=data[2]
        nPD=data[3]
        nSc=data[4]
        coachT=data[5]
        dst=data[6]
        desS=data[7]
        desE=data[8]
        payGate=data[9]
        tpay=data[10]
        dst=dst*5
        idLocal=self.idGen()
        bill='AUTOMATED TICKET GENERATED \n '+''.center(80,'-')+' \n'
        bill+='Ticket ID : '+idLocal+'\n'
        bill+= 'Ticket for : '+ user + '\n'
        bill+=' Coach class :: '+coachT+'\n'
        bill+=' Number of Adults   : ' + str(nAd)+'\n'
        bill+=' Number of Children : ' + str(nC)+'\n'
        bill+=' Persons with Disability (concession) : '+ str(nPD) +'\n'
        bill+=' Senior Citizen(concession) : '+str(nSc)+'\n'
        bill+='\n\n\n\n'
        bill+=' Starting Destination :: '+desS+'\n'
        bill+=' Ending Destination :: '+desE+'\n'
        bill+=' Journey Distance '+str(dst)+'km \n'
        bill+=' Total Payment :: '+str(tpay)+'\n'
        bill+=' Payment Gateway :: '+payGate+'\n\n\n\n'
        bill+='HAPPY JOURNEY \n'

        filename='TK#'+idLocal+'.doc'       ## generate a ticket file 
        f=open(filename,'w')
        f.write(bill)
        f.close()
        yield filename
        yield bill

    def genTicketPTM(self,data=[]):
        """ Generate a platform tiket """
        user=data[0]
        nIndv=data[1]
        des=data[2]
        payGate=data[3]
        tpay=data[4]
        idLocal=self.idGen()
        bill='AUTOMATED TICKET GENERATED \n '+''.center(80,'-')+' \n'
        bill+='Ticket ID : '+idLocal+'\n'
        bill+= 'Ticket for : '+ user + '\n'
        bill+='\n\n\n\n'
        bill+=' Number of Individuals :: '+str(nIndv)+'\n'
        bill+=' PLATFORM TICKET FOR :: '+des+'\n'
        bill+=' Total Payment :: '+str(tpay)+'\n'
        bill+=' Payment Gateway :: '+payGate+'\n\n\n\n'
        bill+='HAPPY JOURNEY \n'

        filename='TK#'+idLocal+'.doc'           ## generate ticket file 
        f=open(filename,'w')
        f.write(bill)
        f.close()
        yield filename
        yield bill

## end of Class  



#Example of raw operation for platform ticket
#t=Ticket()
#t.genTicketPTM('user',3,'SDAH',10,'15648@apl')


#Example of raw operation for normal ticket
#t=Ticket()
#t.genTicketNRM('user',2,3,0,0,'II',500,'KOL','SDAH',560,'15648@apl')

