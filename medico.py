from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, pyqtSignal, Qt
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QAbstractScrollArea, QPushButton, QFileDialog, QMessageBox

from medico_ui import Ui_MainWindow
from confirmar_programacion import ConfirmarProgramacion
from mensage import Mensage

from pandas import read_csv

from chose_plot import ChosePlot
from utils import center_relative
from security import check_cookie


class Medico(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()

    def __init__(self, database, username, password):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.database = database
        self.username = username
        self.password = password
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
            self.toggle_lateral_bar.setIcon(QtGui.QIcon("go-previous.png"))
        else:
            new_width = 0
            self.toggle_lateral_bar.setIcon(QtGui.QIcon("go-next.png"))

        self.animation = QPropertyAnimation(self.lateral_bar, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    @check_cookie()
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
            csv = QPushButton("Guardar test")
            csv.setStyleSheet("QPushButton {background-color: rgb(31,189,200); color: rgb(189, 208, "
                              "211); border: none; border-radius: 10px;}")
            csv.clicked.connect(
                lambda state, dni=query.value(0): self.guardar_csv(dni))
            self.tabla_pacientes.setIndexWidget(self.tabla_pacientes.model().index(table_row, 4), csv)

            #BEGIN PLOTS

            plot = QPushButton("Plot")
            plot.setStyleSheet("QPushButton {background-color: rgb(31,189,200); color: rgb(189, 208, "
                                    "211); border: none; border-radius: 10px;}")
            plot.clicked.connect(
                lambda state, dni=query.value(0): self.plot(dni))
            self.tabla_pacientes.setIndexWidget(self.tabla_pacientes.model().index(table_row, 5), plot)

            #END PLOTS

            table_row += 1

        self.tabla_pacientes.verticalHeader().setVisible(False)
        self.tabla_pacientes.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabla_pacientes.setColumnWidth(3, self.tabla_pacientes.columnWidth(3) * 1.1)
        self.tabla_pacientes.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.tabla_pacientes.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabla_pacientes.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    @check_cookie()
    def confirmar_programacion(self, dni, nombre):
        dialog = ConfirmarProgramacion()
        dialog.setModal(True)
        dialog.set_name_dni(nombre, dni)
        dialog.accepted.connect(lambda: self.programar_test(dni))
        center_relative(self, dialog)
        dialog.exec_()

    def programar_test(self, dni):
        print(dni)

    @check_cookie()
    def guardar_csv(self, dni):
        def add_columns(df, dni):
            query = QSqlQuery()
            query.prepare("SELECT users.id FROM users WHERE users.identificador = :dni")
            query.bindValue(":dni", dni)
            query.exec_()
            if query.next():
                df["id_paciente"] = query.value(0)
                query = QSqlQuery()
                query.prepare("SELECT test.num_test FROM test INNER JOIN users ON users.id = test.id_paciente WHERE "
                              "users.identificador = :dni ORDER BY test.num_test DESC LIMIT 1")
                query.bindValue(":dni", dni)
                query.exec()
                if query.next():
                    next_num = query.value(0) + 1
                else:
                    next_num = 0
                df["num_test"] = next_num
                if not df["item"].is_unique:
                    items = range(len(df.index))
                    df["item"] = items
                return df

        def insert_df(df):
            query = QSqlQuery()
            query.prepare("SELECT id_centro FROM users WHERE id = :id")
            query.bindValue(":id", int(df.at[0, "id_paciente"]))
            query.exec_()
            if query.next():
                id_centro = query.value(0)
                query = QSqlQuery()
                query.prepare("INSERT INTO test (num_test, id_paciente, date, id_centro)"
                              "VALUES (:num_test, :id_paciente, :date, :id_centro)")
                query.bindValue(":num_test", int(df.at[0, "num_test"]))
                query.bindValue(":id_paciente", int(df.at[0, "id_paciente"]))
                query.bindValue(":date", df.at[0, "date"])
                query.bindValue(":id_centro", int(id_centro))
                if not query.exec_():
                    return False

                for index, row in df.iterrows():
                    query = QSqlQuery()
                    query.prepare("INSERT INTO test_unit (item, num_test, id_paciente, time, acc_x, acc_y, acc_z, "
                                  "gyr_x, gyr_y, gyr_z, mag_x, mag_y, mag_z)"
                                  "VALUES (:item, :num_test, :id_paciente, :time, :acc_x, :acc_y, :acc_z, :gyr_x, "
                                  ":gyr_y, :gyr_z, :mag_x, :mag_y, :mag_z)")
                    query.bindValue(":item", row.at["item"])
                    query.bindValue(":num_test", int(row.at["num_test"]))
                    query.bindValue(":id_paciente", int(row.at["id_paciente"]))
                    query.bindValue(":time", row.at["time"])
                    query.bindValue(":acc_x", row.at["acc_x"])
                    query.bindValue(":acc_y", row.at["acc_y"])
                    query.bindValue(":acc_z", row.at["acc_z"])
                    query.bindValue(":gyr_x", row.at["gyr_x"])
                    query.bindValue(":gyr_y", row.at["gyr_y"])
                    query.bindValue(":gyr_z", row.at["gyr_z"])
                    query.bindValue(":mag_x", row.at["mag_x"])
                    query.bindValue(":mag_y", row.at["mag_y"])
                    query.bindValue(":mag_z", row.at["mag_z"])
                    if not query.exec_():
                        return False
                return True
            else:
                return False

        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilter("csv(*.csv);;Text files (*.txt)")
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            colnames = ["item", "date", "time", "acc_x", "acc_y", "acc_z", "gyr_x", "gyr_y", "gyr_z", "mag_x", "mag_y", "mag_z"]
            df = read_csv(filenames[0], delim_whitespace=True, skiprows=6, usecols=range(0, 12), names=colnames)
            if df.isnull().values.any():
                mensage = Mensage()
                mensage.set_text("Dataframe incompleto")
                center_relative(self, mensage)
                mensage.show()
            else:
                df = add_columns(df, dni)
                df = df.drop_duplicates(subset=["time"])
                if insert_df(df):
                    mensage = Mensage()
                    mensage.set_text("Se han insertado los datos correctamente")
                    center_relative(self, mensage)
                    mensage.show()
                else:
                    mensage = Mensage()
                    mensage.set_text("Ha habido un error al insertar los datos")
                    center_relative(self, mensage)
                    mensage.show()

    def plot(self, dni):
        self.chose_plot = ChosePlot(dni)
        center_relative(self, self.chose_plot)
        self.chose_plot.show()
