# -*- coding: utf-8 -*-
# !/usr/bin/python

from Baidu import BaiduSearch
from Bing import BingSearch
from Facebook import FacebookSearch
from Google import GoogleSearch
from Twitter import TwitterSearch
from Youtube import YoutubeSearch
from Yahoo import YahooSearch
from Facebook import FacebookSearch
from multiprocessing import Process, Queue


def GatheringInformation(keyword):
    searchResult = []

    searchResult.append(BaiduSearch(keyword))
    #searchResult.append(BingSearch(keyword))
    #searchResult.append(GoogleSearch(keyword))
    #searchResult.append(TwitterSearch(keyword))
    #searchResult.append(YahooSearch(keyword))
    #searchResult.append(FacebookSearch(keyword))
    #searchResult.append(YoutubeSearch(keyword))

    return searchResult

''' 11/12 멀티 프로세싱 로직 폐기 - 오류 수정 후 반영 예정
searchProcess = []
#BaiduQueue = Queue();
    #BingQueue = Queue(); GoogleQueue = Queue(); TwitterQueue = Queue();
    #YahooQueue = Queue(); FacebookQueue = Queue(); YoutubeQueue = Queue();
    #YoutubeQueue = Queue();

    #searchProcess.append(Process(target=BaiduSearch, args=(keyword, BaiduQueue)))
    #searchProcess.append(Process(target=BingSearch, args=(keyword, BingQueue)))
    #searchProcess.append(Process(target=GoogleSearch, args=(keyword, GoogleQueue)))
    #searchProcess.append(Process(target=TwitterSearch, args=(keyword, TwitterQueue)))
    #searchProcess.append(Process(target=YahooSearch, args=(keyword, YahooQueue)))
    #searchProcess.append(Process(target=FacebookSearch, args=(keyword, FacebookQueue)))
    #searchProcess.append(Process(target=YoutubeSearch, args=(keyword, YoutubeQueue)))

    #for proc in searchProcess:
    #    proc.start()

    #BaiduResult = BaiduQueue.get();
    #BingResult = BingQueue.get(); GoogleResult = GoogleQueue.get();
    #TwitterResult = TwitterQueue.get(); YahooResult = YahooQueue.get(); FacebookResult = FacebookQueue.get();
    #YoutubeResult = YoutubeQueue.get();

    #BaiduQueue.close();
    #BingQueue.close(); GoogleQueue.close(); TwitterQueue.close();
    #YahooQueue.close(); FacebookQueue.close(); YoutubeQueue.close();
    #YoutubeQueue.close();

    #searchResult.append(BaiduResult);
    #searchResult.append(BingResult); searchResult.append(GoogleResult);
    #searchResult.append(TwitterResult); searchResult.append(YahooResult); searchResult.append(FacebookResult);
    #searchResult.append(YoutubeResult);
'''


