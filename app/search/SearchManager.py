# -*- coding: utf-8 -*-
# !/usr/bin/python

from Config import GetTheConfig, WriteTheConfig
from app.storage.Database import now, executeNcommit, executeNfetchall
from app.search.PlatformManager import GatheringInformation
from app.storage.DataManager import SavingSearchData
from app.distribute.Gmail import SendGmail

def RegularSearch():
    keywords = executeNfetchall(GetTheConfig('query', 'select_keyword_research-keyword'))
    for keyword in keywords:
        searchResult = GatheringInformation(keyword.get('keyword'))
        result = SavingSearchData(searchResult)
        if result == False:
            return False
        title = "[Search Complete] " + now()
        message = "Crehacktive bot Search Complete" # 추후 결과 정보 추가 예정
        SendGmail(title, message, GetTheConfig('google', 'bot_admin'))
        return True