from django.contrib import admin
from .models import ReportType, Report

class ReportAdminb(admin.ModelAdmin):
        list_display = ('report_type','igihe_itangirwa','deadline','owner')

class ReportAdmin(admin.ModelAdmin):
        list_display = ('report_type','report_file','submitted_on',)

admin.site.register(Report, ReportAdmin)

admin.site.register(ReportType,ReportAdminb)
