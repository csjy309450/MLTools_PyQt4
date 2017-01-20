#! /usr/bin/python2.7
# -*-encoding=utf-8-*-

from PyQt4 import QtGui
from PyQt4 import QtCore

##暂时没用

class KeySingnal(QtCore.QObject):
    def __init__(self):
        super(KeySingnal, self).__init__()
        self.__msg = ''

    def myEmit(self, msg):
        self.__msg = msg
        self.emit(QtCore.SIGNAL("Signal_Key(PyQt_PyObject)"), msg)

    def preMessage(self):
        return self.__msg