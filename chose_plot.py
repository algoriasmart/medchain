from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMainWindow

from chose_plot_ui import Ui_MainWindow

from plots import PlotsPyQtChart, PlotsPyQtGraph, PlotsPyQtDataVisualization


class ChosePlot(QMainWindow, Ui_MainWindow):
    def __init__(self, dni):
        super().__init__()
        self.setupUi(self)
        self.init_data(dni)
        self.pyqtchart.clicked.connect(lambda: self.show_PyQtChart())
        self.pyqtgraph.clicked.connect(lambda: self.show_PyQtGraph())
        self.pyqtdatavisualization.clicked.connect(lambda: self.show_PyQtDataVisualization() )

    def init_data(self, dni):
        query = QSqlQuery()
        query.prepare("SELECT test.num_test FROM test INNER JOIN users ON users.id = test.id_paciente WHERE "
                      "users.identificador = :dni ORDER BY test.num_test DESC LIMIT 1")
        query.bindValue(":dni", dni)
        query.exec_()
        if query.next():
            num_test = query.value(0)
            query = QSqlQuery()
            query.prepare("SELECT item, acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, mag_x, mag_y, mag_z FROM test_unit "
                          "INNER JOIN users ON users.id = test_unit.id_paciente WHERE test_unit.num_test = :num_test "
                          "AND users.identificador = :dni")
            query.bindValue(":num_test", int(num_test))
            query.bindValue(":dni", dni)
            query.exec_()

            self.item = []
            self.acc_x = []
            self.acc_y = []
            self.acc_z = []
            self.gyr_x = []
            self.gyr_y = []
            self.gyr_z = []
            self.mag_x = []
            self.mag_y = []
            self.mag_z = []

            while query.next():
                self.item.append(query.value(0))
                self.acc_x.append(query.value(1))
                self.acc_y.append(query.value(2))
                self.acc_z.append(query.value(3))
                self.gyr_x.append(query.value(4))
                self.gyr_y.append(query.value(5))
                self.gyr_z.append(query.value(6))
                self.mag_x.append(query.value(7))
                self.mag_y.append(query.value(8))
                self.mag_z.append(query.value(9))

    def show_PyQtChart(self):
        self.plots = PlotsPyQtChart()
        self.plots.set_data_top(self.item, self.acc_x, self.acc_y, self.acc_z, "Aceleración", "m/s²")
        self.plots.set_data_mid(self.item, self.gyr_x, self.gyr_y, self.gyr_z, "Giroscopio", "rad/s")
        self.plots.set_data_bot(self.item, self.mag_x, self.mag_y, self.mag_z, "Magnetometro", "T")
        self.plots.show()
        self.hide()

    def show_PyQtGraph(self):
        self.plots = PlotsPyQtGraph()
        self.plots.set_data_top(self.item, self.acc_x, self.acc_y, self.acc_z, "Aceleración", "m/s²")
        self.plots.set_data_mid(self.item, self.gyr_x, self.gyr_y, self.gyr_z, "Giroscopio", "rad/s")
        self.plots.set_data_bot(self.item, self.mag_x, self.mag_y, self.mag_z, "Magnetometro", "T")
        self.plots.show()
        self.hide()

    def show_PyQtDataVisualization(self):
        self.plots = PlotsPyQtDataVisualization()
        self.plots.set_data_top(self.acc_x, self.acc_y, self.acc_z)
        self.plots.set_data_mid(self.gyr_x, self.gyr_y, self.gyr_z)
        self.plots.set_data_bot(self.mag_x, self.mag_y, self.mag_z)
        self.plots.show()
        self.hide()
