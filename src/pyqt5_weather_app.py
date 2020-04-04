#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import gmtime, strftime

from PySide2.QtWidgets import (QApplication, QLabel, QWidget, QHeaderView, QHBoxLayout, QTableView, QSizePolicy, QGridLayout)
from PySide2.QtCharts import QtCharts
from PySide2 import QtSvg
from datetime import datetime, timedelta

import widgets.weather_tile as weather_tile
import utilities.config_reader as config_reader
import utilities.requester as requester
import utilities.select_day as select_day
import widgets.chart as chart


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        config = config_reader.ConfigReader()
        data = config.load("config/config.json")
        print(data)
        appid = data["Api"]["Appid"]
        url = data["Api"]["Forecasts"]
        self.req = requester.Requester(appid,url)
        self.dataFromWebApi = self.req.fetch()
        print(self.dataFromWebApi)
        self.day_selector = select_day.SelectDay()
        day = strftime("%Y-%m-%d", gmtime())

        self.selected_dat = self.day_selector.select(self.dataFromWebApi, day)
        print(self.selected_dat)
        print(self.selected_dat[0])
        a,b,c,d = (self.selected_dat[0][0])
        print(a)
        print(b)
        self.interfejs()

    def interfejs(self):
        List = []
        self.dataFromWebApi = self.req.fetch()

        for i in range(0,5,1):
            from_now = datetime.now() + timedelta(hours=24*i)
            print(from_now)
            day = from_now.strftime('%Y-%m-%d')
            print("day:{}".format(day))
            self.selected_dat = self.day_selector.select( self.dataFromWebApi, day)
            min = 999
            max = -999
            print("self.selected_dat:{}".format(self.selected_dat))
            for j in range(0,len(self.selected_dat)):
                print("self.selected_dat[0][0]:{}".format(self.selected_dat[0][0]))
                a,b,c,d = (self.selected_dat[0][0])
                if c > max:
                    max = c
                if d < min:
                    min = d
            day2 = "random"
            svgName = "../weather-icons-master/svg/wi-day-cloudy.svg"
            icon = weather_tile.WeatherTile(svgName, day2, max, min)
            List.append(icon)
            print(icon)
            print("min:{}".format(min))
            print("max:{}".format(max))


        firstLayout = QGridLayout()
        for i in range(0,len(List)):
            firstLayout.addWidget(List[i], 0, i)

        mainLayout = QGridLayout()

        chart_widget = chart.Chart(self.selected_dat)
        mainLayout.addWidget(chart_widget, 0, 0)
        mainLayout.addLayout(firstLayout,1 ,0)

        self.setLayout(mainLayout)
        self.resize(300, 200)
        self.setWindowTitle("pyqt5")
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = MainWindow()
    sys.exit(app.exec_())