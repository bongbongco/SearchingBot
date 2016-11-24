# -*- coding: utf-8 -*-
# !/usr/bin/python

from twitter import Twitter, OAuth
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def TwitterSearch(keyword):
    urls = []
    resultUrls = []
    hangul = re.compile('[ㄱ-ㅣ가-힣]+')  # 한글과 띄어쓰기를 제외한 모든 글자

    # 트위터 API 사용 인증용 토큰 값
    ACCESS_TOKEN = GetTheConfig('twitter', 'ACCESS_TOKEN')
    ACCESS_SECRET = GetTheConfig('twitter', 'ACCESS_SECRET')
    CONSUMER_KEY = GetTheConfig('twitter', 'CONSUMER_KEY')
    CONSUMER_SECRET = GetTheConfig('twitter', 'CONSUMER_SECRET')

    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter = Twitter(auth=oauth)
    params = {'result_type':'recent', 'count':int(GetTheConfig('twitter', 'QUANTITY'))}

    if(hangul.match(keyword)):
        params['lang'] = 'ko'
    params['q'] = keyword
    query = twitter.search.tweets(**params)

    for resultEntries in query["statuses"]:
        resultEntry = resultEntries["entities"]["urls"]

        for url in resultEntry:
            urls.append(url[u"expanded_url"])

        urls = DeduplicateValue(urls)

        for url in urls:
            resultUrls.append({"Twitter":url})

    return resultUrls