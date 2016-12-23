# -*- coding: utf-8 -*-
# !/usr/bin/env python

import requests
from common import robustCrawl, getHtmlTree


def freeProxyFifth():
    """
    抓取guobanjia http://www.goubanjia.com/free/gngn/index.shtml
    :return:
    """
    url = "http://www.goubanjia.com/free/gngn/index.shtml"
    tree = getHtmlTree(url)
    # 现在每天最多放15个（一页）
    for i in xrange(15):
        if tree.xpath('.//table[@class="table"]/tbody/tr[{}]/td[2]/a/text()'.format(i+1))[0] ==U'高匿':
            # yield ''.join(proxy_list[0].xpath('.//text()'))
            pass
            proxy_list1 = tree.xpath('.//table[@class="table"]/tbody/tr[{}]/td'.format(i+1))[0]
            d = tree.xpath('.//table[@class="table"]/tbody/tr[{}]/td'.format(i+1))[0]
            d = tree.xpath('.//table[@class="table"]/tbody/tr[{}]/td'.format(i+1))[0]

            g = proxy_list1.xpath('.//text()')
            o = d.xpath('.//span/text() | .//div/text()')
            o1=o[:-1]
            o2=o[-1]
            p = ''.join(o1)+':'+o2
            # b=''.join(d[:-1])+':'+d[-1]
        proxy_list = tree.xpath('.//table[@class="table"]/tbody/tr[{}]/td'.format(i+1))

    for proxy in proxy_list:
        a = proxy.xpath('.//text()')
        c = ''.join(proxy.xpath('.//text()'))
        yield ''.join(proxy.xpath('.//text()'))


    # url = "http://www.goubanjia.com/free/gngn/index.shtml"
    # tree = getHtmlTree(url)
    # proxy_list1 = tree.xpath('.//td[@class="ip"]')
    # proxy_list = tree.xpath('.//td[@class="ip"]/div | //td[@class="ip"]/span')
    # for proxy in proxy_list:
    #     b=''.join(proxy.xpath('.//text()'))
    #     yield ''.join(proxy.xpath('.//text()'))




print 'start'
a = 1
for i in freeProxyFifth():
    print a
    print i
    a += 1
