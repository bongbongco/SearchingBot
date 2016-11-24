# coding=utf-8

# code by xi4okv QQ:48011203 site:xiaokui.cc

from urllib2 import urlopen
import re
from time import sleep
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue
from app.extract.Html import getHtml, getElement


def getRealUrl(storedBaiduUrls):
    realUrls = []
    regexRealUrl = re.compile(r'replace\(\".*?\"\)<')

    for url in storedBaiduUrls:
        html = getHtml(url)
        realUrl = getElement(regexRealUrl, html)
        try:
            realUrl = realUrl[0]
            realUrls.append(realUrl[9:-3])
        except:
            continue
        sleep(1)
    return realUrls


def BaiduSearch(keyword):
    urls = []
    count = -1
    page = int(GetTheConfig('baidu','QUANTITY')) + 1
    regexStoredBaiduUrl = re.compile(r'url":"(.*?)"}')


    while count < page:
        count = count + 1
        paging = 10 * count
        html = getHtml("http://www.baidu.com/s?wd=%s&pn=%s" % (keyword, str(paging)))
        storedBaiduUrls = getElement(regexStoredBaiduUrl, html)
        realUrls = getRealUrl(storedBaiduUrls)

        realUrls = DeduplicateValue(realUrls)

        for url in realUrls:
            urls.append({"Baidu":url})

    return urls