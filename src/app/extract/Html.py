# -*- coding: utf-8 -*-
# !/usr/bin/python

import httplib
from urllib2 import urlopen
import re
from app.distribute.Gmail import SendGmail
from Config import GetTheConfig
from app.storage.Database import now


def getHtml(url):
    response = urlopen(url)
    try:
        html = response.read()
    except httplib.IncompleteRead, e:
        page = e.partial
        title = "[Baidu Error] " + now()
        message = "Baidu Error " + page # 추후 결과 정보 추가 예정
        SendGmail(title, message, GetTheConfig('google', 'bot_admin'))
        html = "Online Shield"

    return html

def getElement(regex, html):
    Element = re.findall(regex, html)
    return Element