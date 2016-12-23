# -*- coding: utf-8 -*-
# !/usr/bin/env python

__author__ = 'berniey'

import os
import sys
from common import GetConfig
from common import Singleton
import RedisClient
import logging
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class DbClient(object):
    """
    DbClient
    """

    __metaclass__ = Singleton

    def __init__(self):
        """
        init
        :return:
        """
        self.config = GetConfig()
        self.__initDbClient()

    def __initDbClient(self):
        """
        init DB Client
        :return:
        """
        __type = None
        if "Redis" == self.config.db_type:
            __type = "RedisClient"
        else:
            pass
        assert __type, 'type error, Not support DB type: {}'.format(self.config.db_type)
        self.client = getattr(__import__(__type), __type)(name=self.config.db_name,
                                                          host=self.config.db_host,
                                                          port=self.config.db_port)

    def get(self, **kwargs):
        return self.client.get(**kwargs)

    def put(self, value, **kwargs):
        return self.client.put(value, **kwargs)

    def pop(self, **kwargs):
        logging.info(self)
        return self.client.pop(**kwargs)

    def delete(self, value, **kwargs):
        return self.client.delete(value, **kwargs)

    def getAll(self):
        return self.client.getAll()

    def changeTable(self, name):
        self.client.changeTable(name)

if __name__ == "__main__":
    account = DbClient()
    account.name = 'name'
    print account.get()

    account.put('312312')
    print(account)
