# -*- coding: utf-8 -*-
# !/usr/bin/env python

import re
import sys
import requests
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from common import robustCrawl, getHtmlTree


class GetFreeProxy(object):
    """
    proxy getter
    """

    def __init__(self):
        pass

    @staticmethod
    @robustCrawl
    def freeProxyFirst(page=10):
        """
        抓取快代理IP http://www.kuaidaili.com/
        :param page: 翻页数
        :return:
        """
        # 增加判断是否为高匿名的条件
        url_list = ('http://www.kuaidaili.com/proxylist/{page}/'.format(page=page) for page in range(1, page + 1))
        for url in url_list:
            tree = getHtmlTree(url)
            for i in xrange(10):

                if tree.xpath('.//div[@id="index_free_list"]//tbody/tr[{}]/td[3]'.format(i + 1))[0].text == u'高匿名':
                    proxy_host = tree.xpath('.//div[@id="index_free_list"]//tbody/tr[{}]/td[1]/text()'.format(i + 1))[0]
                    proxy_port = tree.xpath('.//div[@id="index_free_list"]//tbody/tr[{}]/td[2]/text()'.format(i + 1))[0]
                    proxy = proxy_host + ':' + proxy_port
                    yield proxy

    @staticmethod
    @robustCrawl
    def freeProxySecond(proxy_number=100):
        """
        抓取代理66 http://www.66ip.cn/
        :param proxy_number: 代理数量
        :return:
        """
        # 貌似全是高匿代理
        url = "http://m.66ip.cn/mo.php?sxb=&tqsl={}&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=".format(
                proxy_number)
        html = requests.get(url).content
        for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html):
            yield proxy

    @staticmethod
    @robustCrawl
    def freeProxyThird(days=1):
        """
        抓取有代理 http://www.youdaili.net/Daili/http/
        :param days:
        :return:
        """
        # 并未告知是否为高匿代理，弃用
        # url = "http://www.youdaili.net/Daili/http/"
        # tree = getHtmlTree(url)
        # page_url_list = tree.xpath('.//div[@class="chunlist"]/ul//a/@href')[0:days]
        # for page_url in page_url_list:
        #     html = requests.get(page_url).content
        #     proxy_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html)
        #     for proxy in proxy_list:
        #         yield proxy
        pass




    @staticmethod
    @robustCrawl
    def freeProxyFourth():
        """
        抓取西刺代理 http://api.xicidaili.com/free2016.txt
        :return:
        """
        # 打不开网页，弃用
        # url = "http://api.xicidaili.com/free2016.txt"
        # html = requests.get(url).content
        # for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html):
        #     yield proxy

    @staticmethod
    @robustCrawl
    def freeProxyFifth():
        """
        抓取guobanjia http://www.goubanjia.com/free/gngn/index.shtml
        :return:
        """
        url = "http://www.goubanjia.com/free/gngn/index.shtml"
        tree = getHtmlTree(url)
        proxy_list = tree.xpath('.//td[@class="ip"]')
        for proxy in proxy_list:
            yield ''.join(proxy.xpath('.//text()'))


if __name__ == '__main__':
    gg = GetFreeProxy()
    a=1
    for e in gg.freeProxyFourth():
        print a
        print e
        a += 1
