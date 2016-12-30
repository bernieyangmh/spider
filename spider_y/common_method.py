# -*- coding: utf-8 -*-
# !/usr/bin/env python

import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5000/get/").content

def get_all_proxy():
    return requests.get("http://127.0.0.1:5000/get_all/").content

def delete_proxy(proxy):
    return requests.get("http://127.0.0.1:5000/delete/{}".format(proxy)).content