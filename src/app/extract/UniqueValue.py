# -*- coding: utf-8 -*-
# !/usr/bin/python

from operator import eq
from types import *

def DeduplicateValue(sources, destinations=None):
    sourceTemp = []
    result = []
    duplicate = False

    if destinations == None: # 검색 단계에서 검색 결과 중 중복된 값 제거
        return CheckDeduplicateValue(sources)

    for source in sources:
        sourceTemp.append(ExtractValue(source)) # 데이터 타입에 맞게 URL 값 추출하여 새로운 리스트 구성

    return CheckDeduplicateValue(sourceTemp, destinations)

def CheckDeduplicateValue(sources, destination=None):
    result = []

    if not type(sources) == NoneType: # null check
        for source in sources:
            duplicate = False
            if destination == None:
                sourceTemp = sources[:] # 자기 자신과 비교
                sourceTemp.remove(source)  # remove는 인자 값과 일치하는 요소 하나를 제거
            elif not destination == None:
                sourceTemp = destination[:] # 데이터베이스에 저장된 데이터와 비교

            for temp in sourceTemp:
                if eq(temp, source):
                    duplicate = True

            if not duplicate:
                result.append(source)
    else:
        print "To occur NoneType"
    return result

def ExtractValue(source):
    if type(source[0]) is dict:
        return source[0]['url']
    else:
        return source