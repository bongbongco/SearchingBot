# -*- coding: utf-8 -*-
# !/usr/bin/python

import json
import facebook
from requests import get
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue

access_token = GetTheConfig('facebook','app_id') + "|" + GetTheConfig('facebook','app_secret_code')

def GetTheUrl(post):
    return GetTheConfig('facebook','base_url')+ post['id']


def FacebookSearch(keyword):
    urls = []
    resultUrls = []
    response = get("https://graph.facebook.com/search?access_token=" + access_token +  "&q=" + keyword + "&type=page")
    data = response.text.encode('utf-8')
    jsonData = json.loads(data)
    page = 1
    user = jsonData["data"][0]["id"]  # 값 하나하나 접근하기

    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(user)
    posts = graph.get_connections(profile['id'], connection_name='posts')

    while True:
        for post in posts['data']:
            urls.append({"Facebook":GetTheUrl(post=post)})
        try:
            posts = get(posts['paging']['next']).json()
        except:
            posts = False
        finally:
            if not posts or page == GetTheConfig('facebook', 'QUANTITY'):
                break
        page = page + 1

    urls = DeduplicateValue(urls)

    for url in urls:
        resultUrls.append({"Facebook": url})

    return resultUrls