# -*- coding: utf-8 -*-
# !/usr/bin/python

#from urllib2 import urlopen
#from Config import GetTheConfig
#from app.extract.Html import getHtml, getElement
import mechanicalsoup


client_id = "IizDJ5NIz3PRn6sAL7PF"
client_secret = "BXxDfE7kpT"
oauth_token = "UtTNbJiXFun8MZ83"

browser = mechanicalsoup.Browser()
loginPage = browser.get("https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id="+client_id+"&state=hackpletest&redirect_uri=http%3A%2F%2Fcafe.naver.com&oauth_token="+oauth_token)
#print loginPage
loginForm = loginPage.soup.select("#content")[0].select("form")[0]
#print loginForm
loginForm.select("#id")[0]['value'] = "bongbongco"
loginForm.select("#pw")[0]['value'] = ",Q.6cRUpYCf2E8Ar"
JK
print loginForm

page2 = browser.submit(loginForm, loginPage.url)

print page2.soup

def NaverPublishedMessage():
    '''
    params = {"client_id":GetTheConfig('naver', 'CLIENT_ID')
    #,"client_secret":GetTheConfig('naver', 'CLIENT_SECRET')
    ,"oauth_token":GetTheConfig('naver', 'OAUTH_TOKEN')}


    response = urlopen()
    print response.headers
    '''
