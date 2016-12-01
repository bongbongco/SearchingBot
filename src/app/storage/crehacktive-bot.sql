create database crehacktive_bot;
use crehacktive_bot;

create table data_research (
idx int not null auto_increment,
worker varchar(50) not null,
title varchar(255) not null,
content text,
siteUrl varchar(100) not null,
researchUrl varchar(255) not null,
workUrl varchar(255),
srcPlatform varchar(255),
dstPlatform varchar(255),
grade int,
state varchar(255) default 1,
thumbImg varchar(255),
updateDate char(20),
searchDate char(20),
workDate char(20),
limitDate char(20),
keepDate char(20),
deployType int,
PRIMARY KEY(idx)
) ENGINE=MyISAM DEFAULT CHARSET = utf8;

create table site_research (
idx int not null auto_increment,
site varchar(100) not null,
count int not null,
recentDate char(20),
PRIMARY KEY(idx)
) ENGINE=MyISAM DEFAULT CHARSET = utf8;

create table keyword_research (
idx int not null auto_increment,
keyword  varchar(200) not null,
count int not null,
recentDate char(20),
PRIMARY KEY(idx)
) ENGINE=MyISAM DEFAULT CHARSET = utf8;
