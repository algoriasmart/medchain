# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chose_plot.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.background)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.container1 = QtWidgets.QFrame(self.background)
        self.container1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container1.setObjectName("container1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.container1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pyqtchart = QtWidgets.QPushButton(self.container1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pyqtchart.setFont(font)
        self.pyqtchart.setObjectName("pyqtchart")
        self.horizontalLayout_3.addWidget(self.pyqtchart, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.container1)
        self.container2 = QtWidgets.QFrame(self.background)
        self.container2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container2.setObjectName("container2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.container2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pyqtgraph = QtWidgets.QPushButton(self.container2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pyqtgraph.setFont(font)
        self.pyqtgraph.setObjectName("pyqtgraph")
        self.horizontalLayout_4.addWidget(self.pyqtgraph, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.container2)
        self.frame = QtWidgets.QFrame(self.background)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pyqtdatavisualization = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pyqtdatavisualization.setFont(font)
        self.pyqtdatavisualization.setObjectName("pyqtdatavisualization")
        self.horizontalLayout_5.addWidget(self.pyqtdatavisualization)
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pyqtchart.setText(_translate("MainWindow", "PyQtChart"))
        self.pyqtgraph.setText(_translate("MainWindow", "PyQtGraph"))
        self.pyqtdatavisualization.setText(_translate("MainWindow", "PyQtDataVisualization"))
