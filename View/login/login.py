# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import threading
from Controller.Interface import login_handler
from View.view import Ui_MainWindow
from Common.StaticFunc import md5
from Common.Common import ClientClose
from View.login.ui_login import Ui_MainWindow as UiLogin

import Common.config as config
from server.socket import run_socket
from server.web import run_tornado


class Login(QtWidgets.QMainWindow, UiLogin):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)

        my_icon = QIcon('img/logo.png')
        self.setWindowIcon(my_icon)
        self.BUFFER_SIZE = 1024

        self.setStyleSheet("""
            QLabel{color:#fff;}
            QMessageBox{background-image: url(img/1.jpg)}
            QLineEdit{background:#fff;}
            QPushButton{background-color:#f9e4c5}
        """)
        bg_icon = QtGui.QPixmap('img/1.jpg')
        palette = QtGui.QPalette()
        self.uc = True
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(bg_icon))  # 添加背景图片
        self.setPalette(palette)

        # Constant variable init
        self.password_suffix = 'udontknowwhy'
        self.supper_username = 'master'
        self.super_password = 'f15127eda7c7a3eab663bf8fa8e3be6e'
        self.admin_username = 'admin'

        self.login.clicked.connect(self.submit)

    def keyPressEvent(self, key_event):
        if key_event.key() == QtCore.Qt.Key_Enter or key_event.key() == QtCore.Qt.Key_Return:
            self.submit()

    def submit(self):
        test = True

        # 获取输入的账号密码
        original_password = self.password.text() + self.password_suffix
        username = self.username.text()

        if original_password != self.password_suffix and username != "" or test:
            original_password = md5(original_password)

            # 获取保存的用户账号密码
            if username != self.supper_username:
                original_password = login_handler.get_password(username)

            pwd = None
            if original_password or test:
                if username == self.supper_username:
                    pwd = self.super_password

                if test or original_password == pwd:
                    self.uc = False
                    QtWidgets.QMessageBox.information(self.login, "提示", "验证成功")
                    self.close()
                    level = 1
                    if username in [self.admin_username, self.supper_username] or test:
                        level = 0
                    try:
                        config.ui = Ui_MainWindow(level)

                        web_thread = threading.Thread(target=run_tornado, args=[config.ui])
                        web_thread.start()

                        run_socket()

                        config.ui.show()

                    except Exception as e:
                        import traceback
                        print(e)
                        print('traceback.print_exc():{}'.format(traceback.print_exc()))
                        print('traceback.format_exc():\n{}'.format(traceback.format_exc()))
                else:
                    QtWidgets.QMessageBox.information(self.pushButton, "提示", "密码输出错误")
            else:
                QtWidgets.QMessageBox.information(self.pushButton, "提示", "无此用户")
        else:
            QtWidgets.QMessageBox.information(self.pushButton, "提示", "请输入用户名、密码")

    def closeEvent(self, event):
        if self.uc:
            ClientClose()
