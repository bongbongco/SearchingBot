# -*- coding: utf-8 -*-
# !/usr/bin/python

from google import search
from time import sleep
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue


def RequestSearch(urls, keyword):
    searchCurs = 0
    for url in search(keyword, stop=int(GetTheConfig('google', 'QUANTITY'))): # API 이상 동작으로 검색량 조절 불가
        urls.append(url)
        searchCurs = searchCurs + 1
        sleep(1)
        if searchCurs == int(GetTheConfig('google', 'QUANTITY')):
            return urls  # 리턴 문에 문제가 있음 11/24

def GoogleSearch(keyword):
    urls = []
    resultUrls = []
    prefixs = {'filetype:doc '
        , 'filetype:pdf '
        , 'filetype:ppt '
        , 'filetype:hwp '
        , 'filetype:txt '} # 별도의 conf 파일로 분리 예정

    urls = RequestSearch(urls, keyword)
    for prefix in prefixs:
        urls = RequestSearch(urls, prefix+keyword)

    urls = DeduplicateValue(urls)

    for url in urls:
        resultUrls.append({"Google": url})
    return resultUrls


