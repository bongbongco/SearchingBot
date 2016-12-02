# -*- coding: utf-8 -*-
# !/usr/bin/python

import pymysql
from datetime import timedelta, date
from Config import GetTheConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def connect_db(readData="save"):
	if readData == "distribute":
		DB = GetTheConfig('database', 'board_DB')
	elif readData == "save":
		DB = GetTheConfig('database', 'bot_DB')

	conn = pymysql.connect(host=GetTheConfig('database', 'HOST')
						   , user=GetTheConfig('database', 'USER')
						   , password=GetTheConfig('database', 'PASSWORD')
						   , db=DB
						   , charset=GetTheConfig('database', 'CHARSET'))
	return conn

def init_db():
  Base.metadata.create_all(engine)


def get_db(conn):
	curs = conn.cursor(pymysql.cursors.DictCursor)
	return curs


def now(limit=None):
	now = date.today()
	if None == limit:
		nowTime = "%04d-%02d-%02d" % (now.year, now.month, now.day)
	else:
		now = now + timedelta(days=7)
		nowTime = "%04d-%02d-%02d" % (now.year, now.month, now.day)
	return nowTime


def executeNfetchall(sql, params=None, readData="save"):
	conn = connect_db(readData)
	curs = get_db(conn)
	if not params==None:
		curs.execute(sql, params)
	else:
		curs.execute(sql)
	return curs.fetchall()


def executeNcommit(sql, params):
	conn = connect_db()
	curs = get_db(conn)
	curs.execute(sql, params)
	conn.commit()
	conn.close()
