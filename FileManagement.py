#!usr/bin/python

#
# File FileManagement.py : Class FileHandler
#   holds methods for reading a file of its contents
#   and writing data to a file 
#
class FileHandler():
    """ Class FileHandler for reading from files  and writing to files """


    def getFile(self,filename):
        """ get data from a file """
        localFile=open(filename,'r')
        contents=localFile.read()
        localFile.close()
        return contents
    
    def setFile(self,filename,details):
        """ write data to a file """
        try:
            localFile=open(filename,'w')
            localFile.write(str(details))
            localFile.close()
            return True
        except:
            return False

## end of class 