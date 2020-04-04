#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class ConfigReader():
    def __init__(self, name):
        super().__init__()
        self.name = name

    def load(self):
        with open(self.name, "r") as read_file:
            data = json.load(read_file)
        return data