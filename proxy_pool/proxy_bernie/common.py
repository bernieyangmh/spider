# -*- coding: utf-8 -*-
# !/usr/bin/env python

__author__ = 'berniey'

import os
from ConfigParser import ConfigParser


def robustCrawl(func):
    def decorate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print u"sorry, 抓取出错。错误原因:"
            print e

    return decorate

class LazyProperty(object):
    """
    LazyProperty
    explain: http://www.spiderpy.cn/blog/5/
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class ConfigParse(ConfigParser):
    """
    rewrite ConfigParser, for support upper option
    """

    def __init__(self):
        ConfigParser.__init__(self)

    def optionxform(self, optionstr):
        return optionstr


class Singleton(type):
    """
    Singleton Metaclass
    """

    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton, cls).__call__(*args)
        return cls._inst[cls]




class GetConfig(object):
    """
    to get config from config.ini
    """

    def __init__(self):
        self.pwd = os.path.split(os.path.realpath(__file__))[0]
        # self.config_path = os.path.join(os.path.split(self.pwd)[0], 'Config.ini')
        self.config_path = '/Users/a00301955/Documents/fun_test/proxy_pool/proxy_bernie/Config.ini'
        self.config_file = ConfigParse()
        self.config_file.read(self.config_path)

    @LazyProperty
    def db_type(self):
        return self.config_file.get('DB', 'type')

    @LazyProperty
    def db_name(self):
        return self.config_file.get('DB', 'name')

    @LazyProperty
    def db_host(self):
        return self.config_file.get('DB', 'host')

    @LazyProperty
    def db_port(self):
        return int(self.config_file.get('DB', 'port'))

    @LazyProperty
    def proxy_getter_functions(self):
        return self.config_file.options('ProxyGetter')


# 构造一个延迟计算属性，提升性能


def verifyProxy(proxy):
    """
    检查代理格式
    :param proxy:
    :return:
    """
    import re
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    return True if re.findall(verify_regex, proxy) else False



##TODO 可以在spider中复用
def getHtmlTree(url, **kwargs):
    """
    获取html树
    :param url:
    :param kwargs:
    :return:
    """
    import requests
    from lxml import etree
    html = requests.get(url=url).content
    return etree.HTML(html)

