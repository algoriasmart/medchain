import sys

import bcrypt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import hmac
import hashlib
import base64

from Login import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    @pyqtSlot(str)
    def set_role(self, role):
        self.show()
        self.role = QLabel(role)
        self.setCentralWidget(self.role)
        self.raise_()


def encode_string(string):
    return string.encode('utf-8')


def check_password(password, hash_password):
    salt = "146585145368132386173505678016728509634"
    h = hmac.new(encode_string(salt), encode_string(password), hashlib.sha512)
    h = base64.b64encode(h.digest())
    return bcrypt.checkpw(h, encode_string(hash_password))


class Login(QMainWindow, Ui_MainWindow):
    send_role = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect()
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username.text()
        if username == "":
            self.info.setText("Introduce tu nombre de usuario")
        else:
            password = self.password.text()
            if password == "":
                self.info.setText("Introduce tu contraseña")
            else:
                query = QSqlQuery()
                query.prepare("SELECT email, password FROM users WHERE username = :username")
                query.bindValue(":username", username)
                query.exec()
                if query.next():
                    hash_password = query.value(1)
                    if check_password(password, hash_password):
                        query.prepare("SELECT roles.name FROM roles INNER JOIN roles_users ON roles.id = "
                                      "roles_users.role_id INNER JOIN users ON users.id = roles_users.user_id WHERE "
                                      "users.username = :username")
                        query.bindValue(":username", username)
                        query.exec()
                        if query.next():
                            role = query.value(0)
                            if role != "paciente":
                                self.send_role.emit(role)
                                self.hide()
                            else:
                                self.info.setText("No tienes permiso para acceder")
                        else:
                            self.info.setText("Error no tienes asignado ningún rol")
                    else:
                        self.info.setText("Contraseña incorrecta")
                else:
                    self.info.setText("Usuario incorrecto")

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


app = QApplication(sys.argv)
login = Login()
window = MainWindow()
login.show()
login.send_role.connect(window.set_role)
app.exec_()
