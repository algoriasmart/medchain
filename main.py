import sys

import bcrypt
from PyQt5.QtCore import Qt, QSize, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import hmac
import hashlib
import base64


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


class Login(QWidget):
    send_role = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_widgets()
        self.set_styles()
        self.connect()

    def init_widgets(self):
        self.resize(300, 300)
        self.title = QLabel("Login")
        self.title.setAlignment(Qt.AlignCenter)
        self.username = QLineEdit()
        self.username.setPlaceholderText("User")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.send = QPushButton("Enviar")
        self.send.clicked.connect(self.login)
        self.recover = QLabel("Recuperar contraseña")
        self.info = QLabel()
        main_v_box = QVBoxLayout()
        main_v_box.setAlignment(Qt.AlignHCenter)
        main_v_box.setSpacing(15)
        main_v_box.addWidget(self.title)
        main_v_box.addWidget(self.username)
        main_v_box.addWidget(self.password)
        main_v_box.addWidget(self.send)
        main_v_box.addWidget(self.recover)
        main_v_box.addWidget(self.info)
        self.setLayout(main_v_box)

    def set_styles(self):
        self.setStyleSheet("background-color: rgb(26, 26, 26)")

        self.title.setStyleSheet("color: rgb(220, 216, 206); font-size: 36px; text-align: center")

        input_style = "background-color: rgb(45, 45, 45); color: rgb(140, 140, 140); border: none; font-size: 18px"
        self.username.setStyleSheet(input_style)
        self.password.setStyleSheet(input_style)
        self.username.setMaximumWidth(250)
        self.password.setMaximumWidth(250)

        self.send.setStyleSheet("background-color: rgb(31, 189, 200); color: rgb(220, 216, 206); font-size: 18px")
        self.send.setMaximumWidth(250)

        self.recover.setStyleSheet("color: rgb(31, 189, 200); font-size: 18px")

        self.info.setStyleSheet("color: rgb(255, 0, 0); font-size: 18px")


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

    def connectSQLlite(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("test.sql")
        ok = database.open()
        if ok:
            print('Success')
        else:
            print(database.lastError().text())


app = QApplication(sys.argv)
login = Login()
window = MainWindow()
login.show()
login.send_role.connect(window.set_role)
app.exec_()
