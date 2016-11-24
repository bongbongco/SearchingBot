# -*- coding: utf-8 -*-
# !/usr/bin/python

from urllib2 import urlopen
import re

def getHtml(url):
    response = urlopen(url)
    html = response.read()
    return html

def getElement(regex, html):
    Element = re.findall(regex, html)
    return Element