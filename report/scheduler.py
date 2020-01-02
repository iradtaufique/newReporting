from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from .models import *

from district_reporting.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import datetime
from datetime import date


# this function get currrent datetime, and return next three_months/trimester
def trimester_from_now():

    term = datetime.date.today() + datetime.timedelta((3 * 365 / 12))
    return term


# this function get currrent datetime, and return next thursday

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


d = datetime.datetime.now()
next_friday = next_weekday(d, 3)


# ========================================================== WEEKLY ==================================================

# function that get all owners asigned to report with week,and append it to term[] to
# send them email remainder at the same time
def all_users_emails_week():
    weekly = []
    for email in ReportType.objects.all():

        if email.igihe_itangirwa == 1:
            weekly.append(email.owner.user.email)

    return weekly


# email function of all_users_emails_week

def mailweek(*args, **kwargs):
    subject = "Report Remainder "
    message = "Dear, " \
              "Sir/Madam we just wanted to remind you about submitting reports.' \
              'Don't forget to submit on time " \
              "Thank you!!!"
    send_mail(subject, message, EMAIL_HOST_USER, all_users_emails_week())

    return None

    # ================================================= MONTHLY =================================================


# function that get all owners asigned to report with month,and append it to term[] to
# send them email remainder at the same time
def all_users_emails_monthly():
    month = []

    for email in ReportType.objects.all():

        if email.igihe_itangirwa == 2:
            month.append(email.owner.user.email)
    return month


# email function of all_users_emails_monthly
def mailmonth(*args, **kwargs):
    subject = "Report Remainder "
    message = "Dear, " \
              "Sir/Madam we just wanted to remind you about submitting reports.' \
              'Don't forget to submit on time " \
              "Thank you!!!"
    send_mail(subject, message, EMAIL_HOST_USER, all_users_emails_monthly())

    return None


# ===================================================== TRIMESTER ==========================================
# Termester
# function that get all owners asigned to report with trimester,and append it to term[] to
# send them email remainder at the same time
def all_users_emails_term():
    term = []

    for email in ReportType.objects.all():

        if email.igihe_itangirwa == 3:
            term.append(email.owner.user.email)
    return term


# email function of all_users_emails_term
def mailterm(*args, **kwargs):
    subject = "Report Remainder "
    message = "Dear, " \
              "Sir/Madam we just wanted to remind you about submitting reports.' \
              'Don't forget to submit on time " \
              "Thank you!!!"
    send_mail(subject, message, EMAIL_HOST_USER, all_users_emails_term())

    return None

# ========================================================SEMESTER ================================================================
def all_users_emails_semester():
    semester = []

    for email in ReportType.objects.all():

        if email.igihe_itangirwa == 4:
            semester.append(email.owner.user.email)
    return semester


# email function of all_users_emails_semester
def mailsemester(*args, **kwargs):
    subject = "Report Remainder "
    message = "Dear, " \
              "Sir/Madam we just wanted to remind you about submitting reports.' \
              'Don't forget to submit on time " \
              "Thank you!!!"
    send_mail(subject, message, EMAIL_HOST_USER, all_users_emails_semester())

    return None

# ============================================ YEAR ==============================================================================

def all_users_emails_year():
    year = []

    for email in ReportType.objects.all():

        if email.igihe_itangirwa == 4:

            year.append(email.owner.user.email)
    return year


# email function of all_users_emails_year
def mailyear(*args, **kwargs):
    subject = "Report Remainder "
    message = "Dear, " \
              "Sir/Madam we just wanted to remind you about submitting reports.' \
              'Don't forget to submit on time " \
              "Thank you!!!"
    send_mail(subject, message, EMAIL_HOST_USER, all_users_emails_year())

    return None


# ========================================================== DEADLINE REMAINDER =================================================
def dealine_week(*args, **kwargs):
    subject = "Deadline Notification "
    message = "We just want to inform you that, Name has not been submitted on time." \
              "Thank you"
    send_mail(subject, message, EMAIL_HOST_USER, EMAIL_HOST_USER)

    return None


