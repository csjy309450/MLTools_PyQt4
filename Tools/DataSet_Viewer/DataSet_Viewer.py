#!/usr/bin/python2.7
# -*-encoding=utf-8-*-

import h5py as h5
import numpy as np
import DataSet as ds
import sys
import cv2
from PyQt4 import QtGui
from PyQt4 import QtCore
import copy as cp
import qimage2ndarray as q2d

class QShowWid(QtGui.QWidget):
    def __init__(self, _img_win_size=(100,100), _n_show_sample=1, _parent=None):
        QtGui.QWidget.__init__(self, _parent)
        self.sub_img_win_size = _img_win_size
        self.n_show_sample = _n_show_sample
        self.l_frame = []
        self.l_edge = []
        self.l_optflow = []
        self.l_texture = []
        self.l_label = []
        self.win_size = (0, 0)
        self.__make_img_wid()
        self.__load_default_Image()

    def __load_default_Image(self):
        cv_img = cv2.imread('test.png', cv2.CV_8UC1)
        cv_img = cv2.resize(cv_img, (self.sub_img_win_size[0], self.sub_img_win_size[1]))
        qt_image = q2d.gray2qimage(cv_img)
        for i in xrange(self.n_show_sample):
            self.l_frame[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))
            self.l_edge[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))
            self.l_optflow[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))
            self.l_texture[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))
            self.l_label[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))

    def __make_img_wid(self):
        for i in xrange(self.n_show_sample):
            self.l_frame.append(QtGui.QLabel('frame', parent=self))
            self.l_frame[i].setGeometry(0 * (self.sub_img_win_size[0] + 1) + 10,
                                        i * (self.sub_img_win_size[1] + 1) + 10,
                                        self.sub_img_win_size[0],
                                        self.sub_img_win_size[1])
            self.l_edge.append(QtGui.QLabel('edge', parent=self))
            self.l_edge[i].setGeometry(1 * (self.sub_img_win_size[0] + 1) + 10,
                                       i * (self.sub_img_win_size[1] + 1) + 10,
                                       self.sub_img_win_size[0],
                                       self.sub_img_win_size[1])
            self.l_optflow.append(QtGui.QLabel('optflow', parent=self))
            self.l_optflow[i].setGeometry(2 * (self.sub_img_win_size[0] + 1) + 10,
                                          i * (self.sub_img_win_size[1] + 1) + 10,
                                          self.sub_img_win_size[0],
                                          self.sub_img_win_size[1])
            self.l_texture.append(QtGui.QLabel('texture', parent=self))
            self.l_texture[i].setGeometry(3 * (self.sub_img_win_size[0] + 1) + 10,
                                          i * (self.sub_img_win_size[1] + 1) + 10,
                                          self.sub_img_win_size[0],
                                          self.sub_img_win_size[1])
            self.l_label.append(QtGui.QLabel('label', parent=self))
            self.l_label[i].setGeometry(4 * (self.sub_img_win_size[0] + 1) + 10,
                                        i * (self.sub_img_win_size[1] + 1) + 10,
                                        self.sub_img_win_size[0],
                                        self.sub_img_win_size[1])
        self.win_size = (5 * (self.sub_img_win_size[0] + 1) + 20,
                         self.n_show_sample * (self.sub_img_win_size[1] + 1) + 20)
        self.resize(self.win_size[0], self.win_size[1])

    def darr_interval_mapping(self, _src, _src_inter, _dis_inter):
        t_src = _src.astype(np.float32)
        _dis = (t_src-_src_inter[0])/(_src_inter[1]-_src_inter[0]) * (_dis_inter[1]-_dis_inter[0]) + _dis_inter[0]

        return _dis.astype(np.uint8)

    def darr_label(self, _src):
        _dis = np.zeros((_src.shape[0], _src.shape[1]), dtype=np.uint8)
        for i in xrange(_src.shape[0]):
            for j in xrange(_src.shape[1]):
                if _src[i,j]>0.001:
                    _dis[i,j]=255
        return _dis

    def darr_optflow(self, _src_x, _src_y):
        assert (_src_x.shape[0] == _src_y.shape[0] and _src_x.shape[1] == _src_y.shape[1])
        _dis = np.zeros((_src_x.shape[0], _src_x.shape[1]), dtype=np.uint8)
        t_dis = np.sqrt(np.power(_src_x, 2)+np.power(_src_y, 2))
        for i in xrange(t_dis.shape[0]):
            for j in xrange(t_dis.shape[1]):
                if abs(t_dis[i,j]) > 0.5:
                    _dis[i,j] = 255
        return _dis

    def _update_img_label_core(self, _ndarr_img, _ndarr2qimage):
        for i in xrange(self.n_show_sample):
            ##
            img = self.darr_interval_mapping(_ndarr_img[i][0], (0, 1), (0, 255))
            img = cv2.resize(img, (self.sub_img_win_size[0], self.sub_img_win_size[1]))
            # cv2.imshow('img', img)
            qt_image = _ndarr2qimage(img)
            self.l_frame[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))
            ##
            img = self.darr_interval_mapping(_ndarr_img[i][1], (0, 1), (0, 255))
            img = cv2.resize(img, (self.sub_img_win_size[0], self.sub_img_win_size[1]))
            qt_image = _ndarr2qimage(img)
            # cv2.imshow('edge', img)
            self.l_edge[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))
            ##
            img = self.darr_optflow(_ndarr_img[i][2], _ndarr_img[i][3])
            img = cv2.resize(img, (self.sub_img_win_size[0], self.sub_img_win_size[1]))
            qt_image = _ndarr2qimage(img)
            # cv2.imshow('optflow', img)
            self.l_optflow[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))
            ##
            img = self.darr_interval_mapping(_ndarr_img[i][4], (0, 1), (0, 255))
            img = cv2.resize(img, (self.sub_img_win_size[0], self.sub_img_win_size[1]))
            qt_image = _ndarr2qimage(img)
            # cv2.imshow('texture', img)
            self.l_texture[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))
            ##
            img = self.darr_label(_ndarr_img[i][5])
            img = cv2.resize(img, (self.sub_img_win_size[0], self.sub_img_win_size[1]))
            # cv2.imshow('label', img)
            qt_image = _ndarr2qimage(img)
            self.l_label[i].setPixmap(QtGui.QPixmap.fromImage(qt_image))

    def update_img_label(self, _ndarr_img):
        assert (type(_ndarr_img) is np.ndarray) and \
               (_ndarr_img.shape[0] == self.n_show_sample) and \
               (_ndarr_img.shape[1] == 6)
        if len(_ndarr_img.shape) == 5: # 3 channal image (RGB)
            self._update_img_label_core(_ndarr_img, q2d.array2qimage)
        elif len(_ndarr_img.shape) == 4:
            self._update_img_label_core(_ndarr_img, q2d.gray2qimage)
        else:
            pass

