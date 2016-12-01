# -*- coding: utf-8 -*-
# !/usr/bin/python

from app.distribute.Gmail import SendGmail
from Database import executeNcommit, executeNfetchall, now
from Config import GetTheConfig
import re


def SyncSite():
    storedSiteUrls = executeNfetchall(GetTheConfig('query','select_distinct_siteUrl'))

    for siteUrlDic in storedSiteUrls:
        siteUrl = siteUrlDic["siteUrl"]
        removeProtocal = re.compile(r'https://|http://|ftp://')
        siteUrl = removeProtocal.sub('', siteUrl) # 프로토콜 제거
        numberOfSite = NumberOfValue(GetTheConfig('query', 'count_data_research_siteUrl'), '%'+siteUrl) # 해당 도메인에서 검색된 결과 개수
        columnExist = NumberOfValue(GetTheConfig('query', 'count_site_research_siteUrl') , siteUrl) # 데이터베이스에 해당 도메인 값 존재 여부

        if columnExist == 0:
            executeNcommit(GetTheConfig('query', 'insert_site'), (siteUrl, numberOfSite, now()))
        elif columnExist == 1:
            executeNcommit(GetTheConfig('query', 'update_site'), (numberOfSite, now(), siteUrl))
        else:
            title = "[Check Database ] " + now()
            message = "Check database - [site_research] duplicate siteUrl ("+siteUrl+")"  # 추후 결과 정보 추가 예정
            SendGmail(title, message, GetTheConfig('google', 'bot_admin'))

def NumberOfValue(query, value):
    result = executeNfetchall(query, value)
    return int(result[0]["count(*)"])  # 데이터베이스 조회 결과에서 count 값 추출