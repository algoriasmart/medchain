# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 450))
        self.background.setStyleSheet("QFrame{\n"
"    background-color: rgb(26,26,26);\n"
"    border: 5px solid rgb(11,11,11);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"    border:none;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-radius: 25px;\n"
"    color: rgb(189, 208, 211);\n"
"    text-align:center;\n"
"    padding: 7px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid rgb(31,189,200);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(31,189,200);\n"
"    border-radius: 25px;\n"
"    color: rgb(189, 208, 211);\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.background)
        self.title.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(189, 208, 211);\n"
"border: none;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.username = QtWidgets.QLineEdit(self.background)
        self.username.setMinimumSize(QtCore.QSize(240, 50))
        self.username.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setText("")
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username, 0, QtCore.Qt.AlignHCenter)
        self.password = QtWidgets.QLineEdit(self.background)
        self.password.setMinimumSize(QtCore.QSize(240, 50))
        self.password.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password, 0, QtCore.Qt.AlignHCenter)
        self.login_button = QtWidgets.QPushButton(self.background)
        self.login_button.setMinimumSize(QtCore.QSize(300, 50))
        self.login_button.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.verticalLayout.addWidget(self.login_button, 0, QtCore.Qt.AlignHCenter)
        self.recover_password = QtWidgets.QLabel(self.background)
        self.recover_password.setMinimumSize(QtCore.QSize(260, 0))
        self.recover_password.setMaximumSize(QtCore.QSize(260, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.recover_password.setFont(font)
        self.recover_password.setStyleSheet("border: none;\n"
"color: rgb(31,189,200);")
        self.recover_password.setObjectName("recover_password")
        self.verticalLayout.addWidget(self.recover_password, 0, QtCore.Qt.AlignHCenter)
        self.info = QtWidgets.QLabel(self.background)
        self.info.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.info.setFont(font)
        self.info.setStyleSheet("border: none;\n"
"color: rgb(255,0,0);")
        self.info.setText("")
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Login"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.recover_password.setText(_translate("MainWindow", "Recuperar contraseña"))
