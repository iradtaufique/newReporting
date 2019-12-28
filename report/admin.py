from django.contrib import admin
from .models import ReportType, Report


class ReportAdmin(admin.ModelAdmin):
        list_display = ('report_type','report_file','submited_date',)

admin.site.register(Report, ReportAdmin)

admin.site.register(ReportType)
