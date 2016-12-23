# -*- coding: utf-8 -*-
# !/usr/bin/env python

__author__ = 'breniey'

from flask import Flask, jsonify, request
import sys

sys.path.append('../')

import manager

app = Flask(__name__)

api_list = {
    'get': u'get an usable proxy',
    'refresh': u'refresh proxy pool',
    'get_all': u'get all proxy from proxy pool',
    'delete?proxy=127.0.0.1:8080': u'delete an unable proxy',
}


@app.route('/')
def index():
    return jsonify(api_list)


@app.route('/get/')
def get():
    proxy = manager().get()
    return proxy


@app.route('/refresh/')
def refresh():
    manager().refresh()
    return 'success'


@app.route('/get_all/')
def getAll():
    proxys = manager().getAll()
    return jsonify(proxys)


@app.route('/delete/', methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    manager().delete(proxy)
    return 'success'


if __name__ == '__main__':
    app.run()
