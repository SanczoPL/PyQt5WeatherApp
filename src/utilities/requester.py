#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


class Requester():
    def __init__(self, appid, url):
        super().__init__()
        self.url = url.format(appid)

    def fetch(self):
        r = requests.get(self.url)
        return json.loads(r.text)