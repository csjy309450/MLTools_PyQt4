# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copyWidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class UI_CopyForm(object):
    def __init__(self, Form):
        self.mainWid = Form
        self.setupUi(Form)

    def setupUi(self, Form):
        self.mainForm = Form
        Form.setObjectName(_fromUtf8("Form"))
        # Form.resize(self.mainWid.widSize)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(0, 0, self.mainWid.widSize.width(), self.mainWid.widSize.height())
        self.label.setObjectName(_fromUtf8("label"))
        # self.label.setText('aa')
        self.setPopMenu()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def setPopMenu(self):
        self.popmenu = QtGui.QMenu(self.mainForm)
        action_resize = QtGui.QAction("&resize", self.mainForm)
        action_exit = QtGui.QAction("&close", self.mainForm)
        self.popmenu.addActions([action_resize, action_exit])

        ## connect envent
        action_exit.triggered.connect(self.mainForm.close)
        action_resize.triggered.connect(self.createResizeWid)

    def createResizeWid(self):
        pass

    def retranslateUi(self, Form):
        # self.label.setText(_translate("Form", "TextLabel", None))
        pass
