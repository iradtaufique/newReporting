from calendar import monthrange

from django.db import models
from core.models import UserProfile
from dashboard.models import Department
import datetime
from datetime import timedelta

import arrow
from django.core.exceptions import ValidationError

# this function get currrent datetime, and return next friday
def weekly_deadline(day,weekday):
    week_deadline = weekday - day.weekday()
    if week_deadline <= 0:
        week_deadline +=7
    return day + datetime.timedelta(week_deadline)
day = datetime.datetime.now()




class ReportType(models.Model):
    WEEK = 1
    MONTH = 2
    TERMESTER = 3
    SEMESTER = 4
    YEAR = 5

    TIME_CHOICES = (
        (WEEK, 'Icyumweru'),
        (MONTH, 'Ukwezi'),
        (TERMESTER, 'Igihembwe'),
        (SEMESTER, 'Amezi atandatu'),
        (YEAR, 'Umwaka'),
    )
    report_type = models.CharField(max_length=300)
    igihe_itangirwa = models.PositiveSmallIntegerField(choices=TIME_CHOICES,help_text="eg: Icyumweru, Ukwezi etc..")
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    deadline = models.DateTimeField(blank=True, null=True)


    # save constractor that get the current date and genete deadline of report type depanding on igihe_itangirwa.
    # and save dealine value into deadline fielad
    def save(self,*args,**kwargs):
        if self.igihe_itangirwa == 1:
            self.deadline = weekly_deadline(day,4)

        elif self.igihe_itangirwa == 2:
            monthly = lambda ded_lne:monthrange(ded_lne.year, ded_lne.month)[1]
            today = datetime.datetime.now()
            monthly_deadline = today.replace(day=5) + timedelta(monthly(today))

            self.deadline = monthly_deadline

        elif self.igihe_itangirwa == 3:
            self.deadline = datetime.datetime.now() + datetime.timedelta((3*365/12) + 5)

        elif self.igihe_itangirwa == 4:
            self.deadline = datetime.datetime.now() + datetime.timedelta((6*365/12) + 5)
        elif self.igihe_itangirwa == 5:
            self.deadline = datetime.datetime.now() + datetime.timedelta((12*365/12))
        super(ReportType,self).save(*args,**kwargs)



    def __str__(self):
        return self.report_type


    


class Report(models.Model):
    report_type     = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    report_file     = models.FileField(upload_to='reports')
    submitted_on   = models.DateTimeField(auto_now_add=True,blank=True, null=True)


    def clean(self):
        report_time = arrow.get(self.submitted_on)

        today = datetime.datetime.now()
        if report_time > arrow.utcnow():
            raise ValidationError(
                " you can not generate future report"
            )











