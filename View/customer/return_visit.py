from PyQt5 import QtWidgets, QtCore, QtGui

from Controller import DbHandler
from View.customer.ui.ui_return_visit import Ui_ReturnVisit as UiReturnVisit
from View.customer.return_visit_setting import ReturnVisitSetting
from View.utils.table_utils import get_table_current_index_info
from database.dao.customer import customer_handler

try:
    _from_utf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _from_utf8(s):
        return s


class ReturnVisit(QtWidgets.QWidget, UiReturnVisit):
    def __init__(self):
        super(ReturnVisit, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('客户回访')

        self._init_table_title()

        self.return_visit_button.clicked.connect(self._return_visit_process)

    def _init_table_title(self):
        # 添加表头：
        model = QtGui.QStandardItemModel()

        # 设置表头
        title_list = ["ID", '回访用户', '车牌号', '联系方式', '回访时间']
        table_len = len(title_list)
        # 设置表格属性：
        model.setColumnCount(table_len)

        for i in range(table_len):
            model.setHeaderData(i, QtCore.Qt.Horizontal, _from_utf8(title_list[i]))

        self.return_visit_table.setModel(model)
        self.return_visit_table.setColumnWidth(0, 60)

    def _return_visit_process(self):
        record_id = get_table_current_index_info(self.return_visit_table, 0)
        username = get_table_current_index_info(self.return_visit_table, 1)
        car_id = get_table_current_index_info(self.return_visit_table, 2)
        car_phone = get_table_current_index_info(self.return_visit_table, 3)
        return_visit_date = get_table_current_index_info(self.return_visit_table, 4)
        print(return_visit_date)
        if record_id:
            msg = "您于  <b>{}</b> 要回访用户 ： <b>{}</b><br>联系方式为 ： <b>{}</b><br>车牌号为 ： <b>{}</b>".format(
                return_visit_date[:10],
                username, car_phone,
                car_id)
            ui = ReturnVisitSetting(msg, record_id, car_phone, car_id, username)
            ui.exec_()
            self.return_visit_setting()
        else:
            QtWidgets.QMessageBox.information(self.return_visit_button, "提示", "请选择未回访记录")

    def return_visit_setting(self):

        db_help = DbHandler.DB_Handler()

        # 添加表头：
        model = QtGui.QStandardItemModel()

        # 设置表头
        title_list = ["ID", '回访用户', '车牌号', '联系方式', '回访时间']
        table_len = len(title_list)
        # 设置表格属性：
        model.setColumnCount(table_len)

        for i in range(table_len):
            model.setHeaderData(i, QtCore.Qt.Horizontal, _from_utf8(title_list[i]))

        self.return_visit_table.setModel(model)
        self.return_visit_table.setColumnWidth(0, 200)

        # 获取信息
        callback = customer_handler.get_return_visit_info()

        if callback:
            # 插入信息
            i = 0
            for data in callback:
                for j in range(table_len):
                    model.setItem(i, j, QtGui.QStandardItem(_from_utf8(str(data[j]))))
                i += 1
        self.return_visit_table.setModel(model)
