# -*- coding: utf-8 -*-
# !/usr/bin/python

from requests import get
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue


user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36']


def YahooSearch(keyword):
    urls = []
    resultUrls = []
    quantity = GetTheConfig('yahoo','QUANTITY')
    page = 1
    user_agent = {
        'User-Agent': choice(user_agent_list)}

    while True:
        response = get('http://search.yahoo.co.jp/search?p=%s&b=%d' % (keyword, page),
                       headers=user_agent, timeout=5)
        html = response.text.encode('utf-8')
        soup = BeautifulSoup(html)

        elements = soup.findAll('div', {'class': 'hd'})
        for url in elements:
            for a in url.find_all('a', href=True):
                urls.append(a['href'])

        if page // 10 == int(quantity) // 10:
            break
        page = page + 10

    urls = DeduplicateValue(urls)

    for url in urls:
        resultUrls.append({"Yahoo": url})

    return resultUrls