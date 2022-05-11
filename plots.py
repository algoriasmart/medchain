from PyQt5.QtChart import QChart, QSplineSeries, QChartView, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout

import pyqtgraph as pg

from plots_ui import Ui_MainWindow


class PlotsPyQtChart(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_data_top(self, x, y1, y2, y3, title):
        chart = QChart()
        chart.setTitle(title)

        series = QSplineSeries()
        for xi, yi in zip(x, y1):
            series.append(xi, yi)
        series.setName("x")
        chart.addSeries(series)

        series = QSplineSeries()
        for xi, yi in zip(x, y2):
            series.append(xi, yi)
        series.setName("y")
        chart.addSeries(series)

        series = QSplineSeries()
        for xi, yi in zip(x, y3):
            series.append(xi, yi)
        series.setName("z")
        chart.addSeries(series)

        axisX = QValueAxis()
        axisX.setTitleText("Frame")
        axisX.setRange(min(x), max(x))
        chart.addAxis(axisX, Qt.AlignBottom)

        axisY = QValueAxis()
        axisY.setTitleText("s")
        axisY.setRange(min(min(y1), min(y2), min(y3)), max(max(y1), max(y2), max(y3)))
        chart.addAxis(axisY, Qt.AlignLeft)
        #chart.createDefaultAxes()

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        layout = QHBoxLayout(self.top)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(chartview)

    def set_data_mid(self, x, y1, y2, y3, title):
        chart = QChart()
        chart.setTitle(title)

        series = QSplineSeries()
        for xi, yi in zip(x, y1):
            series.append(xi, yi)
        series.setName("x")
        chart.addSeries(series)

        series = QSplineSeries()
        for xi, yi in zip(x, y2):
            series.append(xi, yi)
        series.setName("y")
        chart.addSeries(series)

        series = QSplineSeries()
        for xi, yi in zip(x, y3):
            series.append(xi, yi)
        series.setName("z")
        chart.addSeries(series)

        chart.createDefaultAxes()

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        layout = QHBoxLayout(self.mid)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(chartview)

    def set_data_bot(self, x, y1, y2, y3, title):
        chart = QChart()
        chart.setTitle(title)

        series = QSplineSeries()
        for xi, yi in zip(x, y1):
            series.append(xi, yi)
        series.setName("x")
        chart.addSeries(series)

        series = QSplineSeries()
        for xi, yi in zip(x, y2):
            series.append(xi, yi)
        series.setName("y")
        chart.addSeries(series)

        series = QSplineSeries()
        for xi, yi in zip(x, y3):
            series.append(xi, yi)
        series.setName("z")
        chart.addSeries(series)

        chart.createDefaultAxes()

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        layout = QHBoxLayout(self.bot)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(chartview)


class PlotsPyQtGraph(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_data_top(self, x, y1, y2, y3, title):
        plt = pg.plot()
        plt.showGrid(x=True, y=True)
        plt.addLegend()
        plt.setLabel('left', 'Vertical Values', units='y')
        plt.setLabel('bottom', 'Frame')
        line1 = plt.plot(x, y1, pen='g', name='x')
        line2 = plt.plot(x, y2, pen='r', name='y')
        line3 = plt.plot(x, y3, pen='b', name='z')

        layout = QHBoxLayout(self.top)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(plt)

    def set_data_mid(self, x, y1, y2, y3, title):
        plt = pg.plot()
        plt.showGrid(x=True, y=True)
        plt.addLegend()
        plt.setLabel('left', 'Vertical Values', units='y')
        plt.setLabel('bottom', 'Frame')
        line1 = plt.plot(x, y1, pen='g', name='x')
        line2 = plt.plot(x, y2, pen='r', name='y')
        line3 = plt.plot(x, y3, pen='b', name='z')

        layout = QHBoxLayout(self.mid)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(plt)

    def set_data_bot(self, x, y1, y2, y3, title):
        plt = pg.plot()
        plt.showGrid(x=True, y=True)
        plt.addLegend()
        plt.setLabel('left', 'Vertical Values', units='y')
        plt.setLabel('bottom', 'Frame')
        line1 = plt.plot(x, y1, pen='g', name='x')
        line2 = plt.plot(x, y2, pen='r', name='y')
        line3 = plt.plot(x, y3, pen='b', name='z')

        layout = QHBoxLayout(self.bot)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(plt)
