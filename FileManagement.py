#!usr/bin/python

class FileHandler():

    def getFile(self,filename):
        localFile=open(filename,'r')
        contents=localFile.read()
        localFile.close()
        return contents
    
    def setFile(self,filename,details):
        try:
            localFile=open(filename,'w')
            localFile.write(str(details))
            localFile.close()
            return True
        except:
            return False

