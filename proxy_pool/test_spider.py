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
        d = tree.xpath('.//table[@class="table"]/tbody/tr[{}]/td'.format(i+1))[0]
        o = d.xpath('.//span/text() | .//div/text()')
        yield ''.join(o[:-1]) + ':' + o[-1]

print 'start'
a = 1
for i in freeProxyFifth():
    print a
    print i
    a += 1
