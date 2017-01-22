# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShellManager.ui'
#
# Created: Fri Aug 12 15:08:13 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import os
import os.path
from PyQt4 import QtCore, QtGui, Qt
import SM_core as sm

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ShellManager(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.smCore = sm.SM_core()
        if not self.smCore.ExtractShellDirPath():
            QtGui.QMessageBox.warning(self, QtCore.QString("Configuration Error"), QtCore.QString("Please configure the Shells' direction path!"))
            exit()
        else:
            self.setupUi()
            self.smCore.SearchShell()
            # print self.smCore.shellList
            self.AddItemtoShellList()

    def setupUi(self):
        self.setObjectName(_fromUtf8("Form_ShellManager"))
        self.resize(694, 571)
        self.QLW_comand = QtGui.QListWidget(self)
        self.QLW_comand.setGeometry(QtCore.QRect(10, 130, 361, 421))
        self.QLW_comand.setObjectName(_fromUtf8("QLW_comand"))
        self.QTE_detail = QtGui.QTextEdit(self)
        self.QTE_detail.setGeometry(QtCore.QRect(380, 130, 301, 421))
        self.QTE_detail.setObjectName(_fromUtf8("QTB_detail"))
        # self.QTE_detail.hide()
        self.QPB_run = QtGui.QPushButton(self)
        self.QPB_run.setGeometry(QtCore.QRect(20, 20, 241, 81))
        self.QPB_run.setObjectName(_fromUtf8("QPB_run"))
        self.QL_lable = QtGui.QLabel(self)
        self.QL_lable.setGeometry(QtCore.QRect(300, 20, 381, 38))
        self.QL_lable.setObjectName(_fromUtf8("QL_ShellDirPath"))
        self.QCB_shells = QtGui.QComboBox(self)
        self.QCB_shells.setGeometry(QtCore.QRect(300, 60, 381, 41))
        self.QCB_shells.setObjectName(_fromUtf8("QCB_shells"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.connect(self.QCB_shells, QtCore.SIGNAL('activated(QString)'), self.Activated)
        self.connect(self.QPB_run, QtCore.SIGNAL('clicked()'), self.OnClickedRun)

    def AddItemtoShellList(self):
        for t_shell in self.smCore.GetShells():
            self.QCB_shells.addItem(QtCore.QString(t_shell))

    def retranslateUi(self):
        self.setWindowTitle(_translate("ShellManager", "ShellManager", None))
        self.QPB_run.setText(_translate("ShellManager", "run", None))

    def Activated(self, txt):
        fileName = os.path.splitext(str(txt))
        detailFilePath = os.path.join(self.smCore.shellDirPath, fileName[0]+'.txt')
        try:
            tfile = open(detailFilePath, 'r')
            detailStr = tfile.read()
            self.QTE_detail.setText(QtCore.QString(detailStr))
        except Exception, err:
            self.QTE_detail.setText(QtCore.QString("This shell have no detail"))

    def OnClickedRun(self):
        shellPath = os.path.join(self.smCore.shellDirPath, str(self.QCB_shells.itemText(self.QCB_shells.currentIndex())))
        cmd = '/bin/sh ' + shellPath
        # print cmd
        os.system(cmd)
        print 'command is complete'

