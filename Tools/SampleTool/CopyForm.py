#! usr/bin/python2.7
# -*-encoding=utf-8-*-

from PyQt4 import QtGui, QtCore
from PyQt4.Qt import *
import UI_CopyForm as uicf
import mySignal

class CopyForm(QtGui.QWidget):
    def __init__(self,_qImg, _parent=None, _widSize=QtCore.QSize(100, 100)):
        super(CopyForm, self).__init__(parent=_parent)
        self.parentqImg = _qImg
        self.parentWid = _parent
        self.setAutoFillBackground(True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.widSize = _widSize
        self.updateImgFlag = False
        self.setGeometry(0, 0, self.widSize.width(), self.widSize.height())

        #self._sinal = mySignal.mySingnal('e')

        # print self.parentClientSize

        self.ui = uicf.UI_CopyForm(self)
        self.repaint()
        ## 设置窗口焦点风格，设置之后才能获取键盘事件
        self.setFocusPolicy(Qt.StrongFocus)

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
            self.__moveTo(newPos)
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

    def __moveTo(self, _newPos):
        """
        将窗口移动至指定位置
        :param _newPos:
        :return:
        """
        newPos = _newPos
        ## 判断新的位置会不会超出父窗口边界
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

    def resizeEvent(self, QResizeEvent):
        self.repaint()

    def keyPressEvent(self, QKeyEvent):
        """
        键盘事件槽
        :param QKeyEvent:
        :return:
        """
        # print QKeyEvent.text(), QKeyEvent.key()
        if QKeyEvent.text() == 'w':
            new_pos = self.pos()+QtCore.QPoint(0, -2)
            self.__moveTo(new_pos)
        elif QKeyEvent.text() == 'a':
            new_pos = self.pos() + QtCore.QPoint(-2, 0)
            self.__moveTo(new_pos)
        elif QKeyEvent.text() == 's':
            new_pos = self.pos() + QtCore.QPoint(0, 2)
            self.__moveTo(new_pos)
        elif QKeyEvent.text() == 'd':
            new_pos = self.pos() + QtCore.QPoint(2, 0)
            self.__moveTo(new_pos)
        elif QKeyEvent.text() == 'e':
            self.emit(QtCore.SIGNAL("Signal_Key(PyQt_PyObject)"), 'e')
            # self._sinal.myEmit()
        elif QKeyEvent.text() == 'q':
            self.emit(QtCore.SIGNAL("Signal_Key(PyQt_PyObject)"), 'q')
        elif QKeyEvent.text() == 'f':
            pass
        else:
            pass
