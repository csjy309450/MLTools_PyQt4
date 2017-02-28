# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResizeDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
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

Dialog_ID = {
    'ID_OK': 1,
    'ID_CANCEL': 2,
}

class ResizeDialog(QtGui.QDialog):
    def __init__(self, _parent=None):
        super(ResizeDialog, self).__init__(_parent)
        self.setupUi(self)
        # self.setModal(True)
        self.returnId = self.exec_()

    def getValue(self):
        return self.returnId

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        # Dialog.resize(464, 166)
        Dialog.setFixedSize(464, 166)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Button_OK = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Button_OK.setObjectName(_fromUtf8("Button_OK"))
        self.horizontalLayout_2.addWidget(self.Button_OK)
        self.Button_Cancel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Button_Cancel.setObjectName(_fromUtf8("Button_Cancel"))
        self.horizontalLayout_2.addWidget(self.Button_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.Button_OK.clicked.connect(self.On_Button_OK)
        self.Button_Cancel.clicked.connect(self.On_Button_Cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def On_Button_OK(self, e):
        self.done(Dialog_ID['ID_OK'])

    def On_Button_Cancel(self, e):
        self.done(Dialog_ID['ID_CANCEL'])

    def GetNewSize(self):
        width = int(self.lineEdit.text())
        height = int(self.lineEdit_2.text())
        return QtCore.QSize(width, height)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "witdh", None))
        self.label_2.setText(_translate("Dialog", "height", None))
        self.Button_OK.setText(_translate("Dialog", "OK", None))
        self.Button_Cancel.setText(_translate("Dialog", "Cancel", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    a = ResizeDialog()
    sys.exit(app.exec_())

