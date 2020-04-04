#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from PyQt5 import QtSvg
#from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PySide2.QtWidgets import (QApplication, QLabel, QWidget, QHeaderView, QHBoxLayout, QTableView, QSizePolicy, QGridLayout)
from PySide2 import QtSvg

class WeatherTile(QWidget):
    def __init__(self, svgImage, labelname, max, min):
        super().__init__()
        self.svgWidget = QtSvg.QSvgWidget(svgImage)
        self.label = QLabel(labelname, self)
        self.labelMin = QLabel(str(min))
        self.labelMax = QLabel(str(max))
        # Instance:
        self.schemeLabelMinMax = QGridLayout()
        self.widgetMinMax = QWidget()
        self.scheme = QGridLayout()
        self.init_ui()

    def init_ui(self):

        self.schemeLabelMinMax.addWidget(self.labelMax, 0, 0)
        self.schemeLabelMinMax.addWidget(self.labelMin, 0, 1)
        self.widgetMinMax.setLayout(self.schemeLabelMinMax)
        self.scheme.addWidget(self.label, 0, 0)
        self.scheme.addWidget(self.svgWidget, 1, 0)
        self.scheme.addWidget(self.widgetMinMax, 2, 0)
        self.setLayout(self.scheme)

        self.setWindowTitle('Burning widget')
        self.setMinimumSize(100, 200)
        self.show()
