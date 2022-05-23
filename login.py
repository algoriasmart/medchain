from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtSql import QSqlQuery

from login_ui import Ui_MainWindow

from security import check_password


class Login(QMainWindow, Ui_MainWindow):
    login_info = pyqtSignal(str, str, str)

    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.database = database
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.login_button.clicked.connect(self.login)

        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.background.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

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
                query.prepare("SELECT password FROM users WHERE username = :username")
                query.bindValue(":username", username)
                query.exec()
                if query.next():
                    hash_password = query.value(0)
                    if check_password(password, hash_password):
                        query.prepare("SELECT roles.name FROM roles INNER JOIN roles_users ON roles.id = "
                                      "roles_users.role_id INNER JOIN users ON users.id = roles_users.user_id WHERE "
                                      "users.username = :username")
                        query.bindValue(":username", username)
                        query.exec()
                        if query.next():
                            role = query.value(0)
                            if role != "paciente":
                                self.info.setText("")
                                self.login_info.emit(username, password, role)
                                self.hide()
                            else:
                                self.info.setText("No tienes permiso para acceder")
                        else:
                            self.info.setText("Error no tienes asignado ningún rol")
                    else:
                        self.info.setText("Contraseña incorrecta")
                else:
                    self.info.setText("Usuario incorrecto")
