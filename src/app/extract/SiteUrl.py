# -*- coding: utf-8 -*-
# !/usr/bin/python

import sys
import re


def ExtractDomain(fullUrl):
    domainRegex = re.compile(r"(http[s]?|ftp):\/\/([a-z0-9-]+\.)+[a-z0-9]{2,4}")
    if type(fullUrl) is list:
        fullUrl = fullUrl[0]
    extractDomain = domainRegex.search(fullUrl)
    return extractDomain.group()