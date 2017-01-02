# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SampleToolWidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import CopyForm as cf

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

class UI_SampleMainForm(object):
    """
    UI in Sample Tool Main Widget
    """
    def setupUi(self, Form):
        """
        初始化窗口UI
        :param Form:
        :return:
        """
        self.mainframe = Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(705, 579)

        ##对象成员变量
        # QLable控件中的显示图像
        self.qImg = QtGui.QPixmap()
        self.currentFrameNum = -1
        self.filePathsList = QtCore.QStringList()

        #获取窗口大小
        self.widRect = Form.frameGeometry()
        ##控件布局
        #定义整个垂直布局内的QWidget面板
        self.VLayoutWidget = QtGui.QWidget(Form)
        self.VLayoutWidget.setGeometry(self.widRect)
        self.VLayoutWidget.setObjectName(_fromUtf8("VLayoutWidget"))
        #定义第一层中的两个QSlider控件
        #HSlider_copyWidScale控制copyWidget窗口的尺寸
        self.HSlider_copyWidScale = QtGui.QSlider(self.VLayoutWidget)
        self.HSlider_copyWidScale.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.HSlider_copyWidScale.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider_copyWidScale.setObjectName(_fromUtf8("HSlider_copyWidScale"))
        #控制图片的分辨率
        self.HSlider_imgScale = QtGui.QSlider(self.VLayoutWidget)
        self.HSlider_imgScale.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider_imgScale.setObjectName(_fromUtf8("HSlider_imgScale"))

        # 定义滑动区域窗口内Widget面板
        self.scrollAreaWidgetContents = QtGui.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollAreaWidgetContents.setMinimumSize(1200, 1200)
        # 定义滑动区域面板内的QLabel对象
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        # self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        # self.label.setPixmap(self.img)
        # self.label.setGeometry(self.img.rect())
        # self.label.setObjectName(_fromUtf8("label"))
        # self.scrollAreaWidgetContents.setMinimumSize(self.img.size())

        #滑动区域窗口
        self.scrollArea = QtGui.QScrollArea(self.VLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        ##layout
        #定义内层布局的横向网格
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #加入之前定义的滑动条
        self.horizontalLayout.addWidget(self.HSlider_copyWidScale)
        self.horizontalLayout.addWidget(self.HSlider_imgScale)
        #按顺序定义外层布局的纵向网格
        self.verticalLayout = QtGui.QVBoxLayout(self.VLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        #按顺序加入定义好的横向网格和滑动区域对象
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.__InitMenubar()

    def __InitMenubar(self):
        action_exit = QtGui.QAction(QtGui.QIcon(), '&exit', self.mainframe)
        action_exit.triggered.connect(self.mainframe.close)

        action_load = QtGui.QAction(QtGui.QIcon(), '&load', self.mainframe)
        action_load.triggered.connect(self.On_Action_Load)

        action_next = QtGui.QAction(QtGui.QIcon(), '&next', self.mainframe)
        action_next.triggered.connect(self.On_Action_Next)

        action_previous = QtGui.QAction(QtGui.QIcon(), '&previous', self.mainframe)
        action_previous.triggered.connect(self.On_Action_Previous)

        action_screenShot = QtGui.QAction(QtGui.QIcon(), '&screen shot', self.mainframe)
        action_screenShot.triggered.connect(self.On_Action_ScreenShot)

        menubar = self.mainframe.menuBar()
        fileMenu = menubar.addMenu('&file')
        fileMenu.addAction(action_load)
        fileMenu.addAction(action_next)
        fileMenu.addAction(action_previous)
        fileMenu.addAction(action_screenShot)
        fileMenu.addAction(action_exit)

    def On_Action_Load(self, event):
        self.filePathsList = QtGui.QFileDialog.getOpenFileNames(self.mainframe, 'Open file',  '/home')
        for filePath in self.filePathsList:
            print filePath
        print self.filePathsList.count()
        self.currentFrameNum = -1
        self.On_Action_Next(None)

    def On_Action_Next(self, event):
        if self.currentFrameNum + 1 < self.filePathsList.count():
            self.currentFrameNum += 1
            self.qImg.load(self.filePathsList[self.currentFrameNum])
            self.label.setPixmap(self.qImg)
            self.label.setGeometry(self.qImg.rect())
            self.scrollAreaWidgetContents.setMinimumSize(self.qImg.size())
            # #根据图像大小调整scrollArea大小
            # geo = self.scrollArea.geometry()
            # geo.setSize(self.qImg.size())
            # self.scrollArea.setGeometry(self.scrollArea.setGeometry(geo))

        # self.mainframe.repaint()

    def On_Action_Previous(self, event):
        if self.currentFrameNum - 1 >= 0:
            self.currentFrameNum -= 1
            self.qImg.load(self.filePathsList[self.currentFrameNum])
            self.label.setPixmap(self.qImg)
            self.label.setGeometry(self.qImg.rect())
            self.scrollAreaWidgetContents.setMinimumSize(self.qImg.size())
        # self.mainframe.repaint()

    def On_Action_ScreenShot(self, event):
        self.copyForm = cf.CopyForm(self.qImg, self.label)

    def retranslateUi(self, Form):
        """
        :param Form:
        :return:
        """
        Form.setWindowTitle(_translate("Form", "Sample Tool", None))

