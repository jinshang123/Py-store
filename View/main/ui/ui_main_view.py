# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 734)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(960, 630))
        self.tabWidget.setMaximumSize(QtCore.QSize(960, 630))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 35))
        self.menuBar.setMinimumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("padding-top:5px;")
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.sales = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        self.sales.setFont(font)
        self.sales.setStyleSheet("")
        self.sales.setObjectName("sales")
        self.supplier = QtWidgets.QMenu(self.menuBar)
        self.supplier.setObjectName("supplier")
        self.setting = QtWidgets.QMenu(self.menuBar)
        self.setting.setObjectName("setting")
        self.setting_user = QtWidgets.QMenu(self.setting)
        self.setting_user.setObjectName("setting_user")
        self.stock = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        self.stock.setFont(font)
        self.stock.setSeparatorsCollapsible(False)
        self.stock.setObjectName("buy")
        self.stock_add = QtWidgets.QMenu(self.stock)
        self.stock_add.setObjectName("stock_add")
        self.inventory = QtWidgets.QMenu(self.menuBar)
        self.inventory.setObjectName("inventory")
        self.operation = QtWidgets.QMenu(self.menuBar)
        self.operation.setObjectName("operation")
        self.return_visit = QtWidgets.QMenu(self.menuBar)
        self.return_visit.setObjectName("return_visit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLocal = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        self.actionLocal.setFont(font)
        self.actionLocal.setObjectName("actionLocal")
        self.actionAll = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        self.actionAll.setFont(font)
        self.actionAll.setObjectName("actionAll")
        self.normal_stock_add = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        self.normal_stock_add.setFont(font)
        self.normal_stock_add.setObjectName("normal_stock_add")
        self.write_off_add = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        self.write_off_add.setFont(font)
        self.write_off_add.setObjectName("write_off_add")
        self.history_stock = QtWidgets.QAction(MainWindow)
        self.history_stock.setObjectName("history_stock")
        self.services_add = QtWidgets.QAction(MainWindow)
        self.services_add.setObjectName("services_add")
        self.store_user = QtWidgets.QAction(MainWindow)
        self.store_user.setObjectName("store_user")
        self.system_user = QtWidgets.QAction(MainWindow)
        self.system_user.setObjectName("system_user")
        self.return_visit_customer = QtWidgets.QAction(MainWindow)
        self.return_visit_customer.setObjectName("return_visit_customer")
        self.setting_device = QtWidgets.QAction(MainWindow)
        self.setting_device.setObjectName("setting_device")
        self.setting_password = QtWidgets.QAction(MainWindow)
        self.setting_password.setObjectName("setting_password")
        self.inventory_search = QtWidgets.QAction(MainWindow)
        self.inventory_search.setObjectName("inventory_search")
        self.inventory_unsalable_pre_warning = QtWidgets.QAction(MainWindow)
        self.inventory_unsalable_pre_warning.setObjectName("inventory_unsalable_pre_warning")
        self.stock_monitor = QtWidgets.QAction(MainWindow)
        self.stock_monitor.setObjectName("stock_monitor")
        self.inventory_money = QtWidgets.QAction(MainWindow)
        self.inventory_money.setObjectName("inventory_money")
        self.inventory_calibration = QtWidgets.QAction(MainWindow)
        self.inventory_calibration.setObjectName("inventory_calibration")
        self.supplier_arrears = QtWidgets.QAction(MainWindow)
        self.supplier_arrears.setObjectName("supplier_arrears")
        self.supplier_payment = QtWidgets.QAction(MainWindow)
        self.supplier_payment.setObjectName("supplier_payment")
        self.performance = QtWidgets.QAction(MainWindow)
        self.performance.setObjectName("performance")
        self.sub_service_operation_data = QtWidgets.QAction(MainWindow)
        self.sub_service_operation_data.setObjectName("sub_service_operation_data")
        self.operation_total_data = QtWidgets.QAction(MainWindow)
        self.operation_total_data.setObjectName("operation_total_data")
        self.sales.addAction(self.actionLocal)
        self.sales.addAction(self.actionAll)
        self.supplier.addAction(self.supplier_arrears)
        self.supplier.addAction(self.supplier_payment)
        self.setting_user.addAction(self.store_user)
        self.setting_user.addAction(self.system_user)
        self.setting.addAction(self.setting_user.menuAction())
        self.setting.addAction(self.services_add)
        self.setting.addAction(self.setting_device)
        self.setting.addAction(self.setting_password)
        self.stock_add.addAction(self.normal_stock_add)
        self.stock_add.addAction(self.write_off_add)
        self.stock.addAction(self.stock_add.menuAction())
        self.stock.addAction(self.history_stock)
        self.stock.addAction(self.stock_monitor)
        self.inventory.addAction(self.inventory_search)
        self.inventory.addAction(self.inventory_unsalable_pre_warning)
        self.inventory.addAction(self.inventory_money)
        self.inventory.addAction(self.inventory_calibration)
        self.operation.addAction(self.performance)
        self.operation.addAction(self.sub_service_operation_data)
        self.operation.addAction(self.operation_total_data)
        self.return_visit.addAction(self.return_visit_customer)
        self.menuBar.addAction(self.sales.menuAction())
        self.menuBar.addAction(self.stock.menuAction())
        self.menuBar.addAction(self.inventory.menuAction())
        self.menuBar.addAction(self.return_visit.menuAction())
        self.menuBar.addAction(self.supplier.menuAction())
        self.menuBar.addAction(self.operation.menuAction())
        self.menuBar.addAction(self.setting.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "门店管理系统"))
        self.sales.setTitle(_translate("MainWindow", "销售明细"))
        self.supplier.setTitle(_translate("MainWindow", "供应商管理"))
        self.setting.setTitle(_translate("MainWindow", "系统管理"))
        self.setting_user.setTitle(_translate("MainWindow", "人员管理"))
        self.stock.setTitle(_translate("MainWindow", "进货管理"))
        self.stock_add.setTitle(_translate("MainWindow", "进货录入"))
        self.inventory.setTitle(_translate("MainWindow", "库存管理"))
        self.operation.setTitle(_translate("MainWindow", "经营分析"))
        self.return_visit.setTitle(_translate("MainWindow", "客户回访"))
        self.actionLocal.setText(_translate("MainWindow", "本店"))
        self.actionAll.setText(_translate("MainWindow", "全店"))
        self.normal_stock_add.setText(_translate("MainWindow", "普通进货录入"))
        self.write_off_add.setText(_translate("MainWindow", "销负进货录入"))
        self.history_stock.setText(_translate("MainWindow", "历史进货"))
        self.services_add.setText(_translate("MainWindow", "服务项目管理"))
        self.store_user.setText(_translate("MainWindow", "门店人员"))
        self.system_user.setText(_translate("MainWindow", "系统人员"))
        self.return_visit_customer.setText(_translate("MainWindow", "回访"))
        self.setting_device.setText(_translate("MainWindow", "设备管理"))
        self.setting_password.setText(_translate("MainWindow", "门店及密码"))
        self.inventory_search.setText(_translate("MainWindow", "库存查询"))
        self.inventory_unsalable_pre_warning.setText(_translate("MainWindow", "滞销预警"))
        self.stock_monitor.setText(_translate("MainWindow", "进货监控"))
        self.inventory_money.setText(_translate("MainWindow", "库存金额"))
        self.inventory_calibration.setText(_translate("MainWindow", "库存校准"))
        self.supplier_arrears.setText(_translate("MainWindow", "欠款明细"))
        self.supplier_payment.setText(_translate("MainWindow", "付款录入"))
        self.performance.setText(_translate("MainWindow", "业绩报表"))
        self.sub_service_operation_data.setText(_translate("MainWindow", "二级分类经营数据"))
        self.operation_total_data.setText(_translate("MainWindow", "总体经营数据"))

