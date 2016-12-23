# -*- coding: utf-8 -*-
# !/usr/bin/env python

__author__ = 'berniey'

from apscheduler.schedulers.blocking import BlockingScheduler
from multiprocessing import Process
import requests
import time
import sys
from ProxyManager import ProxyManager

sys.path.append('../')
print sys.path


class ProxyRefreshSchedule(ProxyManager):
    """
    代理定时刷新
    """

    def __init__(self):
        ProxyManager.__init__(self)

    # 用代理连接百度，200则将代理put到useful_proxy_queue
    def validProxy(self):
        self.db.changeTable(self.raw_proxy_queue)
        raw_proxy = self.db.pop()
        while raw_proxy:
            proxies = {"http": "http://{proxy}".format(proxy=raw_proxy),
                       "https": "https://{proxy}".format(proxy=raw_proxy)}
            try:
                r = requests.get('https://www.baidu.com/', proxies=proxies, timeout=50, verify=False)
                if r.status_code == 200:
                    self.db.changeTable(self.useful_proxy_queue)
                    self.db.put(raw_proxy)
            except Exception as e:
                # print e
                pass
            self.db.changeTable(self.raw_proxy_queue)
            raw_proxy = self.db.pop()


def refreshPool():
    pp = ProxyRefreshSchedule()
    pp.validProxy()


def main(process_num=2):
    p = ProxyRefreshSchedule()
    p.refresh()

    for num in range(process_num):
        P = Process(target=refreshPool, args=())
        P.start()
    print '{time}: refresh complete!'.format(time=time.ctime())


if __name__ == '__main__':
    # pp = ProxyRefreshSchedule()
    # pp.main()
    main()
    sched = BlockingScheduler()
    sched.add_job(main, 'interval', seconds=3600)
    sched.start()
