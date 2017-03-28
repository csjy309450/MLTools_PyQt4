# -*- coding: utf-8 -*-

import sys
import os.path as path
from functools import partial
from PyQt4 import QtGui
from PyQt4 import QtCore
import numpy as np
import SampleWidget as sw
import Tools.pyqtterm as pyqtterm

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))


class MainDockWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainDockWidget, self).__init__(parent)
        self.__setupVariables()
        self.__setupUI()
        self.show()

    def __setupVariables(self):
        self.dockWidList = []

    def __setupUI(self):
        self.setWindowTitle(self.tr("依靠窗口"))

        # 主窗口(采样窗口), SampleWidget对象
        self.sampleWidget = sw.SampleWidget()
        self.setCentralWidget(self.sampleWidget)
        self.dockWidList.append(["central", self.sampleWidget])

        # # 停靠窗口2
        # dock2 = QtGui.QDockWidget(self.tr("停靠窗口2"), self)
        # dock2.setFeatures(QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetClosable)
        # te2 = QtGui.QTextEdit(self.tr("窗口2,只可浮动"))
        # dock2.setWidget(te2)
        # self.addDockWidget(QtCeore.Qt.BottomDockWidgetArea, dock2)
        # print te2.size()
        #
        # # 停靠窗口3
        # dock3 = QtGui.QDockWidget(self.tr("停靠窗口3"), self)
        # dock3.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        # te3 = QtGui.QTextEdit(self.tr("窗口3,可在Main Window任意位置停靠，可浮动，可关闭"))
        # dock3.setWidget(te3)
        # self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock3)

        self.__setUpMenubar()

        self.resizeMainWid()

    def resizeMainWid(self):
        ## 调整窗口大小
        mainWidSize = QtCore.QSize(0, 0)
        for (key, obj) in self.dockWidList:
            if key == "bottom":
                # width = mainWidSize.width() if mainWidSize.width() >= obj.width() else mainWidSize.width()+obj.width()
                height = mainWidSize.height()+obj.height()
                mainWidSize.setWidth(width)
                mainWidSize.setHeight(height)
            elif key == "central":
                width = 600
                height = 600
                mainWidSize.setWidth(width)
                mainWidSize.setHeight(height)
            elif key == "right":
                width = mainWidSize.width() + obj.width()
                # height = mainWidSize.height() if mainWidSize.height() >= obj.height() else mainWidSize.height()+obj.height()
                mainWidSize.setWidth(width)
                mainWidSize.setHeight(height)
        self.resize(mainWidSize)


    def __setUpMenubar(self):
        action_exit = QtGui.QAction(QtGui.QIcon(), '&exit', self)
        action_exit.triggered.connect(self.close)

        action_load = QtGui.QAction(QtGui.QIcon(), '&load', self)
        action_load.setShortcut('Ctrl+1')
        action_load.triggered.connect(self.sampleWidget.On_Action_Load)

        action_next = QtGui.QAction(QtGui.QIcon(), '&next', self)
        action_next.triggered.connect(self.sampleWidget.On_Action_Next)

        action_previous = QtGui.QAction(QtGui.QIcon(), '&previous', self)
        action_previous.triggered.connect(self.sampleWidget.On_Action_Previous)

        action_screenShot_cp = QtGui.QAction(QtGui.QIcon(), '&screen shot by copy form', self)
        action_screenShot_cp.setShortcut('Ctrl+3')
        action_screenShot_cp.triggered.connect(self.sampleWidget.On_Action_ScreenShot_cp)

        action_screenShot_hd = QtGui.QAction(QtGui.QIcon(), '&screen shot by hand', self)
        action_screenShot_hd.setShortcut('Ctrl+4')
        action_screenShot_hd.triggered.connect(self.sampleWidget.On_Action_ScreenShot_hd)

        action_Start2EndArray = QtGui.QAction(QtGui.QIcon(), '&print Start 2 End Array', self)
        action_Start2EndArray.setShortcut('Ctrl+2')
        action_Start2EndArray.triggered.connect(self.sampleWidget.On_Action_Start2EndArray)

        action_dockwid_tools = QtGui.QAction(QtGui.QIcon(), '&tools window', self)
        # action_window.setShortcut('Ctrl+2')
        action_dockwid_tools.triggered.connect(self.On_Action_ShowDockTools)

        action_dockwid_terminal = QtGui.QAction(QtGui.QIcon(), '&terminal', self)
        # action_window.setShortcut('Ctrl+2')
        # action_dockwid_terminal.triggered.connect(self.On_Action_ShowDockWid)
        action_dockwid_terminal.triggered.connect(self.On_Action_ShowDockTernimal)

        action_startlabel = QtGui.QAction(QtGui.QIcon(), '&start label', self)
        # action_window.setShortcut('Ctrl+2')
        action_startlabel.triggered.connect(self.On_Action_startlabel)

        action_savelabel = QtGui.QAction(QtGui.QIcon(), '&save label', self)
        # action_window.setShortcut('Ctrl+2')
        action_savelabel.triggered.connect(self.On_Action_savelabel)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&file')
        fileMenu.addAction(action_load)
        fileMenu.addAction(action_next)
        fileMenu.addAction(action_previous)
        fileMenu.addAction(action_exit)

        windowMenu = menubar.addMenu('&window')
        windowMenu.addAction(action_dockwid_tools)
        windowMenu.addAction(action_dockwid_terminal)

        toolsMenu = menubar.addMenu('&tools')
        toolsMenu.addAction(action_screenShot_cp)
        toolsMenu.addAction(action_screenShot_hd)
        toolsMenu.addAction(action_Start2EndArray)
        toolsMenu.addAction(action_startlabel)
        toolsMenu.addAction(action_savelabel)

    def __setTerminal(self):
        ## 停靠窗口: terminal
        self.dock_term = QtGui.QDockWidget(self.tr("Terminal"), self)
        self.dock_term.setFeatures(QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetClosable)
        # term_size = (790, 200)
        term_size_ = (790, 190)
        # self.dock_term.setFixedSize(term_size[0], term_size[1])
        self.term_wid = pyqtterm.TerminalWidget(self, font_size=16, widSize=term_size_)
        self.term_wid.setMinimumSize(800, 200)
        self.dock_term.setWidget(self.term_wid)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dock_term)
        self.dockWidList.append(["bottom", self.dock_term])

        self.resizeMainWid()
    
    def __setUpDockTools(self):
        """
        停靠窗口: 工具栏
        """
        self.dock_tools = QtGui.QDockWidget(self.tr("工具栏"), self)
        self.dock_tools.setMinimumSize(300, 500) #对QTextEdit对象貌似width不能小于265
        self.dock_tools.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dock_tools.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.tools_wid = QtGui.QWidget(self.dock_tools)
        self.spinBox = QtGui.QSpinBox(self.tools_wid)
        self.spinBox.setGeometry(0, 0, 100, 20)
        button_ok = QtGui.QPushButton(QtCore.QString("ok"), self.tools_wid)
        button_ok.setGeometry(101, 0, 40, 20)
        self.dock_tools.setWidget(self.tools_wid)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dock_tools)
        self.dockWidList.append(["right", self.dock_tools])

        button_ok.clicked.connect(self.On_button_ok)

        self.resizeMainWid()

    def resizeEvent(self, QResizeEvent):
        try:
            # self.dock_term.repaint()
            self.term_wid.flash()
        except Exception,e:
            pass

    def On_Action_ShowDockTools(self, event):
        try:
            self.dock_tools.show()
        except AttributeError, e:
            self.__setUpDockTools()

    def On_Action_ShowDockTernimal(self, event):
        try:
            self.dock_term.show()
        except AttributeError, e:
            self.__setTerminal()


    def On_button_ok(self, event):
        if self.sampleWidget.filePathsList.count() == 0:
            print self.spinBox.value()
            return
        self.sampleWidget.sample_lables[self.sampleWidget.currentFrameNum] = self.spinBox.value()
        self.sampleWidget.On_Action_Next(None)
            
    
    def On_Action_startlabel(self, event):
        if self.sampleWidget.filePathsList.count() == 0:
            print "<warning> Please load samples first!"
            return 
        self.sampleWidget.sample_lables = np.empty(self.sampleWidget.filePathsList.count(), dtype=np.int16)
        self.On_Action_ShowDockWid(None)

    def On_Action_savelabel(self, event):
        if type(self.sampleWidget.sample_lables) is not np.ndarray or self.sampleWidget.sample_lables.shape[0] == 0:
            print "<warning> Please label samples first!"
            return
        save_path = path.join(path.split(str(self.sampleWidget.filePathsList[0]))[0], 'label.txt')
        f = open(save_path, 'w')
        for i in xrange(0, self.sampleWidget.sample_lables.shape[0]):
            f.write(str(self.sampleWidget.filePathsList[i])+"&&&"+str(self.sampleWidget.sample_lables[i])+"\n")
        f.close()

if __name__=='__main__':
    app = QtCore.QCoreApplication(sys.argv)
    main = MainDockWidget()
    sys.exit(app.exec_())