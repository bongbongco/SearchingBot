
from app.search.PlatformManager import GatheringInformation
from app.storage.Database import now, executeNcommit, executeNfetchall
from Config import GetTheConfig, WriteTheConfig
from app.storage.DataManager import SavingSearchData
#from app.distribute.NaverCafeDistribute import NaverPublishedMessage
from app.distribute.Twitter import TwitterDistribute
'''dstribute test'''
#NaverPublishedMessage()
#TwitterDistribute('test')

''' search test
keywords = executeNfetchall(GetTheConfig('query','select_keyword_research-keyword'))
for keyword in  keywords:
    searchResult = GatheringInformation(keyword.get('keyword'))
    SavingSearchData(searchResult)
'''

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = re.compile(r"(http[s]?|ftp):\/\/([a-z0-9-]+\.)+[a-z0-9]{2,4}")

test_str = "http://netsecurity.51cto.com/art/201408/448305_all.htm"
extractDomain = regex.search(test_str)
print extractDomain.group()
'''
matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                         end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                         end=match.end(groupNum),
                                                                         group=match.group(groupNum)))
'''
