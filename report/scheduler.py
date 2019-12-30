from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import *

def start():
    nun = getattr(ReportType, 'deadline')

    print(nun)
    report = ReportType.objects.values('deadline')

   
    # nun = getattr(ReportType, 'deadline')

    print('============================================')
    print(report)
    print('============================================')
    print('hsssssssssss')
    scheduler = BackgroundScheduler()
    scheduler.add_job(mail, 'date', run_date=date(2019,12,27) )
    scheduler.start()