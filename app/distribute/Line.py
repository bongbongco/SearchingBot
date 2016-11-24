# -*- coding: utf-8 -*-
# !/usr/bin/python

from app.utils.Config import ConfigParser
from flask import Flask, request, abort
from Config import GetTheConfig

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)





def LineSendMsg(event):
    config = ConfigParser()
    line_bot_api = LineBotApi(config.get('line', 'ACCESS_TOKEN'))
    handler = WebhookHandler(config.get('line', 'SECRET_TOKEN'))

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))