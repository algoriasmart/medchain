import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class Login(QWidget):
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
        self.password.setPlaceholderText("Password")
        self.send = QPushButton("Enviar")
        self.send.clicked.connect(self.login)
        self.info = QLabel()
        main_v_box = QVBoxLayout()
        main_v_box.setAlignment(Qt.AlignHCenter)
        main_v_box.setSpacing(15)
        main_v_box.addWidget(self.title)
        main_v_box.addWidget(self.username)
        main_v_box.addWidget(self.password)
        main_v_box.addWidget(self.send)
        main_v_box.addWidget(self.info)
        self.setLayout(main_v_box)

    def set_palette(self):
        main_palette = QPalette()
        main_palette.setColor(QPalette.Window, QColor(26, 26, 26))
        self.setPalette(main_palette)

        title_palette = self.title.palette()
        title_palette.setColor(self.title.foregroundRole(), QColor(220, 216, 206))
        self.title.setPalette(title_palette)
        title_font = self.title.font()
        title_font.setPointSize(18)
        self.title.setFont(title_font)

        input_palette = QPalette()
        input_palette.setColor(QPalette.Base, QColor(45, 45, 45))
        input_palette.setColor(QPalette.PlaceholderText, QColor(85, 85, 85))
        input_palette.setColor(QPalette.Text, QColor(140, 140, 140))
        self.username.setPalette(input_palette)
        self.password.setPalette(input_palette)
        self.username.setMinimumSize(QSize(200, 30))
        self.password.setMinimumSize(QSize(200, 30))

        send_palette = QPalette()
        send_palette.setColor(QPalette.Background, QColor(31, 189, 200))
        self.send.setPalette(send_palette)

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

        self.info.setStyleSheet("color: rgb(255, 0, 0); font-size: 18px")


    def login(self):
        username = self.username.text()
        if username == "":
            self.info.setText("Empty username")
        else:
            password = self.password.text()
            if password == "":
                self.info.setText("Empty password")
            else:
                print("Login " + username + " " + password)

    def connect(self):
        server = 'remotemysql.com'
        database_name = 'zAKPC936JP'
        user_name = 'zAKPC936JP'
        password = 'UloEGPhfyS'

        server = 'localhost'
        database_name = 'test'
        user_name = 'root'
        password = 'password'

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
window = Login()
window.show()
app.exec_()

