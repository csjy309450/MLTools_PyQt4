# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocTree.ui'
#
# Created: Wed Aug 10 02:31:07 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_QW_DocTree(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName(_fromUtf8("Ui_QWDocTree"))
        self.resize(669, 725)
        self.treeWidget = QtGui.QTreeWidget(self)
        self.treeWidget.setGeometry(QtCore.QRect(10, 20, 641, 691))
        self.treeWidget.setObjectName(_fromUtf8("QTW_DocTree"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Document Tree", "Document Tree", None))

    def AddItemtoTreeList(self, fileName, parentItem=None):
        t_item = QtGui.QTreeWidgetItem(QtCore.QStringList(QtCore.QString(fileName)))
        if parentItem == None:
            self.treeWidget.addTopLevelItem(t_item)
        else:
            parentItem.addChild(t_item)
        return t_item

