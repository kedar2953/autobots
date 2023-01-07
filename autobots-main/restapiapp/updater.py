from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .views import sending_email

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(sending_email , 'interval' , second = 5)
    scheduler.add_job(sending_email , 'cron' , day_of_week = 'mon-fri' ,  hour = 15 , minute = 22)
    scheduler.start()