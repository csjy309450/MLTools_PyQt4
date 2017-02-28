# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import SampleWidget as sw
import CopyWidget as cw

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))


class MainDockWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainDockWidget, self).__init__(parent)
        self.setWindowTitle(self.tr("依靠窗口"))

        # 主窗口(采样窗口), SampleWidget对象
        self.sampleWidget = sw.SampleWidget()
        self.setCentralWidget(self.sampleWidget)

        # 停靠窗口1
        dock1 = QtGui.QDockWidget(self.tr("停靠窗口1"), self)
        dock1.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        dock1.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        te1 = QtGui.QTextEdit(self.tr("窗口1,可在Main Window的左部和右部停靠，不可浮动，不可关闭"))
        dock1.setWidget(te1)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock1)
        #
        # # 停靠窗口2
        # dock2 = QtGui.QDockWidget(self.tr("停靠窗口2"), self)
        # dock2.setFeatures(QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetClosable)
        # te2 = QtGui.QTextEdit(self.tr("窗口2,只可浮动"))
        # dock2.setWidget(te2)
        # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock2)
        #
        # # 停靠窗口3
        # dock3 = QtGui.QDockWidget(self.tr("停靠窗口3"), self)
        # dock3.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        # te3 = QtGui.QTextEdit(self.tr("窗口3,可在Main Window任意位置停靠，可浮动，可关闭"))
        # dock3.setWidget(te3)
        # self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock3)

        self.__InitMenubar()
        self.show()

    def __InitMenubar(self):
        action_exit = QtGui.QAction(QtGui.QIcon(), '&exit', self)
        action_exit.triggered.connect(self.close)

        action_load = QtGui.QAction(QtGui.QIcon(), '&load', self)
        action_load.triggered.connect(self.sampleWidget.On_Action_Load)

        action_next = QtGui.QAction(QtGui.QIcon(), '&next', self)
        action_next.triggered.connect(self.sampleWidget.On_Action_Next)

        action_previous = QtGui.QAction(QtGui.QIcon(), '&previous', self)
        action_previous.triggered.connect(self.sampleWidget.On_Action_Previous)

        action_screenShot_cp = QtGui.QAction(QtGui.QIcon(), '&screen shot by copy form', self)
        action_screenShot_cp.triggered.connect(self.sampleWidget.On_Action_ScreenShot_cp)

        action_screenShot_hd = QtGui.QAction(QtGui.QIcon(), '&screen shot by hand', self)
        action_screenShot_hd.triggered.connect(self.sampleWidget.On_Action_ScreenShot_hd)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&file')
        fileMenu.addAction(action_load)
        fileMenu.addAction(action_next)
        fileMenu.addAction(action_previous)
        fileMenu.addAction(action_screenShot_cp)
        fileMenu.addAction(action_screenShot_hd)
        fileMenu.addAction(action_exit)

if __name__=='__main__':
    app = QtCore.QCoreApplication(sys.argv)
    main = MainDockWidget()
    sys.exit(app.exec_())