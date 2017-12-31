import traceback

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog

from View.sale.excel_process import ExcelProcess
from View.sale.ui_sale_detail import Ui_SaleDetail as SaleDetail


class SaleBase(QtWidgets.QWidget, SaleDetail):
    def __init__(self):
        super(SaleBase, self).__init__()
        self.setupUi(self)
        my_icon = QIcon('img/logo.png')
        self.setWindowIcon(my_icon)
        self._signal_slot_init()

    def _signal_slot_init(self):
        self.details_import_button.clicked.connect(self._sale_detail_import)
        self.details_export_button.clicked.connect(self._sale_detail_export)

    def _sale_detail_import(self):
        file_dialog = QFileDialog()
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(file_dialog, "选取文件", "C:/",
                                                                   "Text Files (*.xlsx;*.xls)")  # 设置文件扩展名过滤,注意用分号间隔
        if file_name:
            try:
                excel_handler = ExcelProcess()
                excel_handler.import_sale_detail(file_name, self)
                QtWidgets.QMessageBox.information(self.details_import_button, "提示", "导入成功")
            except Exception as e:
                print(e)
                print('traceback.print_exc():{}'.format(traceback.print_exc()))
                print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                QtWidgets.QMessageBox.information(self.details_import_button, "提示", "文件错误")

    def _sale_detail_export(self):
        start_time = self.dateEdit_5.text()
        end_time = self.dateEdit_6.text()
        excel_handler = ExcelProcess()
        file_name = excel_handler.export_sale_detail(start_time, end_time)
        if file_name:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "文件名为：{}".format(file_name))
        else:
            QtWidgets.QMessageBox.information(self.menu1Add, "提示", "暂无消费记录")

    def _result_process(self, result_str):
        if result_str:
            pass
        elif not result_str:
            QtWidgets.QMessageBox.information(self.details_query_button, "提示", "网络连接错误")
        elif result_str == 'restart':
            QtWidgets.QMessageBox.information(self.details_query_button, "提示", "与服务器链接中断，请重新运行软件")
        else:
            pass