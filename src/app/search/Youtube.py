# -*- coding: utf-8 -*-
# !/usr/bin/python

from googleapiclient.discovery import build
from Config import GetTheConfig
from app.extract.UniqueValue import DeduplicateValue


def GetInformation(contentsInformation):
  searchResultUrl = GetTheConfig('youtube', 'base_url') + contentsInformation['id']
  searchResultUrlDic = { "url":(GetTheConfig('youtube', 'base_url')+ contentsInformation['id'])
                         , "image":contentsInformation['image']
  }

  return searchResultUrl, searchResultUrlDic


def ExtractInformation(resultUrl, resultDic, search_result):
  contentInformation = {"title":search_result["snippet"]["title"]
                          ,"id":search_result["id"]["videoId"]
                          ,"image":search_result["snippet"]["thumbnails"]["high"]["url"]}

  searchResultUrl, searchResultDic = GetInformation(contentInformation)

  resultUrl.append(searchResultUrl)
  resultDic.append(searchResultDic)
  return resultUrl, resultDic


def YoutubeSearch(keyword):
  resultUrls = []
  resultDic = []
  urls = []
  # API 사용 인증 토큰
  DEVELOPER_KEY = GetTheConfig('youtube', 'DEVELOPER_KEY')
  YOUTUBE_API_SERVICE_NAME = "youtube"
  YOUTUBE_API_VERSION = "v3"

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=keyword,
    part="id,snippet",
    maxResults=GetTheConfig('youtube', 'QUANTITY')
  ).execute()

  for search_result in search_response.get("items", []):
    if "youtube#video" == search_result["id"]["kind"]:
      resultUrls, resultDic = ExtractInformation(resultUrls, resultDic, search_result)

  deduplicateUrls = resultUrls #11/11 중복 제거 로직 테스트 후 재 반영
  # 중복제거한 URL 값을 이용하여 중복 제거한 Dictionary 만들기
  for resultUrl in resultUrls:
    for dicUrl in resultDic:
      if dicUrl['url'] == resultUrl:
        urls.append({"Youtube": dicUrl})
        break

  return urls