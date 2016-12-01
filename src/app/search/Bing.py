# -*- coding: utf-8 -*-
# !/usr/bin/python

from py_bing_search import PyBingWebSearch
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue

def BingSearch(keyword):
    urls = []
    bing_web = PyBingWebSearch(GetTheConfig('bing', 'Key'), keyword, web_only=False)
    results = bing_web.search(limit=int(GetTheConfig('bing', 'QUANTITY')), format='json')
    for result in results:
        url = result.url
        urls.append(url)

    results = DeduplicateValue(urls)
    urls =[]

    for result in results:
        urls.append({"Bing":result})

    return urls