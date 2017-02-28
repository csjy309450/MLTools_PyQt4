#! /usr/bin/python2.7
# -*-encoding=utf-8-*-

import sys
from PyQt4 import QtCore, QtGui
import MainDocWidget as mdw

class SampleToolApp:
    def __init__(self):
        self.App = QtGui.QApplication(sys.argv)
        MainApp = mdw.MainDockWidget()
        sys.exit(self.App.exec_())

def main():
    app = SampleToolApp()

if __name__=='__main__':
    main()