#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


class SelectDay():
    def __init__(self):
        super().__init__()

    def select(self, data, day):
        selected_day = []

        print(len(data["list"]))
        for i in range(0, len(data["list"])):
            date_time_obj = datetime.datetime.strptime(data["list"][i]["dt_txt"], '%Y-%m-%d %H:%M:%S')
            print(date_time_obj.day)
            if date_time_obj.date().strftime('%Y-%m-%d') == day:
                day_temp = []
                print("good")
                day_temp.append(((data["list"][i]["dt_txt"]), data["list"][i]["main"]["temp"]))
                selected_day.append(day_temp)
        return selected_day