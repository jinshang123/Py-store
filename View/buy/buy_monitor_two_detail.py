# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_stock.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from View.buy.ui.ui_buy_monitor_two_detail import Ui_monitortwodetailDialog


class Diglog_monitor_two_detail(QtWidgets.QDialog, Ui_monitortwodetailDialog):
    def __init__(self):
        super(Diglog_monitor_two_detail, self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self._retranslateUi)

    def _retranslateUi(self):
        self.retranslateUi