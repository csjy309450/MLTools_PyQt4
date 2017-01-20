#! usr/bin/python2.7
# -*-encoding=utf-8-*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import *

class ResizeForm(QtGui.QDialog):
    def __init__(self, _prarent=None):
        super(ResizeForm, self).__init__(parent=_prarent)
        self.edit_width = QtGui.QLineEdit(self)
        self.edit_height = QtGui.QLineEdit(self)
        self.button_OK = QtGui.QPushButton('OK', self)
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    a = ResizeForm()
    sys.exit(app.exec_())
