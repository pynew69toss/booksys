# -*- coding: utf-8 -*-

import os


class readFile:
    
    def __init__(self):
        self.data = []

        
    def readpath(self,path):
        for root, dirs, files in os.walk(path,True):
            print('root: %s' % root)
            print('dirs: %s' % dirs)
            print('files: %s' % files)
            print (' ')
            if len(files) == 0:
                pass
            else:
                print(self.get_filePath_fileName_fileExt(files))


    def get_filePath_fileName_fileExt(self,filename):
        (filepath,tempfilename) = os.path.split(filename[0])
        (shotname,extension) = os.path.splitext(tempfilename)
        return filepath,shotname,extension

