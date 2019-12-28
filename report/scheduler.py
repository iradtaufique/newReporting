from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .models import * 

def start():
    nun = getattr(ReportType, 'deadline')
    
    print(nun)
    scheduler = BackgroundScheduler()
    scheduler.add_job(mail, 'date', run_date=date(2019,12,28) )
    scheduler.start()