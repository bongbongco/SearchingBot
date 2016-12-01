# -*- coding: utf-8 -*-
# !/usr/bin/python

from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler
from Config import GetTheConfig
import time

class Scheduler(object):

    # 클래스 생성시 스케쥴러 데몬을 생성합니다.
    def __init__(self):
        self.sched = BackgroundScheduler()
        self.sched.start()
        self.job_id=''

    # 클래스가 종료될때, 모든 job들을 종료시켜줍니다.
    def __del__(self):
        self.shutdown()

    # 모든 job들을 종료시켜주는 함수입니다.
    def shutdown(self):
        self.sched.shutdown()

    # 특정 job을 종료시켜줍니다.
    def kill_scheduler(self, job_id):
        try:
            self.sched.remove_job(job_id)
        except JobLookupError as err:
            print "fail to stop scheduler: %s" % err
            return

    def searching(self, type, job_id):
        print("%s scheduler process_id[%s] : %d" % (type, job_id, time.localtime().tm_sec))
        print("Searching Data....")


    # 스케쥴러입니다. 스케쥴러가 실행되면서 hello를 실행시키는 쓰레드가 생성되어집니다.
    # 그리고 다음 함수는 type 인수 값에 따라 cron과 interval 형식으로 지정할 수 있습니다.
    # 인수값이 cron일 경우, 날짜, 요일, 시간, 분, 초 등의 형식으로 지정하여,
    # 특정 시각에 실행되도록 합니다.(cron과 동일)
    # interval의 경우, 설정된 시간을 간격으로 일정하게 실행실행시킬 수 있습니다.
    def scheduler(self, type, job_id):
        print "%s Scheduler Start" % type
        if type == 'interval':
            self.sched.add_job(self.searching, type, seconds=10, id=job_id, args=(type, job_id))
        elif type == 'cron':
            self.sched.add_job(self.searching, type
                               , day_of_week=GetTheConfig("schedule", "day_week")
                               , hour=GetTheConfig("schedule", "hour")
                               , minute=GetTheConfig("schedule", "minute")
                               , id=job_id
                               , args=(type, job_id))

def StartingSchedule():
    scheduler = Scheduler()
    # cron 스케쥴러를 실행시키며, job_id는 "1" 입니다.
    try :
        scheduler.scheduler('cron', "1")
        return True
    except:
        return False

        ''' 프로세스 종료 시 사용할 코드
            scheduler.kill_scheduler("1")
            print "######### kill cron schedule ##########"
        '''