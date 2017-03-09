#! /usr/bin/python2.7
# -*-encoding=utf-8-*-

import sys
import os.path as path
import numpy as np
from PyQt4 import QtGui, QtCore
import CopyWidget as cw
import ImgLabel as il

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
    
Mode_ScreenShot = {
    'Mode_None': 0,
    'Mode_CopyWidgetShot': 1,
    'Mode_HandShot': 2,
    }

class SampleWidget(QtGui.QWidget):
    def __init__(self):
        super(SampleWidget, self).__init__()
        ##初始化UI
        self.initialMemberVairables()
        self.setupUi()

    def initialMemberVairables(self):
        # QLable控件中的显示图像
        self.qImg = QtGui.QPixmap()
        self.filePathsList = QtCore.QStringList()
        self.sample_lables = None
        self.currentFrameNum = -1
        self.initFlag = True
        self.screenShotFlag = Mode_ScreenShot['Mode_None']

    def setupUi(self):
        """
        初始化窗口UI
        :param Form:
        :return:
        """
        self.setObjectName(_fromUtf8("SampleWidget"))
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(500, 500)
        # self.setFixedSize(400, 400)
        # self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        # self.setFixedSize(100, 100)

        ##对象成员变量

        #获取窗口大小
        self.widRect = self.frameGeometry()

        ##控件布局
        #定义整个垂直布局内的QWidget面板
        self.VLayoutWidget = QtGui.QWidget(self)
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
        self.HSlider_imgScale.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.HSlider_imgScale.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider_imgScale.setObjectName(_fromUtf8("HSlider_imgScale"))

        # 定义滑动区域窗口内Widget面板
        self.scrollAreaWidgetContents = QtGui.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollAreaWidgetContents.setMinimumSize(100, 100)
        # 定义滑动区域面板内的QLabel对象
        self.label = il.ImgLabel(self.scrollAreaWidgetContents)
        self.label.setText(QtCore.QString('a test'))
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

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def __getScorllAreaClientSize(self):
        return self.UI.scrollArea.size() - QtCore.QSize(self.UI.scrollArea.verticalScrollBar().width(),
                                                        self.UI.scrollArea.horizontalScrollBar().height())

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

            # print "addSize", addSize
            #调整scrollArea区域大小
            newGeometry = self.scrollArea.geometry()
            newGeometry.setSize(self.scrollArea.size() + addSize)
            self.scrollArea.setGeometry(newGeometry)
            # print 'scrollArea', newGeometry
            #调整verticalLayout布局网格区域大小
            newGeometry = self.verticalLayout.geometry()
            newGeometry.setSize(self.verticalLayout.geometry().size() + addSize)
            self.verticalLayout.setGeometry(newGeometry)
            # print "verticalLayout", newGeometry
            #调整VLayoutWidget区域大小
            newGeometry = self.VLayoutWidget.geometry()
            newGeometry.setSize(self.VLayoutWidget.geometry().size() + addSize)
            self.VLayoutWidget.setGeometry(newGeometry)
            # print 'VLayoutWidget', newGeometry
            # self.repaint()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.text() == 'e':
            self.On_Action_Next(None)
            # self._sinal.myEmit()
        elif QKeyEvent.text() == 'q':
            self.On_Action_Previous(None)
            
    def On_Action_Load(self, event):
        self.filePathsList = QtGui.QFileDialog.getOpenFileNames(self, 'Open file', '/home/yangzheng/testData/ucsd')
        for filePath in self.filePathsList:
            print filePath
        # print self.filePathsList.count()
        self.currentFrameNum = -1
        self.On_Action_Next(None)

    def On_Action_Next(self, event):
        if self.currentFrameNum + 1 < self.filePathsList.count():
            self.currentFrameNum += 1
            self.showImage()
            self.parent().setWindowTitle(self.filePathsList[self.currentFrameNum])
        else:
            print "<warning> Has already reached the end!"
        self.repaint()
        try:
            self.copyForm.UpdateImg()
        except Exception, e:
            pass

    def On_Action_Previous(self, event):
        if self.currentFrameNum - 1 >= 0:
            self.currentFrameNum -= 1
            self.showImage()
            self.parent().setWindowTitle(self.filePathsList[self.currentFrameNum])
        else:
            print "<warning> Has already reached the initiate!"
        self.repaint()
        try:
            self.copyForm.UpdateImg()
        except Exception, e:
            pass

    def On_Action_ScreenShot_cp(self, event):
        self.screenShotFlag = Mode_ScreenShot['Mode_CopyWidgetShot']
        self.label.setScreenShotMode(self.screenShotFlag)
        self.copyForm = cw.CopyForm(self.qImg, self.scrollArea)
        # self.connect(self.copyForm._sinal, QtCore.SIGNAL('Signal_Key(PyQt_PyObject)'),
        #                       self, QtCore.SLOT("On_Key_CopyForm(PyQt_PyObject)"))
        self.connect(self.copyForm, QtCore.SIGNAL('Signal_Key(PyQt_PyObject)'),
                              self, QtCore.SLOT("On_Key_CopyForm(PyQt_PyObject)"))

    def On_Action_ScreenShot_hd(self, event):
        self.screenShotFlag = Mode_ScreenShot['Mode_HandShot']
        self.label.setScreenShotMode(self.screenShotFlag)

    def On_Action_Start2EndArray(self, event):
        a = self.label.getStart2EndArray()
        result = np.empty((0, 4), dtype=np.int16)
        for it in a:
            result = np.row_stack([result, [(it[0].x()+it[1].x()+1)/2, (it[0].y()+it[1].y()+1)/2, abs(it[0].x()-it[1].x()),
                           abs(it[0].y()-it[1].y())]])

        filePath = path.splitext(str(self.filePathsList[self.currentFrameNum]))[0]
        np.save(filePath + '.npy', result)
        # print a
        print result
        print filePath + '.npy'


    # def On_MousePress(self, event):
    #     print event

    def On_Key_CopyForm(self, _key):
        # print _key
        if _key == 'e':
            self.On_Action_Next(None)
        elif _key == 'q':
            self.On_Action_Previous(None)
        else:
            pass

    def setPixmap(self, qImg):
        self.label.resetStart2EndArray()
        self.label.setPixmap(qImg)
        self.label.setGeometry(qImg.rect())

    def showImage(self):
        dis = (abs(self.horizontalLayout.geometry().left() - 0),
               abs(self.horizontalLayout.geometry().right() - self.width()),
               abs(self.horizontalLayout.geometry().top() - 0),
               abs(self.height() - self.scrollArea.geometry().bottom()))
        #从文件夹加载图像
        self.qImg.load(self.filePathsList[self.currentFrameNum])
        #显示到QLabel对象，并调整QLabel对象的尺寸为图像尺寸
        self.setPixmap(self.qImg)
        # #设置 QScrollArea 对象中 QWidget 区域的大小
        self.scrollAreaWidgetContents.setMinimumSize(self.qImg.size())
        # # #根据图像大小调整scrollArea大小
        self.scrollArea.setMaximumSize(self.qImg.size() + QtCore.QSize(self.scrollArea.verticalScrollBar().width(),
                                                                       self.scrollArea.horizontalScrollBar().height()))
        #求当前图像对象的基础上窗口允许的最大尺寸
        # print self.horizontalLayout.geometry()
        # print self.size()
        # print self.scrollArea.geometry()
        # print dis
        self.setMaximumSize(self.scrollArea.maximumSize() + QtCore.QSize(
            dis[0]+dis[1], self.HSlider_imgScale.height()+dis[2]+dis[3]))

    def get_file_list(self):
        return self.filePathsList

    def get_sampleLabels(self):
        return self.sample_lables

    def retranslateUi(self, Form):
        """
        :param Form:
        :return:
        """
        Form.setWindowTitle(_translate("Form", "Sample Tool", None))

if __name__=='__main__':
    App = QtGui.QApplication(sys.argv)
    MainApp = SampleWidget()
    sys.exit(App.exec_())






