from django.db import models
from core.models import UserProfile
from dashboard.models import Department
import datetime
from datetime import timedelta, date
from district_reporting.settings import EMAIL_HOST_USER
from django.core.mail import send_mail




def geting_date():
    initial_date = datetime.date(2019,12,23)
    deadline = initial_date + datetime.timedelta(days=5)
    print(deadline)
    return deadline

class ReportType(models.Model):
    WEEK = 1
    TERM = 2
    YEAR = 3
    TIME_CHOICES = (
        (WEEK, 'Icyumweru'),
        (TERM, 'Igihembwe'),
        (YEAR, 'Umwaka'),
    )
    report_type = models.CharField(max_length=300)
    igihe_itangirwa = models.PositiveSmallIntegerField(choices=TIME_CHOICES)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    deadline = models.DateTimeField(auto_now_add=True)


    def notify(self):
        before_deadline = self.deadline - datetime.timedelta(days=1)
        return before_deadline
  

    def __str__(self):
        return self.report_type


class Report(models.Model):
    report_type     = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    report_file     = models.FileField(upload_to='reports')
    submited_date   = models.DateTimeField(auto_now_add=True)





def mail( *args, **kwargs):
    subject = "Welcome "
    message = 'New Report has been added successfully !!!'
    recepient = 'byives21@gmail.com'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])

    return None
