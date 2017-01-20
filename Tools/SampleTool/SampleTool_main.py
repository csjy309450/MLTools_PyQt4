#! /usr/bin/python2.7
# -*-encoding=utf-8-*-

import sys
from PyQt4 import QtCore, QtGui
import  SampleMainForm as smf

class SampleToolApp:
    def __init__(self):
        self.App = QtGui.QApplication(sys.argv)
        MainApp = smf.SampleMainWidget()
        sys.exit(self.App.exec_())

def main():
    a = SampleToolApp()

if __name__=='__main__':
    main()