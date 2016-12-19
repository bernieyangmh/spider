#-*-coding:utf-8-*-
import scrapy
# from scrapy.loader import ItemLoader
# from spider.items import ImageItem
from bs4 import BeautifulSoup
import requests
from lxml import etree
import os
import urllib2
import urllib
import cookielib
import time

meta = {
    'dont_redirect': True,  # 禁止网页重定向
}


def get(url):
    try:
        r = requests.get(url)
        if r.ok:
            encoding = requests.utils.get_encodings_from_content(r.text)
            r.encoding = encoding[0] if encoding else requests.utils.get_encoding_from_headers(r.headers)
            return r.text
        else:
            raise Exception(r.status_code)
    except requests.RequestException as e:
        raise Exception(e)


class Spider(scrapy.Spider):
    name = "spiderjd"
    allowed_domains = ['jd.com']
    start_urls = [
        'https://list.jd.com/list.html?cat=1320,1583&ev=exbrand%5F17332&trans=1&JL=3_%E5%93%81%E7%89%8C_%E6%97%BA%E6%97%BA#J_crumbsBar'
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse,
                                    errback=self.errback,
                                    dont_filter=True)


    def parse(self, response):
        start_time = time.time()
        html = etree.HTML(response.text)
        names,imgs = get_img_name(html)
        next_page_url = html.xpath('//div[@id="J_bottomPage"]/span/a[@class="pn-next"]/@href')
        if next_page_url:
            next_page = 'https://list.jd.com' + next_page_url[0]

        print '耗时{}秒'.format(time.time()-start_time)
        time.sleep(3)
        yield scrapy.Request(next_page, callback=self.parse, meta=meta)


    # def parse_item(self, response):
    #     il = ItemLoader(item=ImageItem(), response=response)
    #     il.add_css('image_urls', 'img::attr(src)')
    #     return il.load_item()
    #
    def errback(self, failure):
        pass



def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_file(url):
    try:
        urlopen = urllib.URLopener()
        fp = urlopen.open('http:'+url)
        data = fp.read()
        return data
    except BaseException, e:
        print e
        return None


def save_file(path, file_name, data):
    if data:
        if not os.path.exists(path):
            os.makedirs(path)
        file = open(path + file_name, "wb")
        file.write(data)
        file.flush()
        file.close()


def get_img_name(html):
    names = []
    imgs = []
    for i in xrange(65):

        img_url = html.xpath(
            '//div[@id="plist"]/ul/li[%d]/div/div[@class="p-img"]/a/img/@src' % (i + 1))
        if not img_url:
            img_url = html.xpath(
                '//div[@id="plist"]/ul/li[%d]/div/div[@class="p-img"]/a/img/@data-lazy-img' % (i + 1))
        if img_url:
            imgs.append(img_url[0][2:])
        else:
            continue
        name = html.xpath(
            '//div[@id="plist"]/ul/li[%d]/div/div[@class="p-name"]/a/em' % (i + 1))
        name_zn = name[0].text.replace("/", "|");
        data = get_file(img_url[0])
        save_file("../JDIMG/", "%s.jpg" % name_zn, data=data)
        names.append(name_zn)
    return names,imgs