from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, pyqtSignal, Qt, pyqtSlot
from PyQt5.QtSql import QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QAbstractScrollArea, QPushButton

from medico_ui import Ui_MainWindow
from confirmar_programacion_ui import Ui_Dialog


class Medico(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()
    programar_signal = pyqtSignal(str, str)

    def __init__(self, database, username):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.database = database
        self.username = username
        self.set_name()
        self.set_center_name()
        self.load_data()
        self.exit.clicked.connect(lambda: self.close())
        self.toggle_lateral_bar.clicked.connect(lambda: self.side_left_menu())
        self.logout.clicked.connect(lambda: self.logout_signal.emit())

        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.background.mouseMoveEvent = moveWindow

        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def set_name(self):
        query = QSqlQuery()
        query.prepare("SELECT nombre FROM users WHERE username = :username")
        query.bindValue(":username", self.username)
        query.exec()
        if query.next():
            nombre = query.value(0)
            self.nombre.setText(nombre)

    def set_center_name(self):
        query = QSqlQuery()
        query.prepare("SELECT centros.nombreFiscal FROM centros INNER JOIN users ON users.id_centro = centros.id "
                      "WHERE users.username = :username")
        query.bindValue(":username", self.username)
        query.exec()
        if query.next():
            nombre_centro = query.value(0)
            self.centro.setText(nombre_centro)

    def side_left_menu(self):
        width = self.lateral_bar.width()

        if width == 0:
            new_width = 150
            #self.open_close_side_bar_btn.setIcon(QtGui.QIcon("chevrons-left.svg"))
        else:
            new_width = 0
            #self.open_close_side_bar_btn.setIcon(QtGui.QIcon("align-left.svg"))

        self.animation = QPropertyAnimation(self.lateral_bar, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def load_data(self):
        query = QSqlQuery()
        query.prepare("SELECT users.identificador, users.nombre, centros.nombreFiscal FROM "
                      "users INNER JOIN centros ON users.id_centro = centros.id INNER JOIN pacientes_asociados ON "
                      "users.id = pacientes_asociados.id_paciente INNER JOIN users AS users2 ON "
                      "pacientes_asociados.id_medico = users2.id WHERE users2.username = :username ")
        query.bindValue(":username", self.username)
        query.exec()
        self.tabla_pacientes.setRowCount(query.size())
        table_row = 0
        while query.next():
            self.tabla_pacientes.setItem(table_row, 0, QtWidgets.QTableWidgetItem(query.value(0)))
            self.tabla_pacientes.setItem(table_row, 1, QtWidgets.QTableWidgetItem(query.value(1)))
            self.tabla_pacientes.setItem(table_row, 2, QtWidgets.QTableWidgetItem(query.value(2)))
            programar = QPushButton("Programar test")
            programar.setStyleSheet("QPushButton {background-color: rgb(31,189,200); color: rgb(189, 208, "
                                    "211); border: none; border-radius: 10px;}")
            programar.clicked.connect(
                lambda state, dni=query.value(0), nombre=query.value(1): self.confirmar_programacion(dni, nombre))
            self.tabla_pacientes.setIndexWidget(self.tabla_pacientes.model().index(table_row, 3), programar)

            table_row += 1

        self.tabla_pacientes.verticalHeader().setVisible(False)
        self.tabla_pacientes.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabla_pacientes.setColumnWidth(3, self.tabla_pacientes.columnWidth(3) * 1.1)
        self.tabla_pacientes.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.tabla_pacientes.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabla_pacientes.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def load_data_view(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("SELECT users.identificador AS DNI, users.nombre AS Nombre, centros.nombreFiscal AS Centro FROM "
                      "users INNER JOIN centros ON users.id_centro = centros.id INNER JOIN pacientes_asociados ON "
                      "users.id = pacientes_asociados.id_paciente INNER JOIN users AS users2 ON "
                      "pacientes_asociados.id_medico = users2.id WHERE users2.username = :username ")
        query.bindValue(":username", self.username)
        query.exec_()
        model.setQuery(query)
        self.tabla_pacientes.setModel(model)
        ver_detalles = QPushButton()
        self.tabla_pacientes.setIndexWidget(model.index(0, 2), ver_detalles)
        self.tabla_pacientes.verticalHeader().setVisible(False)
        self.tabla_pacientes.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabla_pacientes.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabla_pacientes.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def confirmar_programacion(self, dni, nombre):
        print(dni)
        print(nombre)
