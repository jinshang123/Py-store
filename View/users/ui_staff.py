# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Staff(object):
    def setupUi(self, Staff):
        Staff.setObjectName("Staff")
        Staff.resize(945, 603)
        self.layoutWidget = QtWidgets.QWidget(Staff)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 944, 603))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_staff = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_staff.sizePolicy().hasHeightForWidth())
        self.add_staff.setSizePolicy(sizePolicy)
        self.add_staff.setMinimumSize(QtCore.QSize(105, 39))
        self.add_staff.setMaximumSize(QtCore.QSize(105, 39))
        self.add_staff.setObjectName("add_staff")
        self.horizontalLayout_4.addWidget(self.add_staff)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.staff_table = QtWidgets.QTableView(self.layoutWidget)
        self.staff_table.setMinimumSize(QtCore.QSize(940, 491))
        self.staff_table.setObjectName("staff_table")
        self.verticalLayout_5.addWidget(self.staff_table)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.delete_staff = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_staff.sizePolicy().hasHeightForWidth())
        self.delete_staff.setSizePolicy(sizePolicy)
        self.delete_staff.setMinimumSize(QtCore.QSize(127, 59))
        self.delete_staff.setMaximumSize(QtCore.QSize(127, 59))
        self.delete_staff.setObjectName("delete_staff")
        self.horizontalLayout_13.addWidget(self.delete_staff)
        self.update_staff = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_staff.sizePolicy().hasHeightForWidth())
        self.update_staff.setSizePolicy(sizePolicy)
        self.update_staff.setMinimumSize(QtCore.QSize(126, 59))
        self.update_staff.setMaximumSize(QtCore.QSize(126, 59))
        self.update_staff.setObjectName("update_staff")
        self.horizontalLayout_13.addWidget(self.update_staff)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.verticalLayout_12.addLayout(self.verticalLayout_5)

        self.retranslateUi(Staff)
        QtCore.QMetaObject.connectSlotsByName(Staff)

    def retranslateUi(self, Staff):
        _translate = QtCore.QCoreApplication.translate
        Staff.setWindowTitle(_translate("Staff", "Form"))
        self.add_staff.setText(_translate("Staff", "新增员工"))
        self.delete_staff.setText(_translate("Staff", "删除"))
        self.update_staff.setText(_translate("Staff", "修改"))

