# -*- coding: utf-8 -*-
# !/usr/bin/python

from sqlalchemy import Column, Integer, VARCHAR, TEXT, CHAR
from Database import Base


class Data_Research(Base):
    __tablename__ = 'data_research'
    idx = Column(Integer(11), primary_key=True, autoincrement=True)
    worker = Column(VARCHAR(50), nullable=False)
    title = Column(VARCHAR(255), nullable=False)
    content = Column(TEXT)
    siteUrl = Column(VARCHAR(100), nullable=False)
    researchUrl = Column(VARCHAR(255), nullable=False)
    workUrl = Column(VARCHAR(255), default=None)
    srcPlatform = Column(VARCHAR(255), default=None)
    dstPlatform = Column(VARCHAR(255), default=None)
    grade = Column(Integer, default=None)
    state = Column(VARCHAR(255), default=1)
    thumbImg = Column(VARCHAR(255), default=None)
    updateDate = Column(CHAR(20), default=None)
    searchDate = Column(CHAR(20), default=None)
    workDate = Column(CHAR(20), default=None)
    limitDate = Column(CHAR(20), default=None)
    keepDate = Column(CHAR(20), default=None)
    deployType = Column(Integer(11), default=None)

class Keyword_Research(Base):
    __tablename__ = 'keyword_research'
    idx = Column(Integer(11), primary_key=True, autoincrement=True)
    keyword = Column(VARCHAR(200), nullable=False)
    count = Column(Integer(11), nullable=False)
    recentDate = Column(CHAR(20), default=None)

class Site_Research(Base):
    __tablename__ = 'site_research'
    idx = Column(Integer(11), primary_key=True, autoincrement=True)
    site = Column(VARCHAR(100), nullable=False)
    count = Column(Integer(11), nullable=False)
    recentDate = Column(CHAR(20), default=None)



    def __repr__(self):
        return '<User %r>' % (self.name)