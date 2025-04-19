import os
import platform

class Config:
    def __init__(self):
        # platform specific configuration:
        # TODO: load configuration from external file
        self.imgdir = "img"
        if os.sys.platform == 'win32':
            self.device = "com34"
#            self.datFile = 'C:/Documents and Settings/ondro/VirtualBox shared folder/knitting/knitting_machine-master/img/zaloha vzory stroj python.dat'
            self.datFile = '' # Use empty string for Windows default.  Used to be file-06.dat
            self.simulateEmulator = True
        else:
            self.device = "/dev/ttyUSB0"
            self.datFile = "img/file-01.dat"
            self.simulateEmulator = False
        
    def getDatFile(self):
        return self.datFile
    
    def getDevice(self):
        return self.device