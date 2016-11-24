# -*- coding: utf-8 -*-
# !/usr/bin/python

def ExtractSearchUrl(searchResult, platform = None):
    urls = []
    imageUrls = []
    for urlList in searchResult:
        for urlDictionary in urlList:
            if "Youtube" == platform:
                urls.append(urlDictionary["Youtube"]["url"])
                imageUrls.append({urlDictionary["Youtube"]["url"]:urlDictionary["Youtube"]["image"]})
            else:
                urls.append(urlDictionary.values())

    if "Youtube" == platform:
        return urls, imageUrls
    return urls