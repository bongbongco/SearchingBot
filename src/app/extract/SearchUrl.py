# -*- coding: utf-8 -*-
# !/usr/bin/python

from types import *

def ExtractSearchUrl(searchResult):
    urls = []
    imageUrls = []
    for urlList in searchResult:
        for urlDictionary in urlList:
            platform = urlDictionary.keys()[0]
            if platform == "Youtube":
                urls.append(urlDictionary[platform]["url"])
                imageUrls.append({urlDictionary[platform]["url"]: urlDictionary[platform]["image"]})
            else:
                urls.append(urlDictionary.values())

    return urls, imageUrls