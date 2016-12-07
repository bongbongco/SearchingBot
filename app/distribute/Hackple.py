# -*- coding:utf-8 -*-
# !/usr/bin/python

import sys
import requests
import mechanicalsoup
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


reload(sys)
sys.setdefaultencoding('utf-8')

boardList = ["free_board"]

subject ="자유로운 자유 게시판"
content ="자유 게시판의 글 작성은 자유롭습니다"


browser = mechanicalsoup.Browser()
loginPage = browser.get("http://hackple.co.kr/bbs/login.php")
loginForm = loginPage.soup.select("form.eyoom-form")[0]

loginForm.select("input")[1]["value"] = "bongbongco"# ID 
loginForm.select("input")[2]["value"] = "r+E7h9bJvt9n$MLE"# Password  

loginMainPage = browser.submit(loginForm, loginPage.url)
print loginMainPage # 로그인 성공
writePage = browser.get("http://hackple.co.kr/bbs/write.php?bo_table="+boardList[0]) # 쿠키 값 유지하여 글 쓰기 페이지 이동 
writeForm = writePage.soup.select("form")[1]

uid = writeForm.select("input")[0]["value"]

print uid

token_response = browser.post("http://hackple.co.kr/bbs/write_token.php", data={"bo_table":boardList[0]})
jsonMessage = json.loads(token_response.content)
token = jsonMessage["token"]
print token

multipart_data = MultipartEncoder(
    fields={
            "token":token,
            "uid":uid,
            "w":"",
            "bo_table":boardList[0],
            "wr_id":"0",
            "sca":"",
            "sfl":"",
            "stx":"",
            "spt":"",
            "sst":"",
            "sod":"",
            "page":"",
            "board_skin_path":"/home/hackplea/public_html/hackple.co.kr/eyoom/core/board",
            "wr_1":"2|2",
            "wr_2":"",
            "wr_3":"",
            "wr_4":"",
            "wr_5":"",
            "wmode":"",
            "html":"html1",
            "wr_subject":subject,
            "wr_content":"<p>"+content+"</p>",
            "wr_link1":"",
            "wr_link2":""
           }
    )

response = browser.post("http://hackple.co.kr/bbs/write_update.php", data=multipart_data, headers={'Content-Type': multipart_data.content_type})

print response.content
