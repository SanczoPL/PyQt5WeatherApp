#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5 import QtSvg
import json

import widgets.weather_tile as weather_tile
import utilities.config_reader as config_reader
import utilities.requester as requester
import utilities.select_day as select_day

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()
        config = config_reader.ConfigReader()
        data = config.load("config/config.json")
        print(data)
        appid = data["Api"]["Appid"]
        url = data["Api"]["Forecasts"]
        req = requester.Requester(appid,url)
        dataFromWebApi = req.fetch()
        print(dataFromWebApi)
        day_selector = select_day.SelectDay()
        day = '2020-04-05'
        selected_dat = day_selector.select(dataFromWebApi,day)
        print(selected_dat)

    def interfejs(self):
        List = []
        svgName="../weather-icons-master/svg/wi-day-light-wind.svg"
        day = "pt."
        min="-1º"
        max="10º"
        icon = weather_tile.WeatherTile(svgName, day,max ,min )

        svgName = "../weather-icons-master/svg/wi-day-cloudy.svg"
        day = "sob."
        min = "-2º"
        max = "11º"
        icon2 = weather_tile.WeatherTile(svgName, day, max, min)

        firstLayout = QGridLayout()
        svgWidget = QtSvg.QSvgWidget(svgName)
        firstLayout.addWidget(icon, 0, 0)
        firstLayout.addWidget(icon2, 0, 1)
        self.setLayout(firstLayout)
        self.resize(300, 200)
        self.setWindowTitle("pyqt5")
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = MainWindow()
    sys.exit(app.exec_())