# -*- coding: utf-8 -*-
# !/usr/bin/python

import sys
from urllib import urlopen
from urllib import urlencode
import logging
import json

#from app.utils.Config import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

def TelegramSendMsg(chat_id, text, reply_to=None, no_preview=None, keyboard=None):
    u"""send_msg: 메시지 발송
    chat_id:    (integer) 메시지를 보낼 채팅 ID
    text:       (string)  메시지 내용
    reply_to:   (integer) ~메시지에 대한 답장
    no_preview: (boolean) URL 자동 링크(미리보기) 끄기
    keyboard:   (list)    커스텀 키보드 지정
    https://api.telegram.org/bot{{token}}/getUpdates #chat_id 받아오기
    """
    #BASE_URL = 'https://api.telegram.org/bot' + config.get('telegram', 'TOKEN')

    BASE_URL = 'https://api.telegram.org/bot' + '281236042:AAHZo82yFGMmM937tmpp2gPvxU_ydGxJAVs'

    params = {
        'chat_id': str(chat_id),
        'text': text.encode('utf-8'),
    }
    if reply_to:
        params['reply_to_message_id'] = reply_to
    if no_preview:
        params['disable_web_page_preview'] = no_preview
    if keyboard:
        reply_markup = json.dumps({
            'keyboard': keyboard,
            'resize_keyboard': True,
            'one_time_keyboard': False,
            'selective': (reply_to != None),
        })
        params['reply_markup'] = reply_markup

    try:
        urlopen((BASE_URL + '/sendMessage?'+urlencode(params))).read()
    except Exception as e:
        logging.exception(e)

TelegramSendMsg(149071544, 'https://inspirit.net.in/books/cheatsheets/SQL%20Injection%20Cheat%20Sheet.pdf')