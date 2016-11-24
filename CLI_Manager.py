# -*- coding: utf-8 -*-
# !/usr/bin/python

import os
import sys
from getopt import getopt
from src.Config import GetTheConfig
from app.distribute.Gmail import SendGmail
from app.storage.Database import now, executeNcommit, executeNfetchall
from src.app.search.SearchManager import RegularSearch

reload(sys)
sys.setdefaultencoding('utf-8')


def help():
    print "usage : -s or --sns "
    return

def main():
    try:
        # 여기서 입력을 인자를 받는 파라미터는 단일문자일 경우 ':' 긴문자일경우 '='을끝에 붙여주면됨
        opts, args = getopt(sys.argv[1:], "s:r:h:", ["sns=", "run=", "help="])

    except getopt.GetoptError as err:
        print str(err)
        help()
        sys.exit(1)

    for opt, arg in opts:
        if (opt == "-s") or (opt == "--sns"):
            # 데이터베이스 정보 전달 받은 후 config.conf 파일에 쿼리 추가하여 사용 예정
            board = executeNfetchall(GetTheConfig("query", "distribute_test_query"), arg, "distribute")

            title = "[" + board[0]["user_name"] + "] " + now()
            message = board[0]["contents"]  # 게시글 본문이 html 형식인지 plain 형식인지에 따라 Gmail 모듈 변경

            SendGmail(title, message) # 게시글 읽은 후 SNS 배포

        elif (opt == "-r") or (opt == "--run"):
            result = RegularSearch()

            if result == True:
                print GetTheConfig('string', 'RUN_SCHEDULE')
            elif result == False:
                print GetTheConfig('string', 'NON_SAVED')

        elif (opt == "-h") or (opt == "--help") or (opt ==""):
            help()

    return

if __name__ == '__main__':
    main()