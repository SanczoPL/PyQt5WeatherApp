#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide2.QtCore import QDateTime, Qt
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QWidget, QHeaderView, QHBoxLayout, QTableView,
    QSizePolicy)
from PySide2.QtCharts import QtCharts


class Chart(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.model = data
        # Creating QChart
        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.add_series("godzina", [0, 1])

        # Creating QChartView
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # QWidget Layout
        self.main_layout = QHBoxLayout()
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # Right Layout
        size.setHorizontalStretch(4)
        self.chart_view.setSizePolicy(size)
        self.main_layout.addWidget(self.chart_view)

        # Set the layout to the QWidget
        self.setLayout(self.main_layout)

    def add_series(self, name, columns):
        # Create QLineSeries
        self.series = QtCharts.QLineSeries()
        self.series.setName(name)

        # Filling QLineSeries
        for i in range(len(self.model)):
            # Getting the data
            x, y,_,_ = self.model[i][0]

            self.series.append(int(x), int(y))

        self.chart.addSeries(self.series)
        self.chart.legend().setVisible(False)

        # Setting X-axis
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTickCount(len(self.model))

        self.axis_x.setTitleText("hour")
        self.axis_x.setLabelFormat("%d:00")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)
        # Setting Y-axis
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(1.0)
        self.axis_y.setLabelFormat("%.1f")
        self.axis_y.setTitleText("temperature")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        # Getting the color from the QChart to use it on the QTableView
        #self.model.color = "{}".format(self.series.pen().color().name())
