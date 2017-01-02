#! /usr/bin/python2.7
# -*-encoding=utf-8-*-

import sys
from PyQt4 import QtGui, QtCore
import UI_SampleMainForm as ui_smf

class SampleMainWidget(QtGui.QMainWindow):
    def __init__(self):
        super(SampleMainWidget, self).__init__()
        ##初始化UI
        self.initFlag = True
        self.UI = ui_smf.UI_SampleMainForm()
        self.UI.setupUi(self)

        self.show()

    def resizeEvent(self, QResizeEvent):
        if self.initFlag:
            # addSize = QtCore.QSize(0, 0)
            self.initFlag = False
        else:
            #计算窗口增长的大小
            addSize = QResizeEvent.size()-QResizeEvent.oldSize()
            # imgSize = self.UI.qImg.size()
            #
            # newSize = self.UI.scrollArea.size() + addSize
            # if newSize.width() >= imgSize.width():
            #     addSize.setWidth(imgSize.width()-self.UI.scrollArea.size().width())
            # if newSize.height() >= imgSize.height():
            #     addSize.setHeight(imgSize.height() - self.UI.scrollArea.size().width())

            # print "addSize", addSize
            #调整scrollArea区域大小
            newGeometry = self.UI.scrollArea.geometry()
            newGeometry.setSize(self.UI.scrollArea.size() + addSize)
            self.UI.scrollArea.setGeometry(newGeometry)
            # print 'scrollArea', newGeometry
            #调整verticalLayout布局网格区域大小
            newGeometry = self.UI.verticalLayout.geometry()
            newGeometry.setSize(self.UI.verticalLayout.geometry().size() + addSize)
            self.UI.verticalLayout.setGeometry(newGeometry)
            # print "verticalLayout", newGeometry
            #调整VLayoutWidget区域大小
            newGeometry = self.UI.VLayoutWidget.geometry()
            newGeometry.setSize(self.UI.VLayoutWidget.geometry().size() + addSize)
            self.UI.VLayoutWidget.setGeometry(newGeometry)
            # print 'VLayoutWidget', newGeometry
            # self.repaint()






