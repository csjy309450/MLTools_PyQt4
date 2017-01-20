# -*- coding: utf-8 -*-

import sys
from PyQt4 import  QtGui, QtCore
import QtDocManager as dm

def main():
    app = QtGui.QApplication(sys.argv)
    win = dm.Ui_QW_DocManager()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()