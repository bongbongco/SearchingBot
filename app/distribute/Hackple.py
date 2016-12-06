# -*- coding:utf-8 -*-
# !/usr/bin/python

import sys
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


reload(sys)
sys.setdefaultencoding('utf-8')

boardList = ["free_board"]

login_response = requests.post('http://hackple.co.kr/bbs/login_check.php', data={'url':'http%3A%2F%2Fhackple.co.kr'
, 'mb_id':'bongbongco'
, 'mb_password':'test'})

token_response = requests.post("http://hackple.co.kr/bbs/write_token.php", data={"bo_table":boardList[0]}, cookies = login_response.cookies)
jsonMessage = json.loads(token_response.content)

print jsonMessage["token"]

uid_response = requests.post("http://hackple.co.kr/bbs/ajax.autosave.php", data={"bo_table":boardList[0]}, cookies = login_response.cookies)

multipart_data = MultipartEncoder(
    fields={
            'field0': 'value0',
            'field1': 'value1',
           }
    )

response = requests.post('http://httpbin.org/post', data=multipart_data,
                  headers={'Content-Type': multipart_data.content_type})