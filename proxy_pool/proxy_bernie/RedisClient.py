# -*- coding: utf-8 -*-
# !/usr/bin/env python


import random
import json
import redis

class RedisClient(object):
    """
    Reids client
    """

    def __init__(self, name, host, port):
        """
        init
        :param name:
        :param host:
        :param port:
        :return:
        """
        self.name = name
        self.pool = redis.ConnectionPool(host=host, port=port)
        self.__conn = redis.StrictRedis(connection_pool=self.pool)

    def get(self):
        """
        get an item
        :return:
        """
        values = self.__conn.smembers(name=self.name)

        return random.choice(list(values)) if values else None

    def put(self, value):
        """
        put an  item
        :param value:
        :return:
        """
        value = json.dump(value, ensure_ascii=False).encode('utf-8') if isinstance(value, (dict, list)) else value
        return self.__conn.sadd(self.name, value)

    def pop(self):
        """
        pop an item
        :return:
        """
        value = self.get()
        if value:
            self.__conn.srem(self.name, value)
        return value

    def delete(self, value):
        """
        delete an item
        :param key:
        :return:
        """
        self.__conn.srem(self.name, value)

    def getAll(self):
        return self.__conn.smembers(self.name)

    def changeTable(self, name):
        self.name = name
