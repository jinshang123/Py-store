# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_service.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(970, 624)
        Form.setMinimumSize(QtCore.QSize(970, 600))
        Form.setMaximumSize(QtCore.QSize(982, 624))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.import_service = QtWidgets.QPushButton(Form)
        self.import_service.setMinimumSize(QtCore.QSize(75, 31))
        self.import_service.setMaximumSize(QtCore.QSize(75, 31))
        self.import_service.setObjectName("import_service")
        self.horizontalLayout_3.addWidget(self.import_service)
        self.export_service = QtWidgets.QPushButton(Form)
        self.export_service.setMinimumSize(QtCore.QSize(75, 31))
        self.export_service.setMaximumSize(QtCore.QSize(75, 31))
        self.export_service.setObjectName("export_service")
        self.horizontalLayout_3.addWidget(self.export_service)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.first_service_table = QtWidgets.QTableView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_service_table.sizePolicy().hasHeightForWidth())
        self.first_service_table.setSizePolicy(sizePolicy)
        self.first_service_table.setMinimumSize(QtCore.QSize(400, 470))
        self.first_service_table.setMaximumSize(QtCore.QSize(400, 470))
        self.first_service_table.setObjectName("first_service_table")
        self.first_service_table.horizontalHeader().setStretchLastSection(True)
        self.first_service_table.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.first_service_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.add_first_service = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_first_service.sizePolicy().hasHeightForWidth())
        self.add_first_service.setSizePolicy(sizePolicy)
        self.add_first_service.setMinimumSize(QtCore.QSize(79, 42))
        self.add_first_service.setMaximumSize(QtCore.QSize(79, 42))
        self.add_first_service.setObjectName("add_first_service")
        self.horizontalLayout.addWidget(self.add_first_service)
        self.update_first_service = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_first_service.sizePolicy().hasHeightForWidth())
        self.update_first_service.setSizePolicy(sizePolicy)
        self.update_first_service.setMinimumSize(QtCore.QSize(79, 42))
        self.update_first_service.setMaximumSize(QtCore.QSize(79, 42))
        self.update_first_service.setObjectName("update_first_service")
        self.horizontalLayout.addWidget(self.update_first_service)
        self.remove_first_service = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_first_service.sizePolicy().hasHeightForWidth())
        self.remove_first_service.setSizePolicy(sizePolicy)
        self.remove_first_service.setMinimumSize(QtCore.QSize(79, 42))
        self.remove_first_service.setMaximumSize(QtCore.QSize(79, 42))
        self.remove_first_service.setObjectName("remove_first_service")
        self.horizontalLayout.addWidget(self.remove_first_service)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.second_service_table = QtWidgets.QTableView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.second_service_table.sizePolicy().hasHeightForWidth())
        self.second_service_table.setSizePolicy(sizePolicy)
        self.second_service_table.setMinimumSize(QtCore.QSize(400, 470))
        self.second_service_table.setMaximumSize(QtCore.QSize(400, 470))
        self.second_service_table.setObjectName("second_service_table")
        self.second_service_table.horizontalHeader().setVisible(True)
        self.second_service_table.horizontalHeader().setStretchLastSection(True)
        self.second_service_table.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.second_service_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.add_second_service = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_second_service.sizePolicy().hasHeightForWidth())
        self.add_second_service.setSizePolicy(sizePolicy)
        self.add_second_service.setMinimumSize(QtCore.QSize(75, 39))
        self.add_second_service.setMaximumSize(QtCore.QSize(75, 39))
        self.add_second_service.setObjectName("add_second_service")
        self.horizontalLayout_2.addWidget(self.add_second_service)
        self.update_second_service = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_second_service.sizePolicy().hasHeightForWidth())
        self.update_second_service.setSizePolicy(sizePolicy)
        self.update_second_service.setMinimumSize(QtCore.QSize(75, 39))
        self.update_second_service.setMaximumSize(QtCore.QSize(75, 39))
        self.update_second_service.setObjectName("update_second_service")
        self.horizontalLayout_2.addWidget(self.update_second_service)
        self.remove_second_service = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_second_service.sizePolicy().hasHeightForWidth())
        self.remove_second_service.setSizePolicy(sizePolicy)
        self.remove_second_service.setMinimumSize(QtCore.QSize(75, 39))
        self.remove_second_service.setMaximumSize(QtCore.QSize(75, 39))
        self.remove_second_service.setObjectName("remove_second_service")
        self.horizontalLayout_2.addWidget(self.remove_second_service)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.attribute_table = QtWidgets.QTableView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attribute_table.sizePolicy().hasHeightForWidth())
        self.attribute_table.setSizePolicy(sizePolicy)
        self.attribute_table.setMinimumSize(QtCore.QSize(100, 470))
        self.attribute_table.setMaximumSize(QtCore.QSize(100, 470))
        self.attribute_table.setObjectName("attribute_table")
        self.attribute_table.horizontalHeader().setVisible(False)
        self.attribute_table.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.attribute_table)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 39))
        self.label.setMaximumSize(QtCore.QSize(75, 39))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.import_service.setText(_translate("Form", "导出"))
        self.export_service.setText(_translate("Form", "导入"))
        self.add_first_service.setText(_translate("Form", "新增"))
        self.update_first_service.setText(_translate("Form", "修改"))
        self.remove_first_service.setText(_translate("Form", "删除"))
        self.add_second_service.setText(_translate("Form", "新增"))
        self.update_second_service.setText(_translate("Form", "修改"))
        self.remove_second_service.setText(_translate("Form", "删除"))

