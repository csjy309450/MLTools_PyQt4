#-*-encoding=utf-8-*-

import copy
import time
from PyQt4 import QtCore
from PyQt4 import QtGui
import SampleWidget as sw

class ImgLabel(QtGui.QLabel):
    def __init__(self, _parent=None):
        super(ImgLabel, self).__init__(_parent)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.screenShot_flage = sw.Mode_ScreenShot['Mode_None']
        self.mouseDrage = False
        self.updateImgFlag = False
        self.Start2EndArray = []
        self.current_mouse_Start2End = [None, None]
        self.currentImg = None
        self.currentImg_copy = None

    def setScreenShotMode(self, _mode):
        self.screenShot_flage = _mode

    def setPixmap(self, QPixmap):
        self.currentImg = QPixmap.copy()
        self.currentImg_copy = QPixmap.copy()
        super(ImgLabel, self).setPixmap(self.currentImg_copy)
        pass
        # self.currentImg_copy = QPixmap.copy()
        # self.currentImg_copy_copy = QPixmap.copy()

    def resetStart2EndArray(self):
        self.Start2EndArray = []

    def getStart2EndArray(self):
        return self.Start2EndArray

    def mousePressEvent(self, QMouseEvent):
        super(ImgLabel, self).mousePressEvent(QMouseEvent)
        lableGeo = self.geometry()
        mousePos = QMouseEvent.pos()
        if self.screenShot_flage == sw.Mode_ScreenShot['Mode_HandShot']:
            self.current_mouse_Start2End[0] = mousePos
            self.mouseDrage = True
        elif self.screenShot_flage == sw.Mode_ScreenShot['Mode_PointLabel']:
            self.current_mouse_Start2End[0] = mousePos
        else:
            pass

    def mouseMoveEvent(self, QMouseEvent):
        super(ImgLabel, self).mouseMoveEvent(QMouseEvent)
        mousePos = QMouseEvent.pos()
        if self.mouseDrage == True:
            self.current_mouse_Start2End[1] = mousePos
            self.updateImgFlag = True
            self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        super(ImgLabel, self).mouseReleaseEvent(QMouseEvent)
        mousePos = QMouseEvent.pos()
        if self.screenShot_flage == sw.Mode_ScreenShot['Mode_HandShot'] and self.mouseDrage == True:
            self.current_mouse_Start2End[1] = mousePos
            self.mouseDrage = False
            # print self.current_mouse_Start2End
            if self.current_mouse_Start2End[0].x() != self.current_mouse_Start2End[1].x() and \
                self.current_mouse_Start2End[0].y() != self.current_mouse_Start2End[1].y():
                self.Start2EndArray.append([self.current_mouse_Start2End[0], self.current_mouse_Start2End[1]])
                self.currentImg = self.currentImg_copy.copy()
                self.setPixmap(self.currentImg)
                self.update()
            # print self.current_mouse_Start2End
        elif self.screenShot_flage == sw.Mode_ScreenShot['Mode_PointLabel'] and self.mouseDrage == False:
            if mousePos.x() == self.current_mouse_Start2End[0].x() and \
                mousePos.y() == self.current_mouse_Start2End[0].y():
                self.Start2EndArray.append(mousePos)
                self.updateImgFlag = True
                self.update()
        else:
            pass
        
    def paintEvent(self, QPaintEvent):
        super(ImgLabel, self).paintEvent(QPaintEvent)
        go = False
        if self.updateImgFlag == True and self.screenShot_flage==sw.Mode_ScreenShot['Mode_HandShot']:
            self.currentImg_copy = self.currentImg.copy() #浅拷贝,没法深拷贝
            qp = QtGui.QPainter()
            qp.begin(self.currentImg_copy)
            pen = QtGui.QPen(QtGui.QColor(255, 0, 0))
            pen.setWidth(2)
            qp.setPen(pen)
            drawRect = QtCore.QRect(self.current_mouse_Start2End[0].x(),
                                    self.current_mouse_Start2End[0].y(),
                                    self.current_mouse_Start2End[1].x() - self.current_mouse_Start2End[0].x(),
                                    self.current_mouse_Start2End[1].y() - self.current_mouse_Start2End[0].y())
            qp.drawRect(drawRect)
            qp.end()
            # self.setPixmap(self.currentImg_copy)
            self.updateImgFlag = False
        elif self.updateImgFlag == True and self.screenShot_flage==sw.Mode_ScreenShot['Mode_PointLabel']:
            qp = QtGui.QPainter()
            qp.begin(self.currentImg)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0), QtCore.Qt.SolidPattern)
            qp.setBrush(brush)
            qp.drawEllipse(self.current_mouse_Start2End[0], 2, 2)
            qp.end()
            self.updateImgFlag = False
            self.setPixmap(self.currentImg)
        else:
            pass
        