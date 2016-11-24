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

def SavingSearchData(searchResult):
    Unspecified = 1
    workerIndex = 0
    worker =[u"이승용", u"이상훈", u"김성규", u"하동민"]
    #platform = ["Bing", "Google", "Twitter", "Yahoo", "Facebook", "Youtube"]
    databaseStoredUrls = []
    sourceImageUrls = None
    matchWorkerUrls = []
    imageUrl = None


    try:
        platform = searchResult[0][0].keys()[0]
        if "Youtube" == platform: # youtube 여부 판별
            sourceUrls, sourceImageUrls = ExtractSearchUrl(searchResult, 'Youtube')
        # 검색 결과에서 URL 만 추출
        else:
            sourceUrls = ExtractSearchUrl(searchResult)
        # 중복 확인
        StoredSearchUrls = executeNfetchall(GetTheConfig('query', 'SELECT_DATA_RESEARCH-RESEARCHURL'))
        for StoredSearchUrl in StoredSearchUrls:
            databaseStoredUrls.append(StoredSearchUrl['researchUrl'])
        UniqueUrls = DeduplicateValue(sourceUrls, databaseStoredUrls)  # 데이터베이스에서 조회한 데이터와 비교하여 중복된 값 제거

        if UniqueUrls == []: # 데이터베이스에서 조회한 데이터와 비교 후 고유 값이 없으면 검색 량 증가
            IncrementSearchingQuantity()

        for url in UniqueUrls:
            if "Youtube" == platform: # youtube 여부 판별
                for sourceImageUrl in sourceImageUrls:  # 썸네일 이미지
                    if url == sourceImageUrl.keys()[0]:
                        imageUrl = sourceImageUrl[url]
                        break
            siteUrl = ExtractDomain(url)  # 도메인 추출
            matchWorkerUrls.append({'worker': worker[workerIndex]  # 담당자 지정
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
            matchWorkerUrl['worker'], '', matchWorkerUrl['siteUrl'], matchWorkerUrl['url'], platform, Unspecified,
            matchWorkerUrl['imageUrl'], str(now()), str(now('limit'))))

        return True

    except: # 검색된 값이 없는 경우
        IncrementSearchingQuantity()

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
