import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow

from login import Login
from medico import Medico
from auxiliar import Auxiliar


class Controlador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connect()
        self.login = Login(self.database)
        self.login.login_info.connect(self.logged)
        self.login.show()

    def connect(self):
        server = 'remotemysql.com'
        database_name = 'zAKPC936JP'
        user_name = 'zAKPC936JP'
        password = 'UloEGPhfyS'

        self.database = QSqlDatabase.addDatabase("QMYSQL")
        self.database.setHostName(server)
        self.database.setDatabaseName(database_name)
        self.database.setUserName(user_name)
        self.database.setPassword(password)
        ok = self.database.open()
        if ok:
            print('Success')
        else:
            print(self.database.lastError().text())

    @pyqtSlot(str, str)
    def logged(self, username, role):
        if role == "medico":
            self.main_window = Medico(self.database, username)
            self.main_window.logout_signal.connect(self.logout)
            self.raise_()
        if role == "auxiliar":
            self.main_window = Auxiliar(self.database, username)
            self.main_window.logout_signal.connect(self.logout)
            self.raise_()

    @pyqtSlot()
    def logout(self):
        self.main_window.close()
        self.main_window = None
        self.login.username.setText("")
        self.login.password.setText("")
        self.login.show()


app = QApplication(sys.argv)
controlador = Controlador()
app.exec_()
