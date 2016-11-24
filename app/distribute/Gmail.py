# -*- coding:utf-8 -*-
# !/usr/bin/python

import os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email import Encoders
from Config import GetTheConfig


# 주의 사항 하루 발송 메일 제한 500개
# 주의 https://myaccount.google.com/security?pli=1#connectedapps 에서 보안 수준이 낮은 앱 허용

def SendGmail(subject, message, to=None, attach=None):
    gmail_username = GetTheConfig('google', 'gmail_username')  # email User
    gmail_user = GetTheConfig('google', 'gmail_user')  # email Address
    gmail_pwd = GetTheConfig('google', 'gmail_pwd')  # email password

    msg = MIMEMultipart('alternative')

    if not to == None:
        msg['To'] = to
    else:
        msg['To'] = gmail_user
        to = gmail_user

    msg['From'] = gmail_username
    msg['Subject'] = Header(subject, 'utf-8')  # 제목
    msg.attach(MIMEText(message, 'plain', 'utf-8'))  # 내용이 평문일 경우
    #msg.attach(MIMEText(message, 'html', 'utf-8'))  # 내용이 html일 경우

    if not attach == None: # 첨부파일이 존재하는 경우 - 일반 글 배포 외 다른 용도로 사용 시
        part=MIMEBase('application','octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()