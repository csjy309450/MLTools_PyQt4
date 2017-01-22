# -*- coding=utf-8 -*-

import sys
from PyQt4 import QtGui
import Ui_ShellManager


def main():
    app = QtGui.QApplication(sys.argv)
    win = Ui_ShellManager.Ui_ShellManager()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()