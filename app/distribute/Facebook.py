# -*- coding: utf-8 -*-
# !/usr/bin/python

import re
from urllib import urlopen
from urllib import urlencode
import facebook
from Config import GetTheConfig

def FacebookSendPosting():
  # Fill in the values noted in previous steps here
  credentials = {
    "page_id" : GetTheConfig("facebook", "PAGE_ID"),  # Step 1
    "app_id" : GetTheConfig("facebook", "APP_ID"),
    "app_secret_code": GetTheConfig("facebook", "APP_SECRET_CODE"),
    }
  accessToken = getAccessToken(credentials)
  credentials["access_token"] = accessToken
  api = get_api(credentials)
  msg = "Hello, world!"
  status = api.put_wall_post(msg)
  print status

def get_api(credentials):
  graph = facebook.GraphAPI(credentials['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  response = graph.get_object('me/accounts')
  page_access_token = None
  for page in response['data']:
    if page['id'] == credentials['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph

def getAccessToken(credentials):
  BASE_URL = "https://graph.facebook.com/oauth/access_token?"
  params = {"client_id":credentials["app_id"],
            "client_secret":credentials["app_secret_code"],
            "grant_type":"client_credentials"
            }
  response = urlopen(BASE_URL + urlencode(params)).read()
  response = re.split('=', response)
  shortLiveAccess_token = response[1]
  params["fb_exchange_token"] = shortLiveAccess_token
  params["grant_type"] = "fb_exchange_token"
  response = urlopen(BASE_URL + urlencode(params)).read()
  print response
  return shortLiveAccess_token

#https://graph.facebook.com/oauth/access_token?client_id=1661442370813352&client_secret='f3e9f7649276855393ed7f29e9740287'&grant_type=fb_exchange_token&fb_exchange_token=1661442370813352|t4XZDjJNTYQYGrbQkx71TDsWS6w