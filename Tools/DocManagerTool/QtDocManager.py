# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocManager.ui'
#
# Created: Wed Aug 10 02:30:29 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import QtDocTree as dt
from Core import DocManager

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

class Ui_QW_DocManager(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowIcon(QtGui.QIcon('DocManager.ico'))
        self.setObjectName(_fromUtf8("QW_DocManager"))
        self.setFixedSize(581, 725)
        self.QPB_Search = QtGui.QPushButton(self)
        self.QPB_Search.setGeometry(QtCore.QRect(10, 30, 147, 38))
        self.QPB_Search.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QPB_Search.setObjectName(_fromUtf8("QPB_Search"))
        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(10, 160, 561, 551))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(180, 30, 381, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 90, 451, 41))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 90, 55, 28))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.connect(self.QPB_Search, QtCore.SIGNAL("clicked()"), self.OnSearchClicked)

    def retranslateUi(self):
        self.setWindowTitle(_translate("QW_DocManager", "DocManager", None))
        self.QPB_Search.setText(_translate("QW_DocManager", "Search", None))
        self.label.setText(_translate("QW_DocManager", "filter", None))

    def GetTreeWinPos(self):
        QP_mainWinPos = self.pos()
        mainWinWidth = self.width()
        QP_mainWinPos.setX(QP_mainWinPos.x() + mainWinWidth)
        QP_mainWinPos.setY(QP_mainWinPos.y())
        return QP_mainWinPos

    def AddItemtoTreeList(self, fileName, parentItem=None):
        return self.docTree.AddItemtoTreeList(fileName, parentItem)

    def DisplayDocumentsInTreeWin(self):
        currentDir = [[None, -1]]
        for t_file in self.docCore.docList:
            # if t_file[2] == 0:
            #     if t_file[1] <= currentDir[-1][1]:
            #         while t_file[1] <= currentDir[-1][1]:
            #             del currentDir[-1]
            #     else:
            #         t_item = self.docTree.AddItemtoTreeList(t_file[0], currentDir[-1][0])
            #         currentDir.append([t_item, t_file[1]])
            # else:
            #     self.docTree.AddItemtoTreeList(t_file[0], currentDir[-1][0])
            if t_file[1] <= currentDir[-1][1]:
                while t_file[1] <= currentDir[-1][1]:
                    del currentDir[-1]
            if t_file[2] == 0:
                t_item = self.AddItemtoTreeList(t_file[0], currentDir[-1][0])
                currentDir.append([t_item, t_file[1]])
            else:
                self.AddItemtoTreeList(t_file[0], currentDir[-1][0])

    def moveEvent(self, event):
        QP_mainWinPos = self.GetTreeWinPos()
        try:
            self.docTree.move(QP_mainWinPos)
        except Exception, e:
            pass

    def OnSearchClicked(self):
        import os.path
        dirPath = self.lineEdit.text().__str__()
        if not os.path.isdir(dirPath):
            return
        self.docCore = DocManager.DocManager.DocManager()
        self.docCore.GetCatalogList(dirPath)
        print repr(self.docCore)
        self.docTree = dt.Ui_QW_DocTree()
        self.docTree.move(self.GetTreeWinPos())
        self.DisplayDocumentsInTreeWin()
        self.docTree.show()