class DS_Viewer(QtGui.QWidget):
    def __init__(self, path, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.path = path
        print path
        self.n_show_sample = 11
        self.img_win_size = (50, 50)

        self.setWindowTitle('DS Viewer')
        self.button_next = QtGui.QPushButton('next', self)
        self.button_next.move(85, 0)
        self.button_next.setShortcut('S')
        self.button_prior = QtGui.QPushButton('prior', self)
        self.button_prior.setShortcut('A')
        self.ld_nframe = QtGui.QLineEdit(parent=self)
        self.ld_nframe.move(170, 0)
        self.l_message = QtGui.QLabel('message', parent=self)
        self.l_message.setGeometry(0,30,500,30)
        self.l_message.setText(QtCore.QString('default image'))
        self.wid_img = QShowWid(_parent=self, _n_show_sample=self.n_show_sample, _img_win_size=self.img_win_size)
        self.wid_img.move(0, 70)
        self.setGeometry(300, 300, self.wid_img.width()+100, self.wid_img.height()+100)
        self.load_h5_data()

        QtCore.QObject.connect(self.button_next, QtCore.SIGNAL('clicked()'),  self.On_Click_button_next)
        QtCore.QObject.connect(self.button_prior, QtCore.SIGNAL('clicked()'),  self.On_Click_button_prior)
        QtCore.QObject.connect(self.ld_nframe, QtCore.SIGNAL('returnPressed()'), lambda: self.On_ReturnPressed(self.ld_nframe))
        # self.ld_nframe.returnPressed.connect(lambda: self.On_ReturnPressed(self.ld_nframe))

    def __show_image(self):
        sample = np.empty((self.n_show_sample, self.dataset.shape[1],self.dataset.shape[2],self.dataset.shape[3]))
        for i in xrange(self.n_show_sample):
            # t_sample = cp.deepcopy(self.dataset[self.nframe+i])
            sample[i] = self.dataset[self.nframe+i]

        self.wid_img.update_img_label(sample)
        self.l_message.setText(
            QtCore.QString("current frame indx is :" + str(self.nframe) + "~" + str(self.nframe + self.n_show_sample-1)))

    def On_Click_button_next(self):
        if self.nframe >= self.dataset.shape[0]-self.n_show_sample-1:
            self.nframe = -self.n_show_sample
        self.nframe += self.n_show_sample
        self.__show_image()
        # cv2.waitKey()


    def On_Click_button_prior(self):
        if self.nframe <= 0:
            self.nframe = self.dataset.shape[0]
        self.nframe -= self.n_show_sample
        self.__show_image()
        # cv2.waitKey()

    def On_ReturnPressed(self, _sgnal_qobj):
        def is_num_by_except(num):
            try:
                tnum = int(num)
                return tnum
            except ValueError:
                print "%s ValueError" % num
                return None

        t_nframe = is_num_by_except(_sgnal_qobj.text())
        if t_nframe >= 0 and t_nframe < self.n_total_sample:
            # print t_nframe
            self.nframe = t_nframe
            if t_nframe >= self.n_total_sample - self.n_show_sample:
                self.nframe = self.n_total_sample - self.n_show_sample
            self.__show_image()

    def load_h5_data(self):
        self.f = h5.File(self.path, 'r')
        self.dataset = self.f['data']
        self.n_total_sample = self.dataset.shape[0]
        self.nframe = -self.n_show_sample


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    viewer = DS_Viewer(sys.argv[1])
    viewer.show()
    sys.exit(app.exec_())

