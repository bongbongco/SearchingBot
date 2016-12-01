# -*- coding: utf-8 -*-
# !/usr/bin/python

from twitter import Twitter, OAuth
import twitter
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def TwitterDistribute(message):
    # 트위터 API 사용 인증용 토큰 값
    ACCESS_TOKEN = GetTheConfig('twitter', 'ACCESS_TOKEN')
    ACCESS_SECRET = GetTheConfig('twitter', 'ACCESS_SECRET')
    CONSUMER_KEY = GetTheConfig('twitter', 'CONSUMER_KEY')
    CONSUMER_SECRET = GetTheConfig('twitter', 'CONSUMER_SECRET')
    twitterApi = Twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_SECRET)

    print(twitterApi.VerifyCredentials())
    #status = twitterApi.PostUpdate('I love python-twitter!')
    #print(status.text)