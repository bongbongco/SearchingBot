# -*- coding: utf-8 -*-
# !/usr/bin/python

from app.distribute.Gmail import SendGmail
from Database import executeNcommit, executeNfetchall, now
from Config import GetTheConfig
import re


def SyncSite():
    storedSiteUrls = executeNfetchall(GetTheConfig('query','distinct_siteUrl'))

    for siteUrl in storedSiteUrls:
        removeProtocal = re.compile(r'https://|http://|ftp://')
        siteUrl = removeProtocal.sub('', siteUrl) # 프로토콜 제거
        numberOfSite = executeNfetchall(GetTheConfig('query', 'count_data_research_siteUrl'), siteUrl)

        if executeNfetchall(GetTheConfig('query', 'count_site_research_siteUrl') , siteUrl) == 0:
            executeNcommit(GetTheConfig('query', 'insert_site'), siteUrl, numberOfSite, now())
        elif executeNfetchall(GetTheConfig('query', 'count_site_research_siteUrl') , siteUrl) == 1:
            executeNcommit(GetTheConfig('query', 'update_site'), numberOfSite, now(), siteUrl)
        else:
            title = "[Check Database ] " + now()
            message = "Check database - (site_research) duplicate siteUrl"  # 추후 결과 정보 추가 예정
            SendGmail(title, message, GetTheConfig('google', 'bot_admin'))
