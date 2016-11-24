# -*- coding: utf-8 -*-
# !/usr/bin/python

import os
import configparser

os.chdir(os.path.dirname(os.path.abspath( __file__ ))) # 작업 경로 변경


def ConfigParser():
    config = configparser.RawConfigParser()
    config.read('config.conf')
    return config

def GetTheConfig(category, item):
    config = ConfigParser()
    result = config.get(category, item)
    return result

def WriteTheConfig(category, item, value):
    config = ConfigParser()
    config.set(category, item, value)
    with open('config.conf', 'wb') as configfile:
        config.write(configfile)
