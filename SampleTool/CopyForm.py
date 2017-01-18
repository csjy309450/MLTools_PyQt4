#! usr/bin/python2.7
# -*-encoding=utf-8-*-

from PyQt4 import QtGui, QtCore
from PyQt4.Qt import *
import UI_CopyForm as uicf

class CopyForm(QtGui.QWidget):
    def __init__(self, _qImg, _parent=None, _widSize=QtCore.QSize(100, 100)):
        super(CopyForm, self).__init__(parent=_parent)
        self.parentqImg = _qImg
        self.parentWid = _parent
        self.setAutoFillBackground(True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.widSize = _widSize
        self.updateImgFlag = False
        self.setGeometry(0, 0, self.widSize.width(), self.widSize.height())

        # print self.parentClientSize

        self.ui = uicf.UI_CopyForm(self)

        self.show()

    def __getParentClientSize(self):
        self.parentClientSize = self.parentWid.size() - QtCore.QSize(
            self.parentWid.verticalScrollBar().width(),
            self.parentWid.horizontalScrollBar().height())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__getParentClientSize()
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()
            # print self.frameGeometry().topLeft()
        elif event.button() == Qt.RightButton:
            # print event
            self.ui.popmenu.exec_(event.globalPos())

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            newPos = event.globalPos() - self.dragPosition
            # print 'newPos', newPos
            if newPos.x() <= 0:
                newPos.setX(0)
            elif newPos.x() >= (self.parentClientSize.width() - self.width()):
                # print self.parentWid.geometry()
                # print self.parentClientSize
                newPos.setX(self.parentClientSize.width() - self.width())
            if newPos.y() <= 0:
                newPos.setY(0)
            elif newPos.y() >= (self.parentClientSize.height() - self.height()):
                newPos.setY(self.parentClientSize.height() - self.height())

            self.move(newPos)
            self.UpdateImg()
            event.accept()

    def UpdateImg(self):
        # print self.geometry()
        self.subImg = self.parentqImg.copy(self.geometry())
        self.updateImgFlag = True
        self.repaint()
        self.ui.label.setPixmap(self.subImg)


    def paintEvent(self, QPaintEvent):
        if self.updateImgFlag:
            qp = QtGui.QPainter()
            qp.begin(self.subImg)
            pen = QtGui.QPen(QtGui.QColor(255, 0, 0))
            pen.setWidth(2)
            qp.setPen(pen)
            drawRect = self.rect()
            drawRect.setBottom(drawRect.bottom() - 2)
            drawRect.setRight(drawRect.right() - 2)
            qp.drawRect(drawRect)
            qp.end()
            self.updateImgFlag = False
