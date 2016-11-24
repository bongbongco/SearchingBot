# -*- coding: utf-8 -*-
# !/usr/bin/python

import sys
import re


def favicon(domain):
    favicon = "/favicon.ico"
    faviconUrl = domain + favicon
    return faviconUrl