#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class ConfigReader():
    def __init__(self):
        super().__init__()

    def load(self, name):
        with open(name, "r") as read_file:
            data = json.load(read_file)
        return data
