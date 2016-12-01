# -*- coding: utf-8 -*-
# !/usr/bin/python

from Database import executeNcommit, executeNfetchall, now
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue
from app.extract.SearchUrl import ExtractSearchUrl
from app.extract.SiteUrl import ExtractDomain
from app.schedule.Quantity import IncrementQuantity
from app.distribute.Gmail import SendGmail
import subprocess
from types import *


def IncrementSearchingQuantity():
    print "None Data"
    IncrementQuantity() # 검색 량 증가
    title = "[Increment Searching Quantity] " + now()
    message = "Crehacktive bot Increment Searching Quantity/Standard Increment : " + GetTheConfig('manager', 'standard_increment')  # 추후 결과 정보 추가 예정
    SendGmail(title, message, GetTheConfig('google', 'bot_admin'))
    result = subprocess.call('../bin/python ./CLI_Manager -r', shell=True)
    if result == GetTheConfig('string', 'RUN_SCHEDULE'):
        return True
    elif result == GetTheConfig('string', 'NON_SAVED'):
        return False


def SavingSearchData(searchResults):
    Unspecified = 1
    workerIndex = 0
    worker =[u"이승용", u"이상훈", u"김성규", u"하동민"]
    databaseStoredUrls = []
    sourceImageUrls = None
    matchWorkerUrls = []
    imageUrl = None

    if searchResults ==[] : # 검색된 값이 없는 경우
        IncrementSearchingQuantity()

    # 검색 결과에서 URL 만 추출
    sourceUrls, sourceImageUrls = ExtractSearchUrl(searchResults)

    # 중복 확인
    StoredSearchUrls = executeNfetchall(GetTheConfig('query', 'SELECT_DATA_RESEARCH-RESEARCHURL'))
    for StoredSearchUrl in StoredSearchUrls:
        databaseStoredUrls.append(StoredSearchUrl['researchUrl'])
    UniqueUrls = DeduplicateValue(sourceUrls, databaseStoredUrls)  # 데이터베이스에서 조회한 데이터와 비교하여 중복된 값 제거

    if UniqueUrls == []: # 데이터베이스에서 조회한 데이터와 비교 후 고유 값이 없으면 검색 량 증가
        IncrementSearchingQuantity()

    for url in UniqueUrls:
        for sourceImageUrl in sourceImageUrls:  # 썸네일 이미지
            if url == sourceImageUrl.keys()[0]:
                imageUrl = sourceImageUrl[url]
                break

        for searchResult in searchResults: # 플랫폼 종류
            for urlDictionary in searchResult:
                if urlDictionary.keys()[0] == "Youtube":
                    if url == urlDictionary[urlDictionary.keys()[0]]["url"]:
                        platform = urlDictionary.keys()[0]
                        break
                else:
                    if url == urlDictionary.values():
                        platform = urlDictionary.keys()[0]
                        break

        siteUrl = ExtractDomain(url)  # 도메인 추출
        matchWorkerUrls.append({'worker': worker[workerIndex]  # 담당자 지정
                                   , 'platform':platform
                                   , 'siteUrl': siteUrl
                                   , 'imageUrl': imageUrl
                                   , 'url': url})
        workerIndex = workerIndex + 1
        if workerIndex == 4:
            workerIndex = 0

    # 데이터베이스 저장
    for matchWorkerUrl in matchWorkerUrls:
        print matchWorkerUrl
        executeNcommit(GetTheConfig('query', 'INSERT_DATA'), (
        matchWorkerUrl['worker'], '', matchWorkerUrl['siteUrl'], matchWorkerUrl['url'], matchWorkerUrl['platform'], Unspecified,
        matchWorkerUrl['imageUrl'], str(now()), str(now('limit'))))

    return True