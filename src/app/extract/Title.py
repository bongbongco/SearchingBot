# -*- coding: utf-8 -*-
# !/usr/bin/python

from BeautifulSoup import BeautifulSoup

def ExtractTitle(html):
    soup = BeautifulSoup(html)
    try:
        title = soup.title.string
    except:
        title = "blank"

    return title.rstrip('\r')