#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from time import gmtime, strftime


class SelectDay():
    def __init__(self):
        super().__init__()

    def select(self, data, day): 
        selected_day = []
        now = strftime("%Y-%m-%d", gmtime())
        print("Date :{}".format(now))
        print("Date is in future")
        for i in range(0, len(data["list"])):
            date_time_obj = datetime.datetime.strptime(data["list"][i]["dt_txt"], '%Y-%m-%d %H:%M:%S')
            if date_time_obj.date().strftime('%Y-%m-%d') == day:
                day_temp = []
                daytime = datetime.datetime.strptime(data["list"][i]["dt_txt"], '%Y-%m-%d %H:%M:%S')
                day_insert = daytime.strftime('%H')
                day_temp.append((day_insert, data["list"][i]["main"]["temp"], data["list"][i]["main"]["temp_max"], data["list"][i]["main"]["temp_min"]))

                selected_day.append(day_temp)
        return selected_day