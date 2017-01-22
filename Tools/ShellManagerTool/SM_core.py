# -*- coding=utf-8 -*-

import os
import os.path

class SM_core:
    def __init__(self):
        self.shellList = []

    def SetShellDirPath(self, shellDirPath):
        self.shellDirPath = shellDirPath

    def ExtractShellDirPath(self):
        try:
            tfile = open('./shellDirPath.txt', 'r')
            t_Path = tfile.readline()
            self.shellDirPath = t_Path.strip('\n')
            tfile.close()
        except Exception, err:
            return False
        return True

    def SearchShell(self):
        t_shelllist = os.listdir(self.shellDirPath)
        for t_fileName in t_shelllist:
            str_path = os.path.splitext(t_fileName)
            if str_path[1] == '.sh':
                self.shellList.append(t_fileName)
            else:
                pass

    def GetShells(self):
        return self.shellList

def main():
    sm = SM_core()
    print sm.GetShells()
    print __file__

if __name__ == '__main__':
    main()