def dealine_month(*args, **kwargs):
    subject = "Deadline Notification "
    message = "We just want to inform you that, Name has not been submitted on time." \
              "Thank you"
    send_mail(subject, message, EMAIL_HOST_USER, EMAIL_HOST_USER)

    return None

def dealine_term(*args, **kwargs):
    subject = "Welcome "
    message = 'New Report has been added successfully !!!'
    send_mail(subject, message, EMAIL_HOST_USER, EMAIL_HOST_USER)

    return None

def dealine_sem(*args, **kwargs):
    subject = "Deadline Notification "
    message = "We just want to inform you that, Name has not been submitted on time." \
              "Thank you"
    send_mail(subject, message, EMAIL_HOST_USER, EMAIL_HOST_USER)

    return None

def dealine_year(*args, **kwargs):
    subject = "Deadline Notification "
    message = "We just want to inform you that, Name has not been submitted on time." \
              "Thank you"
    send_mail(subject, message, EMAIL_HOST_USER, EMAIL_HOST_USER)

    return None



# ========================================================== START FUNCTION=======================================================

# start scheduler email remainder and call all needed functions, that generate
def start(deadline):
    week = all_users_emails_week()
    month = all_users_emails_monthly()
    term = all_users_emails_term()

    report_n = Report.objects.all()

    reports_n = ReportType.objects.all()
    reports = ReportType.objects.all()



    for simple in reports:
        if simple.igihe_itangirwa == 1:

            deadlina = next_weekday(d, 3)
            scheduler = BackgroundScheduler()
            scheduler.add_job(mailweek, 'date', run_date=deadlina)
            for reports in reports_n:
                for repo in report_n:
                    if repo.submitted_on > reports.deadline:
                        scheduler.add_job(dealine_week, 'date', run_date=repo.submitted_on )
                        scheduler.start()
            scheduler.start()

        elif simple.igihe_itangirwa == 2:
            from calendar import monthrange

            days_in_month = lambda dt: monthrange(dt.year, dt.month)[1]
            today = date.today()
            therd_day = today.replace(day=3) + timedelta(days_in_month(today))

            scheduler = BackgroundScheduler()
            scheduler.add_job(mailmonth, 'date', run_date=therd_day)
            for reports in reports_n:
                for repo in report_n:
                    if repo.submitted_on > reports.deadline:
                        scheduler.add_job(dealine_month, 'date', run_date=repo.submitted_on )
                        scheduler.start()
            scheduler.start()

        elif simple.igihe_itangirwa == 3:

            deadlina = trimester_from_now()
            scheduler = BackgroundScheduler()
            scheduler.add_job(mailterm, 'date', run_date=deadlina)
            for reports in reports_n:
                for repo in report_n:
                    if repo.submitted_on > reports.deadline:
                        scheduler.add_job(dealine_term, 'date', run_date=repo.submitted_on )
                        scheduler.start()
            scheduler.start()

        elif simple.igihe_itangirwa == 4:
            deadlina = datetime.datetime.now() + timedelta((6*365/12))
            scheduler = BackgroundScheduler()
            scheduler.add_job(mailsemester, 'date',run_date=deadlina)
            for reports in reports_n:
                for repo in report_n:
                    if repo.submitted_on > reports.deadline:
                        scheduler.add_job(dealine_sem, 'date', run_date=repo.submitted_on )
                        scheduler.start()

            scheduler.start()

        elif simple.igihe_itangirwa == 5:
            deadlina = datetime.datetime.now() + timedelta((12*365/12))
            scheduler = BackgroundScheduler()
            scheduler.add_job(mailyear, 'date', run_date=deadlina)
            for reports in reports_n:
                for repo in report_n:
                    if repo.submitted_on > reports.deadline:
                        scheduler.add_job(dealine_year, 'date', run_date=repo.submitted_on )
                        scheduler.start()

            scheduler.start()


