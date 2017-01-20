#! /usr/bin/python2.7
# -*-encoding=utf-8-*-

import sys
from PyQt4 import QtGui, QtCore
import UI_SampleMainForm as ui_smf
import mySignal

class SampleMainWidget(QtGui.QMainWindow):
    def __init__(self):
        super(SampleMainWidget, self).__init__()
        ##初始化UI
        self.initFlag = True
        self.UI = ui_smf.UI_SampleMainForm()
        self.UI.setupUi(self)

        self.show()

    def __getScorllAreaClientSize(self):
        return self.UI.scrollArea.size() - QtCore.QSize(self.UI.scrollArea.verticalScrollBar().width(),
                                                        self.UI.scrollArea.horizontalScrollBar().height())

    @QtCore.pyqtSlot("PyQt_PyObject")
    def On_Key_CopyForm(self, _key):
        # print _key
        if _key == 'e':
            self.UI.On_Action_Next(None)
        elif _key == 'q':
            self.UI.On_Action_Previous(None)
        else:
            pass

    def resizeEvent(self, QResizeEvent):
        if self.initFlag:
            # addSize = QtCore.QSize(0, 0)
            self.initFlag = False
        else:
            #计算窗口增长的大小
            addSize = QResizeEvent.size()-QResizeEvent.oldSize()

            # 限制窗口增大的尺寸
            # imgSize = self.UI.qImg.size()
            # scorllAreaClientSize = self.__getScorllAreaClientSize()
            # newSize = scorllAreaClientSize + addSize
            # if scorllAreaClientSize.width() >= imgSize.width() :
            #     # self.setMaximumWidth(imgSize.width()+130)
            #     if newSize.width() < imgSize.width():
            #         pass
            #     else:
            #         addSize.setWidth(0)
            # elif scorllAreaClientSize.width() < imgSize.width() and newSize.width() >= imgSize.width():
            #     addSize.setWidth(imgSize.width()-scorllAreaClientSize.width())
            # else:
            #     pass
            #
            # if scorllAreaClientSize.height() == imgSize.height():
            #     # self.setMaximumHeight(imgSize.height()+180)
            #     if newSize.height() < imgSize.height():
            #         pass
            #     else:
            #         addSize.setHeight(0)
            #
            # elif scorllAreaClientSize.height() < imgSize.height() and newSize.height() >= imgSize.height():
            #     addSize.setHeight(imgSize.height() - scorllAreaClientSize.height())
            # else:
            #     pass

            # if addSize == QtCore.QSize(0, 0):
            #     return

            print "addSize", addSize
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






