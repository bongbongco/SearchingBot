# -*- coding: utf-8 -*-
# !/usr/bin/python

from Config import GetTheConfig, WriteTheConfig


def IncrementQuantity():
    Standard_increment = int(GetTheConfig('manager', 'standard_increment'))
    platforms = ['google', 'twitter', 'bing', 'baidu', 'yahoo'] #  Youtube는 API 상으로 50이 최대 값

    for platform in platforms:
        if platform == 'baidu':
            Standard_increment = Standard_increment - 9
        WriteTheConfig(platform, 'quantity', int(GetTheConfig(platform, 'quantity')) + Standard_increment)
        Standard_increment = int(GetTheConfig('manager', 'standard_increment'))
