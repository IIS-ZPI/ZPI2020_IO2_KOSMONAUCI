from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import icons_rc
import pyqtgraph as pg
from statisticsCalculator.coefficients import *
from statisticsCalculator.distribution_of_changes import *
from statisticsCalculator.session_count import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 290, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 4, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.mode = QtWidgets.QComboBox(self.frame_2)
        self.mode.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mode.setFont(font)
        self.mode.setObjectName("comboBox")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.currentTextChanged.connect(self.on_mode_changed)
        self.verticalLayout.addWidget(self.mode)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.time_interval_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.time_interval_label.setFont(font)
        self.time_interval_label.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.time_interval_label)
        self.time_interval = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.time_interval.setFont(font)
        self.time_interval.setObjectName("comboBox_3")
        self.time_interval.addItem("")
        self.time_interval.addItem("")
        self.time_interval.addItem("")
        self.time_interval.addItem("")
        self.time_interval.addItem("")
        self.time_interval.addItem("")
        self.verticalLayout_2.addWidget(self.time_interval)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.currency = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.currency.setFont(font)
        self.currency.setObjectName("comboBox_4")
        self.currency.addItem("")
        self.currency.addItem("")
        self.currency.addItem("")
        self.currency.addItem("")
        self.currency.addItem("")
        self.currency.addItem("")
        self.verticalLayout_3.addWidget(self.currency)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.currency_2_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.currency_2_label.setFont(font)
        self.currency_2_label.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.currency_2_label)
        self.currency_2 = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.currency_2.setFont(font)
        self.currency_2.setObjectName("comboBox_5")
        self.currency_2.addItem("")
        self.currency_2.addItem("")
        self.currency_2.addItem("")
        self.currency_2.addItem("")
        self.currency_2.addItem("")
        self.currency_2.addItem("")
        self.verticalLayout_4.addWidget(self.currency_2)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.draw)
        spacerItem2 = QtWidgets.QSpacerItem(87, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.graphicsView = PlotWidget(self.frame_3)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('w')
        self.graphicsView.showGrid(x=True, y=True)
        self.graphicsView.setMouseEnabled(False, False)
        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mode"))
        self.mode.setItemText(0, _translate("MainWindow", "Determine the number of sessions"))
        self.mode.setItemText(1, _translate("MainWindow", "Statistic measures"))
        self.mode.setItemText(2, _translate("MainWindow", "Changes distribution"))
        self.time_interval_label.setText(_translate("MainWindow", "Time Interval"))
        self.time_interval.setItemText(0, _translate("MainWindow", "1 week"))
        self.time_interval.setItemText(1, _translate("MainWindow", "2 weeks"))
        self.time_interval.setItemText(2, _translate("MainWindow", "1 month"))
        self.time_interval.setItemText(3, _translate("MainWindow", "1 quarter"))
        self.time_interval.setItemText(4, _translate("MainWindow", "half a year"))
        self.time_interval.setItemText(5, _translate("MainWindow", "1 year"))
        self.label_3.setText(_translate("MainWindow", "Currency"))
        self.currency.setItemText(0, _translate("MainWindow", "USD"))
        self.currency.setItemText(1, _translate("MainWindow", "CHF"))
        self.currency.setItemText(2, _translate("MainWindow", "AUD"))
        self.currency.setItemText(3, _translate("MainWindow", "GBP"))
        self.currency.setItemText(4, _translate("MainWindow", "UAH"))
        self.currency.setItemText(5, _translate("MainWindow", "EUR"))
        self.currency_2_label.setText(_translate("MainWindow", "Currency 2"))
        self.currency_2.setItemText(0, _translate("MainWindow", "EUR"))
        self.currency_2.setItemText(1, _translate("MainWindow", "GBP"))
        self.currency_2.setItemText(2, _translate("MainWindow", "UAH"))
        self.currency_2.setItemText(3, _translate("MainWindow", "USD"))
        self.currency_2.setItemText(4, _translate("MainWindow", "AUD"))
        self.currency_2.setItemText(5, _translate("MainWindow", "CHF"))
        self.pushButton.setText(_translate("MainWindow", "DRAW"))

    def on_mode_changed(self, value):
        _translate = QtCore.QCoreApplication.translate
        if value == 'Determine the number of sessions':
            self.currency_2.hide()
            self.currency_2_label.hide()
            self.time_interval.show()
            self.time_interval_label.show()

            self.prepare_time_interval_list(_translate)
        elif value == 'Statistic measures':
            self.currency_2.hide()
            self.currency_2_label.hide()
            self.time_interval.show()
            self.time_interval_label.show()

            self.prepare_time_interval_list(_translate)
        else:
            self.currency_2.show()
            self.currency_2_label.show()

            [self.time_interval.removeItem(0) for _ in range(6)]

            self.time_interval.addItem("")
            self.time_interval.addItem("")

            self.time_interval.setItemText(0, _translate("MainWindow", "1 month"))
            self.time_interval.setItemText(1, _translate("MainWindow", "1 quarter"))

    def prepare_time_interval_list(self, _translate):
        [self.time_interval.removeItem(0) for _ in range(6)]
        [self.time_interval.addItem("") for _ in range(6)]

        self.time_interval.setItemText(0, _translate("MainWindow", "1 week"))
        self.time_interval.setItemText(1, _translate("MainWindow", "2 weeks"))
        self.time_interval.setItemText(2, _translate("MainWindow", "1 month"))
        self.time_interval.setItemText(3, _translate("MainWindow", "1 quarter"))
        self.time_interval.setItemText(4, _translate("MainWindow", "half a year"))
        self.time_interval.setItemText(5, _translate("MainWindow", "1 year"))

    def draw(self):
        self.graphicsView.clear()
        self.graphicsView.setLabel('bottom', '')
        self.graphicsView.setLabel('left', '')
        styles = {'color': 'grey', 'font-size': '20px'}

        currency = self.currency.currentText()
        interval = self.time_interval.currentText()

        if self.mode.currentText() == "Statistic measures":
            if interval == "1 week":
                timedelta = relativedelta(weeks=1)
            elif interval == "2 weeks":
                timedelta = relativedelta(weeks=1)
            elif interval == "1 month":
                timedelta = relativedelta(months=1)
            elif interval == "1 quarter":
                timedelta = relativedelta(months=3)
            elif interval == "half a year":
                timedelta = relativedelta(months=6)
            elif interval == "1 year":
                timedelta = relativedelta(years=1)

            curr_date = datetime.now()
            date = curr_date - timedelta
            date = date.strftime("%Y-%m-%d")
            curr_date = curr_date.strftime("%Y-%m-%d")

            object = get_coefficients(currency, date, curr_date)

            labels = ("", "median", "stdDev", "mode", "coeffVar")
            y = [object.median, object.stDeviation, object.mode, object.coefficientVariation]

            ticks = [list(zip(range(len(labels)), labels))]
            x = [i for i in range(1, len(labels))]

            bargraph = pg.BarGraphItem(x=x, height=y, width=0.6, brush="#5871A3")
            axisX = self.graphicsView.getAxis('bottom')
            axisX.setTicks(ticks)

            self.graphicsView.addItem(bargraph)
        elif self.mode.currentText() == "Changes distribution":
            currency_2 = self.currency_2.currentText()
            if interval == "1 month":
                timedelta = relativedelta(months=1)
            elif interval == "1 quarter":
                timedelta = relativedelta(months=3)

            curr_date = datetime.now()
            date = curr_date - timedelta
            date = date.strftime("%Y-%m-%d")
            curr_date = curr_date.strftime("%Y-%m-%d")

            labels, y = get_distribution_of_changes(currency, currency_2, date, curr_date)

            ticks = [list(zip(range(len(labels) + 1), tuple([""] + labels)))]
            x = [i for i in range(1, len(labels) + 1)]

            bargraph = pg.BarGraphItem(x=x, height=y, width=0.6, brush="#5871A3")
            axisX = self.graphicsView.getAxis('bottom')
            axisX.setTicks(ticks)

            self.graphicsView.setLabel('bottom', currency_2, **styles)
            self.graphicsView.setLabel('left', 'Number of changes', **styles)

            self.graphicsView.addItem(bargraph)
        else:
            if interval == "1 week":
                labels, y = get_last_weeks_count(currency, 1)
            elif interval == "2 weeks":
                labels, y = get_last_weeks_count(currency, 2)
            elif interval == "1 month":
                labels, y = get_last_months_count(currency, 1)
            elif interval == "1 quarter":
                labels, y = get_last_months_count(currency, 3)
            elif interval == "half a year":
                labels, y = get_last_months_count(currency, 6)
            elif interval == "1 year":
                labels, y = get_last_months_count(currency, 12)

            ticks = [list(zip(range(len(labels) + 1), tuple([""] + labels)))]
            x = [i for i in range(1, len(labels) + 1)]

            bargraph = pg.BarGraphItem(x=x, height=y, width=0.6, brush="#5871A3")
            axisX = self.graphicsView.getAxis('bottom')
            axisX.setTicks(ticks)

            self.graphicsView.setLabel('left', 'Number of occurrence', **styles)

            self.graphicsView.addItem(bargraph)
